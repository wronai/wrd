# Claude Code Setup Guide

This guide provides comprehensive instructions for setting up Claude Code on Linux systems, including Fedora. Claude Code is a powerful AI coding assistant that can be accessed via the command line.

## Prerequisites

- A Linux distribution (tested on Fedora, Ubuntu, and Debian)
- Node.js (v16 or later recommended)
- npm (Node Package Manager)
- Python 3.8+ (for alternative Python client)
- Git
- An Anthropic API key

## Installation Methods

### Method 1: Using the Installation Script (Recommended)

We provide a convenient installation script that handles all the setup for you:

1. Download the installation script:
   ```bash
   curl -O https://raw.githubusercontent.com/wronai/wrd/main/install_claude_code.sh
   chmod +x install_claude_code.sh
   ```

2. Run the installation script:
   ```bash
   ./install_claude_code.sh
   ```

3. The script will:
   - Install system dependencies
   - Set up Node.js using NVM (Node Version Manager)
   - Configure npm to use a local directory to avoid permission issues
   - Install the Claude Code CLI globally
   - Provide instructions for setting up your environment variables

### Method 2: Manual Installation

If you prefer to install manually, follow these steps:

1. **Install Node.js and npm**:
   ```bash
   # For Fedora
   sudo dnf install -y nodejs npm
   
   # For Debian/Ubuntu
   # sudo apt update && sudo apt install -y nodejs npm
   ```

2. **Set up npm to use a local directory** (avoids permission issues):
   ```bash
   mkdir -p ~/.npm-global
   npm config set prefix '~/.npm-global'
   echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
   source ~/.bashrc
   ```

3. **Install Claude Code CLI globally**:
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```

## Configuration

### Setting Up Your API Key

1. Get your Anthropic API key from the [Anthropic Console](https://console.anthropic.com/).

2. Set the API key as an environment variable in your shell configuration file:
   ```bash
   echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.bashrc
   source ~/.bashrc
   ```
   
   For Zsh users:
   ```bash
   echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.zshrc
   source ~/.zshrc
   ```

### WRD Integration

If you're using WRD, you can configure Claude Code by updating your `~/.wrd/config.yaml`:

```yaml
ai_tools:
  claude_code:
    enabled: true
    api_key: ${ANTHROPIC_API_KEY}  # Read from environment variable
    default_model: claude-3-opus-20240229
    max_tokens: 4000
    temperature: 0.7
```

## Usage

### Basic Usage

```bash
# Start an interactive chat session
claude-code chat

# Get a response to a single prompt
claude-code prompt "Explain how to use Claude Code"

# Specify a different model
claude-code --model claude-3-sonnet-20240229 prompt "Write a Python function to reverse a string"
```

### Common Options

- `--model`: Specify the model to use (default: claude-3-opus-20240229)
- `--max-tokens`: Maximum number of tokens to generate (default: 4000)
- `--temperature`: Controls randomness (0.0 to 1.0, default: 0.7)
- `--top-p`: Nucleus sampling parameter (0.0 to 1.0)
- `--stream`: Stream the response

### Interactive Mode

```bash
claude-code interactive
```

In interactive mode, you can:
- Type your messages and press Enter to send
- Use `Ctrl+D` to exit
- Type `/help` to see available commands

## Troubleshooting

### Permission Denied Errors

If you encounter permission errors when installing npm packages globally:

1. Make sure you've set up npm to use a local directory as shown in the installation steps
2. Ensure the npm global bin directory is in your PATH:
   ```bash
   echo 'export PATH="$(npm config get prefix)/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   ```

### Node.js Version Issues

If you need to manage multiple Node.js versions, we recommend using NVM (Node Version Manager):

```bash
# Install NVM
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash

# Install and use Node.js LTS
nvm install --lts
nvm use --lts
```

### API Key Not Found

If you get an error about the API key not being found:

1. Verify the API key is set in your environment:
   ```bash
   echo $ANTHROPIC_API_KEY
   ```
2. Make sure you've sourced your shell configuration file after adding the API key
3. Try setting the API key directly in your command:
   ```bash
   ANTHROPIC_API_KEY=your-key-here claude-code prompt "Hello"
   ```

## Advanced Usage

### Using with WRD Workflows

You can integrate Claude Code with WRD workflows by adding it to your project's workflow configuration:

```yaml
# .wrd/workflows/code_review.yaml
name: Code Review Workflow
description: Automated code review using Claude Code
triggers:
  - pull_request
  - push

jobs:
  claude-code-review:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
        
      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          
      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code
        
      - name: Run code review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          # Example: Run code review on changed files
          git diff --name-only HEAD^ HEAD | xargs -I{} sh -c '
            echo "\nReviewing $1..."
            claude-code prompt "Review this code for potential issues, security vulnerabilities, and improvements:\n\n$(cat "$1")"
          ' _ {}'
```

### Customizing the Model Behavior

You can customize how Claude Code responds by providing a system prompt:

```bash
claude-code --system "You are a senior software engineer with 10+ years of experience in Python and cloud technologies. Provide concise, professional code reviews." prompt "Review this code..."
```

## Best Practices

1. **Environment Variables**: Always use environment variables for API keys instead of hardcoding them in scripts.
2. **Model Selection**: Choose the appropriate model based on your needs:
   - `claude-3-opus-20240229`: Most capable, highest cost
   - `claude-3-sonnet-20240229`: Balanced performance and cost
   - `claude-3-haiku-20240307`: Fastest, most cost-effective
3. **Rate Limiting**: Be aware of API rate limits and implement appropriate backoff strategies in automated workflows.
4. **Error Handling**: Always implement proper error handling when using Claude Code in scripts.
5. **Security**: Never commit API keys to version control. Use environment variables or secret management solutions.

## Support

For additional help, please refer to:
- [Anthropic Documentation](https://docs.anthropic.com/)
- [WRD Documentation](https://wronai.github.io/wrd/)
- [GitHub Issues](https://github.com/wronai/wrd/issues)

## License

This documentation is part of the WRD project and is licensed under the MIT License.
