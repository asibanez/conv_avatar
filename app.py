from flask import Flask, render_template, request, jsonify
import os, time, base64, requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Get API key from environment variable
API_KEY = os.getenv('DID_API_KEY')
if not API_KEY:
    raise ValueError("DID_API_KEY not found in environment variables. Please set it in your .env file")

# Create auth header
auth_header = "Basic " + base64.b64encode(API_KEY.encode()).decode()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def generate_video():
    try:
        data = request.get_json()
        text = data.get('text', '').strip()
        
        if not text:
            return jsonify({'error': 'Text is required'}), 400
        
        # Create clip payload
        create_payload = {
            "script": {
                "type": "text",
                "input": text
            },
            "presenter_id": "amy-Aq6OmGZnMt",
            "driver_id": "Vcq0R4a8F0"
        }
        
        # Create clip
        r = requests.post(
            "https://api.d-id.com/clips",
            headers={"Authorization": auth_header, "Accept":"application/json", "Content-Type":"application/json"},
            json=create_payload,
        )
        r.raise_for_status()
        clip_id = r.json()["id"]
        
        # Poll until ready
        max_attempts = 60  # 2 minutes max
        attempts = 0
        
        while attempts < max_attempts:
            s = requests.get(f"https://api.d-id.com/clips/{clip_id}",
                           headers={"Authorization": auth_header, "Accept":"application/json"})
            s.raise_for_status()
            data = s.json()
            
            if data.get("status") == "done":
                return jsonify({
                    'success': True,
                    'video_url': data["result_url"],
                    'clip_id': clip_id
                })
            elif data.get("status") in {"error", "failed"}:
                return jsonify({
                    'success': False,
                    'error': f"Clip failed: {data}"
                }), 400
            
            time.sleep(2)
            attempts += 1
        
        return jsonify({
            'success': False,
            'error': 'Video generation timed out'
        }), 408
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    print("🎬 D-ID Video Generator starting...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print(f"✅ API key loaded: {API_KEY[:20]}...")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
