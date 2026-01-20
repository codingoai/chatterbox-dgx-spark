#!/bin/bash
# Load .env file using --env-file if it exists
ENV_ARGS=""
if [ -f .env ]; then
  ENV_ARGS="--env-file .env"
fi

docker run --gpus all -it --rm \
  -v $(pwd)/source_code:/workspace/chatterbox \
  $ENV_ARGS \
  -e HF_HUB_ENABLE_HF_TRANSFER=1 \
  chatterbox:latest
