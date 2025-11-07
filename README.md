# Travel Planner AI

An intelligent travel planning application powered by Google's Gemini 1.5 Flash model. This application helps users create personalized travel itineraries based on their preferences, budget, and interests.

## Features

- **AI-Powered Planning**: Uses Gemini 1.5 Flash for intelligent travel recommendations
- **Comprehensive Itineraries**: Includes flights, accommodation, activities, and budget breakdowns
- **Interactive UI**: Modern, responsive web interface with interest tag selection
- **Personalized Recommendations**: Tailored suggestions based on user interests and preferences
- **Budget Planning**: Detailed cost estimations and money-saving tips
- **Local Insights**: Cultural tips, safety information, and local recommendations

## Project Structure

```
travel-planner-ai/
├── backend/
│   ├── app.py              # Main Flask application
│   ├── requirements.txt    # Python dependencies
│   └── .env.example       # Environment variables template
├── frontend/
│   ├── templates/
│   │   └── index.html     # Main HTML template
│   └── static/
│       ├── style.css      # CSS styles
│       └── script.js      # JavaScript functionality
└── README.md              # This file
```

## Setup Instructions

### Prerequisites

1. Python 3.8 or higher
2. Google Gemini API key (get it from [Google AI Studio](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd travel-planner-ai
   ```

2. **Set up the backend:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   - Copy `.env.example` to `.env`
   - Add your Gemini API key to the `.env` file:
     ```
     GEMINI_API_KEY=your_actual_api_key_here
     ```

4. **Alternative: Set environment variable directly (Windows):**
   ```cmd
   set GEMINI_API_KEY=your_actual_api_key_here
   ```

### Running the Application

1. **Start the Flask server:**
   ```bash
   cd backend
   python app.py
   ```

2. **Open your web browser and navigate to:**
   ```
   http://localhost:5000
   ```

## Usage

1. **Fill in the travel form:**
   - **Source**: Your departure city
   - **Destination**: Where you want to travel
   - **Dates**: Your travel dates (e.g., "Dec 15-22, 2024")
   - **Budget**: Your total budget in USD
   - **Travelers**: Number of people traveling
   - **Interests**: Select from predefined tags or add custom interests

2. **Generate your plan:**
   - Click "Generate Travel Plan"
   - Wait for the AI to create your personalized itinerary

3. **Review your itinerary:**
   - The AI will provide detailed recommendations including:
     - Flight information and costs
     - Accommodation options
     - Daily activity suggestions
     - Budget breakdown
     - Local tips and safety information

## API Endpoints

- `GET /` - Serves the main web interface
- `POST /api/generate-plan` - Generates travel plan based on user input
- `GET /api/health` - Health check endpoint

## Input Parameters

The application accepts the following user inputs:

- **source** (string): Departure city/location
- **destination** (string): Travel destination
- **dates** (string): Travel dates in any readable format
- **budget** (number): Total budget in USD
- **travelers** (string): Number of travelers
- **interests** (string): User interests and preferences

## Technologies Used

### Backend
- **Flask**: Web framework
- **Google Generative AI**: Gemini 1.5 Flash model
- **Flask-CORS**: Cross-origin resource sharing
- **Python-dotenv**: Environment variable management

### Frontend
- **HTML5**: Structure
- **CSS3**: Styling with modern design
- **JavaScript**: Interactive functionality
- **Font Awesome**: Icons
- **Google Fonts**: Typography

## Customization

### Modifying the AI Prompt
Edit the prompt in `backend/app.py` in the `generate_travel_plan` method to customize the AI's response format or add additional information.

### Styling Changes
Modify `frontend/static/style.css` to change the appearance of the application.

### Adding Features
- Add new form fields in `frontend/templates/index.html`
- Update the JavaScript in `frontend/static/script.js` for new functionality
- Modify the Flask routes in `backend/app.py` for new API endpoints

## Troubleshooting

### Common Issues

1. **API Key Error**: Make sure your Gemini API key is correctly set in the environment variables
2. **Module Not Found**: Ensure all dependencies are installed with `pip install -r requirements.txt`
3. **Port Already in Use**: Change the port in `app.py` if port 5000 is already in use
4. **CORS Issues**: The Flask-CORS package should handle cross-origin requests automatically

### Getting Help

If you encounter issues:
1. Check the console output for error messages
2. Verify your API key is valid and has sufficient quota
3. Ensure all dependencies are properly installed
4. Check that the Flask server is running on the correct port

## Future Enhancements

Potential improvements for the application:
- User authentication and saved plans
- Integration with booking APIs
- Map visualization of itineraries
- Weather information integration
- Social sharing features
- Mobile app version
- Multi-language support

## License

This project is for educational and personal use. Please ensure you comply with Google's Gemini API terms of service when using this application.