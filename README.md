
<p align="center">
  <a href="https://portal.evolution.land/">
    <img src="https://avatars.githubusercontent.com/u/40032386?s=200&v=4" alt="Logo" width="80" height="80">
  </a>
  <p align="center">
    <a href="https://portal.evolution.land/">Evolution Land</a> backend service provides game data such as land plots, apostles, NFT assets, etc.
    <br />
    <br />
    <br />
    <a href="https://portal.evolution.land/">View Evolution Land Game</a>
    ·
    <a href="https://github.com/orgs/evolutionlandorg/discussions/new?category=q-a">Report Bug</a>
    ·
    <a href="https://github.com/orgs/evolutionlandorg/discussions/new?category=ideas">Suggest New Features</a>
  </p>
</p>

### Repository Overview

Evolution Land consists of several key repositories that work together to create the complete gaming experience:

* **[evo-backend-server](https://github.com/evolutionlandorg/evo-backend-server)**: The core backend service that handles API requests, data processing, and game state management.

* **[evo-frontend](https://github.com/evolutionlandorg/evo-frontend)**: The user interface and interactive elements of Evolution Land, built with modern web technologies.

* **[evo-apostle-svg](https://github.com/evolutionlandorg/evo-apostle-svg)**: A collection of SVG icons and badges for Apostles, providing visual representation for in-game characters.

* **[market-contracts](https://github.com/evolutionlandorg/market-contracts)**: Smart contracts powering the Dutch auction marketplace, enabling secure and decentralized trading of game assets.

* **[raffle](https://github.com/evolutionlandorg/raffle)**: Smart contracts managing the lottery and raffle systems within the game.

* **[land](https://github.com/evolutionlandorg/land)**: Smart contracts handling the ownership, transfer, and management of virtual land plots.

* **[token-contracts](https://github.com/evolutionlandorg/token-contracts)**: Smart contracts for various tokens used within the Evolution Land ecosystem.
* **[evo-deploy](https://github.com/evolutionlandorg/evo-deploy)**: Deployment contracts for Evolution Land.

### Deployment Guide

Getting started with Evolution Land backend is straightforward:

1. Clone the repository:
   ```bash
   git clone https://github.com/evolutionlandorg/evolutionland.git
   ```

2. Navigate to the Docker deployment directory:
   ```bash
   cd deploy/docker
   ```

3. Run the deployment script:
   ```bash
   bash ./start.sh
   ```

4. Visit [evo-frontend](https://github.com/evolutionlandorg/evo-frontend) to deploy the frontend service.

5. If you want to deploy the contracts, please refer to [evo-deploy](https://github.com/evolutionlandorg/evo-deploy).

The script will guide you through setting up MySQL credentials and data directories, and will automatically deploy all necessary services using Docker Compose.

#### New Network Deployment Guide

This guide walks you through deploying Evolution Land on a new blockchain network.

##### Prerequisites
- Python and pip installed
- Access to wallet credentials
- Docker environment (if using evo-backend)

##### Deployment Steps

1. **Deploy Smart Contracts**
   - Use [evo-deploy](https://github.com/evolutionlandorg/evo-deploy) to deploy contracts to your target network
   - Follow the deployment instructions in the evo-deploy repository

2. **Configure Land Resources**
   - Generate land resource information
   - Format it according to [init/example_land_resource.json](init/example_land_resource.json) template
   - Ensure resource distribution matches your game design

3. **Set Up Configuration**
   - Navigate to [init/conf/conf.py](init/conf/conf.py)
   - Configure the following:
     - Wallet address
     - Private key
     - New network name
     - Other network-specific parameters

4. **Generate Land Plots**
   ```bash
   cd ./init
   pip install -r requirements.txt
   export CHAIN=<new_network_name>
   python land.py
   ```

5. **Update Backend Configuration**
   - Add network configuration JSON file to [evo-backend-server/config](https://github.com/evolutionlandorg/evo-backend-server/tree/main/config)
   - Redeploy the `evo-backend` service
   - Initialize land data by running:
     ```bash
     docker exec -it evo-backend /app/evo-backend InitLandsFormChain <new_network_name_in_config>
     ```

6. **Configure and Deploy Apostles**
   - Update [init/apostle.py](init/apostle.py):
     - Set desired apostle genes array
     - Configure apostle owner address
   - Generate apostles:
     ```bash
     cd ./init
     export CHAIN=<new_network_name>
     python apostle.py
     ```

7. **Set Up Marketplace**
   - List apostles for auction:
     ```bash
     cd ./init
     export CHAIN=<new_network_name>
     python apostleAuction.py
     ```
   - List land plots for auction:
     ```bash
     cd ./init
     export CHAIN=<new_network_name>
     python clockAuction.py
     ```

##### Notes
- Ensure each step completes successfully before proceeding to the next
- Back up important data before making changes
- Monitor transaction status on your blockchain explorer
- Consider gas fees and network conditions when deploying contracts and creating assets

### System Requirements

- Docker and Docker Compose
- Minimum 4GB RAM
- 20GB available disk space
- Internet connection for downloading container images and initial data

### Architecture Overview

Evolution Land backend uses a microservices architecture with the following components:

- **API Server**: Handles game logic and client requests
- **MySQL Database**: Stores game state and user data
- **Redis Cache**: Provides high-speed data caching
- **Apostle SVG Server**: Generates dynamic character images

### License

This project is open source and available under the MIT License. See [LICENSE.txt](https://github.com/evolutionlandorg/evolutionland/master/LICENSE.txt) for complete license terms.

### Contributing

We welcome contributions! Please feel free to submit pull requests or open issues for any improvements you'd like to suggest.

### Support

If you need help or have questions:
- Open a [GitHub Discussion](https://github.com/orgs/evolutionlandorg/discussions)
- Visit our [Documentation](https://docs.evolution.land)