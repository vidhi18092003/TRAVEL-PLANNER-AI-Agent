#!/usr/bin/env python3
"""
Setup script for Travel Planner AI
This script helps set up the environment and dependencies
"""

import os
import subprocess
import sys

def install_requirements():
    """Install Python requirements"""
    print("Installing Python dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "backend/requirements.txt"])
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def check_api_key():
    """Check if API key is set"""
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key or api_key == 'your_api_key_here':
        print("⚠️  GEMINI_API_KEY not found or not set properly!")
        print("Please set your API key using one of these methods:")
        print("1. Set environment variable: set GEMINI_API_KEY=your_actual_key")
        print("2. Create a .env file in the backend directory")
        print("3. Edit the app.py file directly (not recommended)")
        return False
    else:
        print("✅ GEMINI_API_KEY is set!")
        return True

def main():
    print("🚀 Travel Planner AI Setup")
    print("=" * 40)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required!")
        sys.exit(1)
    
    print(f"✅ Python {sys.version.split()[0]} detected")
    
    # Install requirements
    if not install_requirements():
        sys.exit(1)
    
    # Check API key
    api_key_set = check_api_key()
    
    print("\n" + "=" * 40)
    print("Setup Summary:")
    print("✅ Dependencies installed")
    print("✅ Project structure ready" if api_key_set else "⚠️  API key needs to be configured")
    
    if api_key_set:
        print("\n🎉 Setup complete! You can now run the application:")
        print("   python backend/app.py")
        print("   or double-click run.bat")
    else:
        print("\n⚠️  Please configure your API key before running the application.")
    
    print("\n📖 For detailed instructions, see README.md")

if __name__ == "__main__":
    main()