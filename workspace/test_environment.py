#!/usr/bin/env python3
"""
Test script to verify the Python environment in the container.
"""
import sys
import subprocess
import json

def check_python_version():
    """Check Python version and installed packages."""
    print("=== Python Environment ===")
    print(f"Python version: {sys.version}")
    
    try:
        import anthropic
        print(f"✅ anthropic version: {anthropic.__version__}")
    except ImportError:
        print("❌ anthropic package not found")
    
    print("\n=== Installed Packages ===")
    subprocess.run(["pip", "list"], check=True)

def check_node_environment():
    """Check Node.js and npm versions."""
    print("\n=== Node.js Environment ===")
    try:
        # Check Node.js version
        node_version = subprocess.check_output(["node", "--version"], text=True).strip()
        print(f"Node.js version: {node_version}")
        
        # Check npm version
        npm_version = subprocess.check_output(["npm", "--version"], text=True).strip()
        print(f"npm version: {npm_version}")
        
        # Check if @anthropic-ai/cli is installed
        try:
            claude_version = subprocess.check_output(
                ["npm", "list", "-g", "@anthropic-ai/cli", "--json"],
                stderr=subprocess.DEVNULL,
                text=True
            )
            claude_info = json.loads(claude_version)
            if "version" in claude_info:
                print(f"✅ @anthropic-ai/cli version: {claude_info['version']}")
            else:
                print("✅ @anthropic-ai/cli is installed")
        except subprocess.CalledProcessError:
            print("❌ @anthropic-ai/cli not found in global npm packages")
            
    except FileNotFoundError as e:
        print(f"❌ {e.filename} not found. Is Node.js installed?")

def main():
    """Run all checks."""
    check_python_version()
    check_node_environment()
    
    print("\n=== Environment Test Complete ===")

if __name__ == "__main__":
    main()
