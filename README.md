# container-mgmt-app

```bash
├── app/
│   ├── __init__.py
│   │── config.yml   
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── endpoints.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── config_loader.py
│   │   ├── fee_calculator.py
│   └── tests/
│       ├── __init__.py
│       ├── test_endpoints.py
│       ├── test_fee_calculation.py
│
├── Dockerfile
├── docker-compose.yml
└── README.md
```

# Container Management Case Study API

This project implements a RESTful API to manage demurrage and detention fees for shipping containers. The API is built using FastAPI and can be easily run using Docker.

## Features

- **Create Container**: Add a new shipping container to the system.
- **Update Container**: Update an existing container or add a new shipping container to the system.
- **Get Container**: Retrieve details of a specific container.
- **Get All Containers**: Retrieve a list of all containers.
- **Calculate Fees**: Calculate demurrage and detention fees for a container.
- **Get Fees**: Retrieve the calculated fees for a specific container.
- **Generate Statistics**: Generate and return statistics about container usage and fees.

## Requirements

- Github Account [Sign Up here](https://github.com)
- Git [How to Install](https://git-scm.com/downloads)
- Docker & Docker Compose ([How to Install](https://docs.docker.com/compose/install/))

## Installation

1. Clone the repository:

```bash
   git clone https://github.com/rishabh-oswal-github/container-mgmt-app.git
   cd container-mgmt-app
```

2. Build and run the Docker container:

```bash
   docker compose up --build
```

3. The API will be available at http://localhost:8000

4. The API Docs will be avialable at http://localhost:8000/docs OR http://localhost:8000/redoc
