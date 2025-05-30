## Setup
1. Setup virtualenv
    ```bash
    python3 -m venv env
    ```
2. Activate venv
    ```bash
    source env/bin/activate
    ```
3. Check if python is correctly pointing to the virtual env
   ```bash
   which python3
   ```
4. Install dependencies
   ```bash
   python3 -m pip install -r requirements.txt
   ```
5. **Setup .env file** : At the root directory setup the .env file with the secrets
```bash
ENV=development
PREFIX=/
ROOT_PATH=/whatsapp-agent
PORT=8000
WORKERS=1

# Build args
PROJECT_NAME=whatsapp_agent
BASE_IMAGE=python:3.11-slim
REPOSITORY_NAME=docker.io/anieshaz

# Database settings
DB_TYPE=postgresql
DB_USER=myuser
DB_PASSWORD=mypassword
DB_HOST=db
DB_PORT=5432
DB_NAME=mydatabase
```

## Testing
Before pushing any changes make sure that all the tests are passing by running.

```bash
python3 -m pytest
```

## API

### Running The API server

```bash
python3 -m app.server
```

### Try out apis

You can explore the API by visiting the .http files in the `requests` folder and running them using the Rest Client plugin in VSCode.

> Note: The .vscode folder is already included in the repo.

  - Install [Rest client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) plugin from VSCode marketplace.
  - If the .vscode folder isn’t present, create it in the root directory and add the following to settings.json:
    ```json
        "rest-client.environmentVariables": {
          "development": {
            "baseUrl": "http://localhost:8000"
          },
          "production": {
            "baseUrl": "https://example.production.com/api"
          }
        }
    ```
- Use `Ctrl+Shift+P` to open the command palette, type `Rest Client: Switch Environment`, and select the desired environment.
- Navigate to the `requests` folder and start executing API requests for the environment.

## Containerizing the server

> Note : Podman is necessary for this setup, colima can also be used with slight modifications.

### Building image
Update the version number for new builds, then run:

```bash
sh ./build.sh
```

## Running with docker-compose

```bash
docker-compose -p demo up -d --build app
```

```bash
docker-compose -p demo down
```