from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai
import os
from datetime import datetime
import json

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
CORS(app)

# Configure Gemini API
# You'll need to set your API key as an environment variable
# export GEMINI_API_KEY="your_api_key_here"
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if not GEMINI_API_KEY:
    print("Warning: GEMINI_API_KEY environment variable not set")
    GEMINI_API_KEY = "your_api_key_here"  # Replace with your actual API key

genai.configure(api_key=GEMINI_API_KEY)

# Initialize Gemini 1.5 Flash model
model = genai.GenerativeModel('gemini-1.5-flash')

class TravelPlannerAI:
    def __init__(self):
        self.model = model
    
    def generate_travel_plan(self, source, destination, dates, budget, travelers, interests):
        """Generate a comprehensive travel plan using Gemini AI"""
        
        prompt = f"""
        You are an expert travel planner. Create a detailed, personalized travel itinerary based on the following information:

        **Travel Details:**
        - Source: {source}
        - Destination: {destination}
        - Travel Dates: {dates}
        - Budget: ${budget} USD
        - Number of Travelers: {travelers}
        - Interests: {interests}

        **Please provide a comprehensive travel plan that includes:**

        1. **Flight Information:**
           - Recommended flight times and airlines
           - Estimated flight costs
           - Best booking tips

        2. **Accommodation Recommendations:**
           - 3-4 hotel/accommodation options with different price ranges
           - Location benefits and amenities
           - Estimated costs per night

        3. **Daily Itinerary:**
           - Day-by-day activities based on interests
           - Must-visit attractions and hidden gems
           - Estimated time for each activity
           - Transportation between locations

        4. **Budget Breakdown:**
           - Detailed cost estimation for flights, accommodation, food, activities, and transportation
           - Money-saving tips
           - Budget allocation suggestions

        5. **Local Information:**
           - Best local restaurants and cuisine to try
           - Cultural etiquette and tips
           - Weather considerations and packing suggestions
           - Local transportation options

        6. **Safety and Practical Tips:**
           - Important safety information
           - Required documents/visas
           - Emergency contacts and useful phrases
           - Currency and payment methods

        Please format the response in a clear, organized manner with proper headings and bullet points. Make it engaging and personalized based on the traveler's interests.
        """

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating travel plan: {str(e)}"

# Initialize the travel planner
travel_planner = TravelPlannerAI()

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/api/generate-plan', methods=['POST'])
def generate_plan():
    """API endpoint to generate travel plan"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['source', 'destination', 'dates', 'budget', 'travelers', 'interests']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Extract data
        source = data['source']
        destination = data['destination']
        dates = data['dates']
        budget = data['budget']
        travelers = data['travelers']
        interests = data['interests']
        
        # Generate travel plan
        travel_plan = travel_planner.generate_travel_plan(
            source, destination, dates, budget, travelers, interests
        )
        
        return jsonify({
            'success': True,
            'travel_plan': travel_plan,
            'request_data': data
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'model': 'gemini-1.5-flash'})

if __name__ == '__main__':
    print("Starting Travel Planner AI Server...")
    print("Make sure to set your GEMINI_API_KEY environment variable")
    print("Server will run on http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)