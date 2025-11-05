# sampo-dashboard

## Development Setup

### 1. Clone the repository

To clone the [repository](https://github.com/eScienceLab/sampo-dashboard), click `<> Code` above the list of files on the GitHub page of this repo, and copy the URL under your choice of clone method (HTTPS / SSH Key / GitHub CLI). 

In the CLI: \
`git clone <URL>`

Change into the project directory for the following steps: \
`cd sampo-dashboard`

### 2. Configure .env

Make a copy of `env.template`, rename it to `.env` and populate the variables.

### 3. Build Docker images and start containers

The following command builds the development Docker images (`--build`) before starting containers in detached mode (`-d`).

`docker compose -f docker-compose.dev.yml up -d --build`

### 4. Stop and remove containers and networks

`docker compose -f docker-compose.dev.yml down`
