#!/bin/bash

# Create workspace directory if it doesn't exist
mkdir -p workspace

# Build and start the container
docker-compose -f docker-compose.claude-code.yml up -d

# Install Claude Code globally in the container
docker-compose -f docker-compose.claude-code.yml exec -u node claude-code npm install -g @anthropic-ai/claude-code

# Start an interactive shell in the container
echo "Starting Claude Code container..."
echo "Run 'claude' to start Claude Code"
echo "Your workspace is mounted at /workspace"

docker-compose -f docker-compose.claude-code.yml exec -u node -it claude-code /bin/bash
