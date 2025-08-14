# 🎬 D-ID Text to Video Generator (Python Flask)

A modern, responsive web application built with Python Flask that transforms text input into talking avatar videos using D-ID's AI-powered video generation API. Generate professional-looking videos with realistic avatars speaking your text in real-time.

## ✨ Features

- **Python Backend**: Built with Flask for robust server-side processing
- **Real-time Video Generation**: Convert text to video in minutes
- **Background Processing**: Asynchronous video generation with progress tracking
- **Multiple Voice Options**: Choose from various Microsoft Neural voices (English, Spanish, French)
- **Avatar Selection**: Pick from different presenter avatars
- **Progress Tracking**: Real-time progress updates during video generation
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Auto-play Videos**: Generated videos play automatically in the browser
- **Download Support**: Save generated videos to your device
- **Character Counter**: Track text length with visual feedback
- **Keyboard Shortcuts**: Use Ctrl+Enter to generate videos quickly
- **RESTful API**: Clean API endpoints for video generation and status checking

## 🚀 Quick Start

### 1. Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- D-ID API key

### 2. Get Your D-ID API Key

1. Visit [D-ID Studio](https://studio.d-id.com/)
2. Create an account or sign in
3. Navigate to your API settings
4. Copy your API key

### 3. Install Dependencies

```bash
# Clone or download the project
cd d-id-video-generator

# Install Python dependencies
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```bash
# Copy the example file
cp env.example .env

# Edit the .env file and add your D-ID API key
nano .env  # or use your preferred editor
```

Add your D-ID API key to the `.env` file:
```bash
DID_API_KEY=your_actual_did_api_key_here
```

**Important**: Make sure there are no spaces around the `=` sign and no quotes around the API key.

### 4.1. Test Environment Setup

Test that your `.env` file is configured correctly:

```bash
python test_env.py
```

This will verify that your environment variables are loaded properly.

### 5. Run the Application

```bash
# Start the Flask application
python app.py
```

The app will start on `http://localhost:5000`

### 6. Use the Application

1. Open your browser and go to `http://localhost:5000`
2. If you set your API key in the `.env` file, you can leave the API Key field empty
3. Otherwise, enter your D-ID API key in the API Key field
4. Click "🎥 Generate Video" to start creating videos

## 🎯 Usage

### Text Input
- **Maximum Length**: 500 characters
- **Supported Languages**: English, Spanish, French (depending on voice selection)
- **Tips**: Use clear, well-punctuated text for best results

### Voice Selection
- **Jenny (US English)**: Clear, professional female voice
- **Guy (US English)**: Warm, engaging male voice
- **Ryan (British English)**: Sophisticated British accent
- **Sonia (British English)**: Elegant British female voice
- **Elvira (Spanish)**: Natural Spanish female voice
- **Denise (French)**: Fluent French female voice

### Avatar Selection
- **Amy**: Professional female presenter
- **John**: Business-oriented male presenter
- **Sarah**: Friendly female presenter
- **Mike**: Approachable male presenter

### Keyboard Shortcuts
- **Ctrl/Cmd + Enter**: Generate video
- **Escape**: Close dialogs

## 🔧 Technical Details

### Architecture
- **Backend**: Python Flask web framework
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **API Integration**: D-ID Talks API with RESTful endpoints
- **Background Processing**: Threading for non-blocking video generation
- **Status Tracking**: Real-time progress updates via polling

### API Endpoints
- `GET /` - Main application page
- `POST /api/generate` - Start video generation
- `GET /api/status/<task_id>` - Check video generation status
- `GET /api/voices` - Get available voices
- `GET /api/presenters` - Get available presenters
- `GET /health` - Health check endpoint

### Video Generation Process
1. **Queue**: Video generation request is queued
2. **Processing**: Background worker processes the request
3. **D-ID API**: Calls D-ID API to create video
4. **Polling**: Monitors generation progress
5. **Completion**: Returns video URL when ready

### Security Features
- API key validation on server-side
- Input sanitization and validation
- Rate limiting considerations
- No sensitive data logging

## 📁 File Structure

```
d-id-video-generator/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # HTML template with embedded CSS/JS
├── requirements.txt       # Python dependencies
├── env.example           # Example environment configuration
├── .env                  # Your environment variables (create this)
└── README.md             # This documentation
```

## 🐛 Troubleshooting

### Common Issues

1. **"ModuleNotFoundError: No module named 'flask'"**
   ```bash
   pip install -r requirements.txt
   ```

2. **"Port already in use"**
   ```bash
   # Kill process using port 5000
   lsof -ti:5000 | xargs kill -9
   # Or change port in app.py
   ```

3. **"Unauthorized" Error**
   - Check that your `.env` file exists and contains `DID_API_KEY=your_key`
   - Ensure no spaces around `=` and no quotes around the key
   - Verify your D-ID API key is valid and has sufficient credits
   - Run `python test_env.py` to verify environment setup

4. **"API key not found" Error**
   - Make sure you have a `.env` file in the project root
   - Check that the file contains `DID_API_KEY=your_actual_key`
   - Restart the Flask app after creating/modifying the `.env` file

4. **Video Generation Fails**
   - Verify your text is within the 500 character limit
   - Check your internet connection
   - Ensure your D-ID account has available credits

5. **Slow Generation**
   - Video generation typically takes 1-3 minutes
   - Longer text may take more time
   - Check D-ID service status if unusually slow

### Error Messages

- **"Video generation timed out"**: Generation took longer than 5 minutes
- **"HTTP 401"**: Invalid or expired API key
- **"HTTP 429"**: Rate limit exceeded (too many requests)
- **"HTTP 500"**: D-ID service error (try again later)

## 🚀 Production Deployment

### Environment Variables
```bash
export FLASK_ENV=production
export FLASK_DEBUG=0
export SECRET_KEY=your-secret-key-here
```

### Production Server
```bash
# Using Gunicorn (recommended)
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Using uWSGI
pip install uwsgi
uwsgi --http :5000 --module app:app
```

### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 💰 Pricing & Limits

- **D-ID Credits**: Each video generation consumes credits from your D-ID account
- **Free Tier**: Limited credits available for new users
- **Paid Plans**: Various pricing tiers for higher usage
- **Rate Limits**: API calls are subject to rate limiting

## 🔗 Resources

- [D-ID Official Website](https://www.d-id.com/)
- [D-ID Studio](https://studio.d-id.com/)
- [D-ID API Documentation](https://docs.d-id.com/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python Documentation](https://docs.python.org/)

## 📝 License

This project is open source and available under the MIT License. Feel free to modify and distribute as needed.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

### Development Setup
```bash
# Clone the repository
git clone <repository-url>
cd d-id-video-generator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run in development mode
python app.py
```

## 📞 Support

For technical issues with this application:
- Check the troubleshooting section above
- Review D-ID's official documentation
- Contact D-ID support for API-related issues
- Open an issue on the project repository

---

**Note**: This application requires an active D-ID account and API key to function. Video generation consumes credits from your D-ID account.
