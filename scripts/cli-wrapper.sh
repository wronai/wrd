#!/bin/bash
# Wrapper script for Claude CLI in the VS Code container

# Set NODE_PATH to include global node_modules
NODE_PATH=$(npm root -g)
export NODE_PATH

# Check if running in a terminal
if [ ! -t 1 ]; then
    echo "Error: This script must be run in a terminal"
    exit 1
fi

# Check if Node.js is available
if ! command -v node &> /dev/null; then
    echo "Error: Node.js is not installed"
    exit 1
fi

# Check if the Anthropic SDK is installed
if ! npm list -g @anthropic-ai/sdk &> /dev/null; then
    echo "Installing @anthropic-ai/sdk..."
    if ! npm install -g @anthropic-ai/sdk; then
        echo "Error: Failed to install @anthropic-ai/sdk"
        exit 1
    fi
    # Update NODE_PATH after installation
    NODE_PATH=$(npm root -g)
    export NODE_PATH
fi

# Check if API key is set
if [ -z "$ANTHROPIC_API_KEY" ] && [ -f "/workspace/.env" ]; then
    # Try to load from .env file if not set
    export $(grep -v '^#' /workspace/.env | xargs)
fi

if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "Warning: ANTHROPIC_API_KEY environment variable is not set"
    echo "Please add your API key to the .env file or enter it below:"
    read -p "Enter your Anthropic API key: " api_key
    export ANTHROPIC_API_KEY="$api_key"
    
    # Update .env file
    if [ -w "/workspace/.env" ]; then
        if grep -q "^ANTHROPIC_API_KEY=" /workspace/.env; then
            sed -i "s/^ANTHROPIC_API_KEY=.*/ANTHROPIC_API_KEY=$api_key/" /workspace/.env
        else
            echo "ANTHROPIC_API_KEY=$api_key" >> /workspace/.env
        fi
        echo "API key saved to .env file"
    fi
fi

# Debug information (can be removed later)
echo "NODE_PATH: $NODE_PATH"
echo "Node.js version: $(node -v)"

# Start Node.js REPL with Claude SDK preloaded
node -e "
// Print module search paths for debugging
console.log('Module search paths:', require('module')._nodeModulePaths(process.cwd()));

try {
  // Try to load the SDK
  const { Anthropic } = require('@anthropic-ai/sdk');
  console.log('Successfully loaded @anthropic-ai/sdk');
  
  const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  });

  const anthropic = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY
  });

  console.log('Claude CLI - Type your message and press Enter. Type "exit" to quit.');
  console.log('Using model: claude-3-opus-20240229');
  console.log('API Key:', process.env.ANTHROPIC_API_KEY ? '*** (set)' : 'Not set!');

  async function chat() {
    const messages = [];
    
    while (true) {
      const userInput = await new Promise(resolve => 
        readline.question('\nYou: ', resolve)
      );
      
      if (userInput.toLowerCase() === 'exit') {
        console.log('Goodbye!');
        process.exit(0);
      }
      
      messages.push({ role: 'user', content: userInput });
      
      try {
        process.stdout.write('\nClaude: ');
        
        const stream = await anthropic.messages.create({
          model: 'claude-3-opus-20240229',
          max_tokens: 1000,
          messages: messages,
          stream: true
        });
        
        let fullResponse = '';
        for await (const chunk of stream) {
          process.stdout.write(chunk.delta.text || '');
          fullResponse += chunk.delta.text || '';
        }
        
        messages.push({ role: 'assistant', content: fullResponse });
        console.log('\n');
        
      } catch (error) {
        console.error('\nError:', error.message);
        if (error.response) {
          console.error('Response status:', error.response.status);
          console.error('Response data:', error.response.data);
        }
      }
    }
  }
  
  chat().catch(console.error);
} catch (error) {
  console.error('Failed to initialize Claude SDK:', error);
  console.error('NODE_PATH:', process.env.NODE_PATH);
  console.error('Global node_modules:', require('child_process').execSync('npm root -g').toString().trim());
  process.exit(1);
}
"
