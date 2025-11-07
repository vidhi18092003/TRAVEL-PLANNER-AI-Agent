#!/usr/bin/env python3
"""
Test script for Travel Planner AI app
"""

import sys
import os

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

def test_imports():
    """Test if all required packages can be imported"""
    print("🧪 Testing imports...")
    
    try:
        import flask
        print("✅ Flask imported successfully")
    except ImportError:
        print("❌ Flask not found - install with: pip install Flask")
        return False
    
    try:
        import flask_cors
        print("✅ Flask-CORS imported successfully")
    except ImportError:
        print("❌ Flask-CORS not found - install with: pip install Flask-CORS")
        return False
    
    try:
        import google.generativeai as genai
        print("✅ Google Generative AI imported successfully")
    except ImportError:
        print("❌ Google Generative AI not found - install with: pip install google-generativeai")
        return False
    
    return True

def test_api_connection():
    """Test Gemini API connection"""
    print("\n🔗 Testing Gemini API connection...")
    
    try:
        import google.generativeai as genai
        
        # Use the same API key as in app.py
        api_key = "AIzaSyCllwZ6qmw35eMyfd8HJRVfzX6SNffSFGU"
        genai.configure(api_key=api_key)
        
        # Initialize model
        model = genai.GenerativeModel('gemini-1.5-flash')
        print("✅ Gemini 1.5 Flash model initialized")
        
        # Test API call
        print("🧪 Testing API call...")
        response = model.generate_content("Hello! Please confirm you are Gemini 1.5 Flash and say hello back.")
        
        print("✅ API call successful!")
        print(f"Response: {response.text[:100]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ API test failed: {e}")
        return False

def test_flask_app():
    """Test if Flask app can be imported and initialized"""
    print("\n🌐 Testing Flask app...")
    
    try:
        # Import the app
        from app import app, travel_planner
        print("✅ Flask app imported successfully")
        
        # Test the travel planner class
        if travel_planner:
            print("✅ TravelPlannerAI initialized successfully")
        
        return True
        
    except Exception as e:
        print(f"❌ Flask app test failed: {e}")
        return False

def main():
    print("🚀 Travel Planner AI - System Test")
    print("=" * 50)
    
    # Test imports
    if not test_imports():
        print("\n❌ Import test failed. Please install missing packages.")
        return
    
    # Test API connection
    if not test_api_connection():
        print("\n❌ API test failed. Please check your internet connection.")
        return
    
    # Test Flask app
    if not test_flask_app():
        print("\n❌ Flask app test failed.")
        return
    
    print("\n" + "=" * 50)
    print("🎉 All tests passed! Your Travel Planner AI is ready to run!")
    print("\nTo start the application:")
    print("1. Run: python backend/app.py")
    print("2. Open browser to: http://localhost:5000")
    print("3. Or just double-click run.bat")

if __name__ == "__main__":
    main()