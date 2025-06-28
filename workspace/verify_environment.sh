#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== Verifying Containerized Development Environment ===${NC}"

# Function to run a command and check its exit status
run_command() {
    local container=$1
    local command=$2
    local description=$3
    
    echo -n "${description}... "
    if docker exec "${container}" bash -c "${command}" > /dev/null 2>&1; then
        echo -e "${GREEN}✓${NC}"
        return 0
    else
        echo -e "${RED}✗${NC}"
        return 1
    fi
}

# Check if containers are running
check_containers() {
    local vs_code_running=false
    local claude_cli_running=false
    
    if docker ps --format '{{.Names}}' | grep -q '^claude-vscode$'; then
        vs_code_running=true
    fi
    
    if docker ps --format '{{.Names}}' | grep -q '^claude-code$'; then
        claude_cli_running=true
    fi
    
    if [ "$vs_code_running" = true ] && [ "$claude_cli_running" = true ]; then
        return 0
    else
        return 1
    fi
}

# Main verification
echo -e "\n${GREEN}=== Checking Containers ===${NC}"
if ! check_containers; then
    echo -e "${RED}Error: One or more containers are not running.${NC}"
    echo -e "Make sure to start the containers with: docker-compose -f docker-compose.claude-code.yml up -d"
    exit 1
else
    echo -e "✓ All required containers are running"
fi

# Test VS Code container
echo -e "\n${GREEN}=== Testing VS Code Container ===${NC}"
run_command "claude-vscode" "python3 --version" "Checking Python installation"
run_command "claude-vscode" "python3 -c 'import anthropic'" "Checking Claude Python package"
run_command "claude-vscode" "node --version" "Checking Node.js installation"
run_command "claude-vscode" "code-server --version" "Checking VS Code Server installation"

# Test Claude Code CLI container
echo -e "\n${GREEN}=== Testing Claude Code CLI Container ===${NC}"
run_command "claude-code" "node --version" "Checking Node.js installation"
run_command "claude-code" "npm list -g @anthropic-ai/sdk" "Checking Claude SDK installation"

# Test file sharing
echo -e "\n${GREEN}=== Testing File Sharing ===${NC}"
TEST_FILE="test_shared_file_$(date +%s).txt"
TEST_CONTENT="This is a test file created at $(date)"
echo "$TEST_CONTENT" > "./workspace/$TEST_FILE"

if docker exec claude-vscode test -f "/workspace/$TEST_FILE" && \
   docker exec claude-code test -f "/workspace/$TEST_FILE"; then
    echo -e "✓ File sharing is working correctly"
    
    # Verify file content
    if [ "$(cat "./workspace/$TEST_FILE")" = "$TEST_CONTENT" ]; then
        echo -e "✓ File content is preserved"
    else
        echo -e "${RED}✗ File content is corrupted${NC}"
    fi
else
    echo -e "${RED}✗ File sharing is not working correctly${NC}"
fi

# Clean up
rm -f "./workspace/$TEST_FILE"

echo -e "\n${GREEN}=== Environment Verification Complete ===${NC}"
echo -e "Access VS Code at: ${GREEN}http://localhost:8082${NC}"
echo -e "Access Claude CLI: ${GREEN}docker exec -it claude-code bash${NC}"
