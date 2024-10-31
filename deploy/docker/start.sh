#! /bin/bash

log() {
    local level=$1
    local message=$2
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    printf "[%-19s] %-7s %s\n" "$timestamp" "[$level]" "$message"
}

info() {
    log "INFO" "$1"
}

warn() {
    log "WARN" "$1"
}

error() {
    log "ERROR" "$1"
}

read -p "Please input mysql password(default: random generate): " MYSQL_PASSWORD
if [ -z "$MYSQL_PASSWORD" ]; then
    MYSQL_PASSWORD=$(openssl rand -hex 32)
    warn "Generated new MySQL password. Please save it securely!"
    info "MySQL Password: $MYSQL_PASSWORD"
fi

read -p "Please input mysql data directory(default: ./mysql): " MYSQL_DATA_DIR
if [ -z "$MYSQL_DATA_DIR" ]; then
    MYSQL_DATA_DIR="./mysql"
fi
MYSQL_PORT=13306
REDIS_PORT=16379
MYSQL_DB="evo"
API_SERVER_PORT=2333
APOSTLE_SVG_SERVER_PORT=1337
need_init_mysql_data=false
if [ ! -d "$MYSQL_DATA_DIR/data" ]; then
    if [ ! -f "$MYSQL_DATA_DIR/consensus-backend.sql" ]; then
        info "MySQL data directory not found. Starting download process..."
        info "Downloading MySQL initial data from remote server..."
        wget https://gcs.evolution.land/mysql_data.tar.gz -O mysql_data.tar.gz || {
            error "Failed to download MySQL data"
            exit 1
        }
        info "Extracting MySQL data to $MYSQL_DATA_DIR..."
        tar -xzf mysql_data.tar.gz -C $MYSQL_DATA_DIR || {
            error "Failed to extract MySQL data"
            exit 1
        }
        info "Cleaning up temporary files..."
        rm mysql_data.tar.gz
        info "MySQL data preparation completed successfully"
    fi
    need_init_mysql_data=true
fi

if [ ! -d "$MYSQL_DATA_DIR" ]; then
    info "MySQL data directory not found. Creating..."
    mkdir -p $MYSQL_DATA_DIR
fi

export MYSQL_PASSWORD=$MYSQL_PASSWORD
export MYSQL_DATA_DIR="$MYSQL_DATA_DIR"
export MYSQL_PORT=$MYSQL_PORT
export REDIS_PORT=$REDIS_PORT
export MYSQL_DB=$MYSQL_DB
export API_SERVER_PORT=$API_SERVER_PORT
export APOSTLE_SVG_SERVER_PORT=$APOSTLE_SVG_SERVER_PORT

docker-compose stop && docker-compose rm -f && docker-compose up -d

if $need_init_mysql_data; then
    mysql_container_name="evolutionland-backend-evo-mysql-1"
    info "Initializing MySQL database..."
    info "Waiting for MySQL service to be ready..."
    
    while ! docker exec -it $mysql_container_name mysqladmin ping -h localhost -uevo -p$MYSQL_PASSWORD | grep "mysqld is alive"; do
        info "MySQL service is starting... (retrying in 1 second)"
        sleep 1
    done
    
    info "MySQL service is now available"
    info "Waiting for 10 seconds to ensure MySQL is fully initialized..."
    sleep 10
    
    info "Starting data import process..."
    if docker exec -it $mysql_container_name mysql -uevo -p$MYSQL_PASSWORD $MYSQL_DB -e "source /bitnami/mysql/consensus-backend.sql;"; then
        info "Database import completed successfully"
    else
        error "Failed to import database data"
        exit 1
    fi
fi

docker restart evolutionland-evo-backend-1

info "Checking evo-backend service status..."
while ! curl -s http://localhost:$API_SERVER_PORT/api/v1/health | grep "not found"; do
    info "Waiting for evo-backend to start... (retrying in 1 second)"
    sleep 1
done
info "✨ Evo-backend service is now ready and operational"