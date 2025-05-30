#!/bin/bash

echo "executing script...."
START_CMD="python -m app.server"

# cp /etc/config/env.txt /usr/src/$PROJECT_NAME/.env
# cp -r /etc/config/certs /usr/src/$PROJECT_NAME/certs

$START_CMD
