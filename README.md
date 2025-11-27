# RO-Crate Profile Portal

## About

RO-Crates are a method for packaging research data with their metadata. RO-Crate Profiles define the conventions, types and properties to do this for specific communities and domains.

## Submitting a profile to the portal

The profile portal is accepting contributions! 

> [!IMPORTANT]
> To be accepted, the profile must be a [Profile Crate](url) accessible on the public internet.

To add your profile (or a profile you feel is missing):
- Open `scripts/profile_urls.txt` in this repo for editing (click file, then click pencil icon)
- Append the URL of your profile to the file on a new line
- Click `Commit Changes` and select `Create a new branch for this commit and start a pull request`
- In the `Open a pull request window`, click `Create pull request` - the RO-Crate team will now be notified about your request
- When the pull request page has opened, you will notice some automated checks running
  - :white_check_mark: If successful: all good, the team will review and merge your request
  - :x: If the check fails: there is an error or problem with your URL, either click the link to view the error message and debug or [raise a ticket for the RO-Crate team here](https://github.com/eScienceLab/sampo-dashboard/issues) 

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
