# How to Get Your Gemini API Key

## Step 1: Get Your API Key

1. **Visit Google AI Studio**: Go to [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

2. **Sign in** with your Google account

3. **Create API Key**: Click on "Create API Key" button

4. **Copy the key**: Copy the generated API key (it will look something like: `AIzaSyC...`)

## Step 2: Set Up Your Environment

### Option 1: Create .env file (Recommended)
1. Copy the `.env.example` file to `.env`:
   ```bash
   copy backend\.env.example backend\.env
   ```

2. Edit the `.env` file and replace `your_gemini_api_key_here` with your actual API key:
   ```
   GEMINI_API_KEY=AIzaSyC_your_actual_api_key_here
   ```

### Option 2: Set Environment Variable (Windows)
Open Command Prompt or PowerShell and run:
```cmd
set GEMINI_API_KEY=AIzaSyC_your_actual_api_key_here
```

### Option 3: Set in PowerShell
```powershell
$env:GEMINI_API_KEY="AIzaSyC_your_actual_api_key_here"
```

## Step 3: Install Dependencies

Run this command in the project directory:
```bash
cd backend
pip install -r requirements.txt
```

## Step 4: Run the Application

```bash
python backend/app.py
```

Then open your browser and go to: http://localhost:5000

## Important Notes

- **Keep your API key secret** - never share it publicly
- **Free tier limits**: Gemini API has usage limits on the free tier
- **Rate limits**: Don't make too many requests too quickly

## Troubleshooting

If you get an error about the API key:
1. Make sure the key is correctly set
2. Check that you have internet connection
3. Verify the key is valid in Google AI Studio
4. Make sure you haven't exceeded your API quota