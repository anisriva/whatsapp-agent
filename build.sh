#!/bin/bash

PROJECT_NAME=${1:-whatsapp_agent}
BASE_IMAGE=${2:-python:3.11-slim}
REPOSITORY_NAME=${3:-docker.io/anieshaz}

docker build --build-arg PROJECT_NAME="$PROJECT_NAME" --build-arg BASE_IMAGE="$BASE_IMAGE" -t "$REPOSITORY_NAME/$PROJECT_NAME-image" .
