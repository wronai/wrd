#!/bin/bash

# Exit on error
set -e

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== Testing Containerized Environments ===${NC}"

# Function to run tests in a container
run_tests() {
    local container_name=$1
    local test_command=$2
    
    echo -e "\n${GREEN}Testing in ${container_name}...${NC}"
    
    if docker ps -a --format '{{.Names}}' | grep -q "^${container_name}$"; then
        echo "Running tests in ${container_name}..."
        docker exec -it "${container_name}" ${test_command}
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}✅ Tests passed in ${container_name}${NC}"
        else
            echo -e "${RED}❌ Tests failed in ${container_name}${NC}"
            exit 1
        fi
    else
        echo -e "${RED}Container ${container_name} not found. Is it running?${NC}"
        exit 1
    fi
}

# Test Python environment in VS Code container
run_tests "claude-vscode" "python3 /workspace/test_environment.py"

# Test Node.js environment in Claude Code container
run_tests "claude-code" "node --version && npm --version && npm list -g @anthropic-ai/cli"

echo -e "\n${GREEN}=== All tests completed successfully! ===${NC}"
