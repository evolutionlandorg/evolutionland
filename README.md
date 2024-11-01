<p align="center">
  <a href="https://portal.evolution.land/">
    <img src="https://avatars.githubusercontent.com/u/40032386?s=200&v=4" alt="Logo" width="80" height="80">
  </a>
  <h1 align="center">Evolution Land</h1>
  <p align="center">
    Backend service providing game data including land plots, apostles, and NFT assets
    <br />
    <a href="https://portal.evolution.land/"><strong>Play Evolution Land »</strong></a>
    <br />
    <br />
    <a href="https://docs.evolution.land">Documentation</a>
    ·
    <a href="https://github.com/orgs/evolutionlandorg/discussions/new?category=q-a">Report Bug</a>
    ·
    <a href="https://github.com/orgs/evolutionlandorg/discussions/new?category=ideas">Request Feature</a>
  </p>
</p>

## Table of Contents
- [Overview](#overview)
- [Key Components](#key-components) 
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Basic Deployment](#basic-deployment)
- [Network Deployment Guide](#network-deployment-guide)
- [Contributing](#contributing)
- [Support](#support)
- [License](#license)

## Overview
Evolution Land is a blockchain-based virtual world game with multiple components working together to create an immersive gaming experience.

## Key Components
Our ecosystem consists of several key repositories:

| Repository | Description |
|------------|-------------|
| [evo-backend-server](https://github.com/evolutionlandorg/evo-backend-server) | Core backend service for API and game state management |
| [evo-frontend](https://github.com/evolutionlandorg/evo-frontend) | User interface and interactive elements |
| [market-contracts](https://github.com/evolutionlandorg/market-contracts) | Dutch auction marketplace smart contracts |
| [land](https://github.com/evolutionlandorg/land) | Land management smart contracts |
| [token-contracts](https://github.com/evolutionlandorg/token-contracts) | Ecosystem token contracts |
| [evo-deploy](https://github.com/evolutionlandorg/evo-deploy) | Deployment contracts and tools |

## Getting Started

### Prerequisites
- Docker and Docker Compose
- Minimum 4GB RAM
- 20GB available disk space
- Internet connection

### Basic Deployment
1. Clone the repository:
   ```bash
   git clone https://github.com/evolutionlandorg/evolutionland.git
   ```

2. Deploy backend services:
   ```bash
   cd deploy/docker
   bash ./start.sh
   ```

3. Deploy frontend by following [evo-frontend](https://github.com/evolutionlandorg/evo-frontend) instructions

## Network Deployment Guide

### Prerequisites
- Python and pip installed
- Wallet credentials
- Docker environment (for backend)

### Deployment Steps

1. **Deploy Smart Contracts**
   ```bash
   # Follow evo-deploy repository instructions
   ```

2. **Generate Land Resources**
   ```bash
   cd ./init
   pip install -r requirements.txt
   export CHAIN=<network_name>
   python land.py
   ```

3. **Deploy Apostles**
   ```bash
   python apostle.py
   ```

4. **Setup Marketplace**
   ```bash
   python apostleAuction.py
   python clockAuction.py
   ```

Detailed deployment instructions can be found in our [Documentation](https://docs.evolution.land).

## Contributing
We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting pull requests.

## Support
- [GitHub Discussions](https://github.com/orgs/evolutionlandorg/discussions)
- [Documentation](https://docs.evolution.land)

## License
This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.