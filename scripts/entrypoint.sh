#!/bin/sh

# Fix permissions for the coder user
chown -R coder:coder /home/coder
chown -R coder:coder /workspace

# Ensure config directory exists
mkdir -p /home/coder/.config/code-server

# Create local bin directory
mkdir -p /home/coder/.local/bin

# Create a wrapper script for claude
cat > /usr/local/bin/claude << 'EOL'
#!/bin/sh
export NODE_PATH=/home/coder/.npm-global/lib/node_modules
exec node -e "process.env.ANTHROPIC_API_KEY='$ANTHROPIC_API_KEY'; require('@anthropic-ai/sdk').main()"
EOL

chmod +x /usr/local/bin/claude

# Install Anthropic SDK globally
echo "Installing @anthropic-ai/sdk..."
su -c "npm install -g @anthropic-ai/sdk" coder

# Generate a random token
TOKEN=$(openssl rand -hex 16)

# Set the token in config file
cat > /home/coder/.config/code-server/config.yaml << EOL
bind-addr: 0.0.0.0:8080
auth: none
password: $TOKEN
cert: false
EOL

# Set correct permissions
chown -R coder:coder /home/coder/.config

# Display the token for login
echo "========================================"
echo "VS Code Access Token: $TOKEN"
echo "Access at: http://localhost:8083"
echo ""
echo "Claude CLI is available. Type 'claude' to start."
echo "API Key: $ANTHROPIC_API_KEY"
echo "========================================"

# Start code-server as the coder user
exec su -c "code-server --bind-addr 0.0.0.0:8080 --auth none --disable-telemetry" coder
