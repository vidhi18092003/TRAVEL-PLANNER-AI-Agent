#!/usr/bin/env python3
"""
Test script to verify Gemini API connection
"""

import os
import sys
from dotenv import load_dotenv

# Add backend directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

# Load environment variables
load_dotenv('backend/.env')

try:
    import google.generativeai as genai
    
    # Get API key
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("❌ GEMINI_API_KEY not found in environment variables")
        print("Make sure you have a .env file in the backend directory with your API key")
        sys.exit(1)
    
    print(f"✅ API Key found: {api_key[:10]}...")
    
    # Configure Gemini
    genai.configure(api_key=api_key)
    
    # Initialize model
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    print("✅ Gemini model initialized successfully")
    
    # Test API call
    print("🧪 Testing API connection...")
    response = model.generate_content("Say hello and confirm you're Gemini 1.5 Flash")
    
    print("✅ API test successful!")
    print(f"Response: {response.text}")
    
    print("\n🎉 Everything is working! You can now run the Travel Planner AI:")
    print("   python backend/app.py")
    
except ImportError as e:
    print(f"❌ Missing dependency: {e}")
    print("Please install the required packages:")
    print("   python install_dependencies.py")
    
except Exception as e:
    print(f"❌ Error testing API: {e}")
    print("Please check your API key and internet connection")