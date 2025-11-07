#!/usr/bin/env python3
"""
Travel Planner AI Launcher
This script handles the complete startup process
"""

import os
import sys
import subprocess
import webbrowser
import time
from threading import Timer

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = ['flask', 'google.generativeai', 'flask_cors', 'dotenv']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    return missing_packages

def install_dependencies():
    """Install missing dependencies"""
    print("Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, 'install_dependencies.py'])
        return True
    except subprocess.CalledProcessError:
        return False

def check_api_key():
    """Check if API key is configured"""
    from dotenv import load_dotenv
    load_dotenv('backend/.env')
    
    api_key = os.getenv('GEMINI_API_KEY')
    return api_key and api_key != 'your_gemini_api_key_here'

def open_browser():
    """Open browser after a delay"""
    time.sleep(2)  # Wait for server to start
    webbrowser.open('http://localhost:5000')

def main():
    print("🚀 Starting Travel Planner AI...")
    print("=" * 50)
    
    # Check dependencies
    missing = check_dependencies()
    if missing:
        print(f"❌ Missing dependencies: {', '.join(missing)}")
        print("Installing dependencies...")
        if not install_dependencies():
            print("❌ Failed to install dependencies. Please install manually.")
            return
    
    # Check API key
    if not check_api_key():
        print("❌ Gemini API key not configured!")
        print("Please set your API key in backend/.env file")
        print("Get your key from: https://makersuite.google.com/app/apikey")
        return
    
    print("✅ All checks passed!")
    print("🌐 Starting web server...")
    print("📱 Opening browser...")
    
    # Open browser after delay
    Timer(3.0, open_browser).start()
    
    # Start the Flask app
    try:
        os.chdir('backend')
        subprocess.run([sys.executable, 'app.py'])
    except KeyboardInterrupt:
        print("\n👋 Travel Planner AI stopped.")
    except Exception as e:
        print(f"❌ Error starting application: {e}")

if __name__ == "__main__":
    main()