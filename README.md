
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

The script will guide you through setting up MySQL credentials and data directories, and will automatically deploy all necessary services using Docker Compose.

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