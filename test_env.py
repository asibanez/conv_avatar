#!/usr/bin/env python3
"""
Simple test script to verify .env file loading
"""

import os
from dotenv import load_dotenv

def test_env_loading():
    print("🔍 Testing .env file loading...")
    
    # Check if .env file exists
    if os.path.exists('.env'):
        print("✅ .env file found")
    else:
        print("❌ .env file not found")
        print("   Create one by copying env.example to .env")
        return False
    
    # Load environment variables
    load_dotenv()
    
    # Check API key
    api_key = os.getenv('DID_API_KEY')
    if api_key:
        print(f"✅ DID_API_KEY loaded: {api_key[:10]}...")
        print(f"   Key length: {len(api_key)} characters")
        return True
    else:
        print("❌ DID_API_KEY not found in .env file")
        print("   Make sure your .env file contains: DID_API_KEY=your_actual_key_here")
        return False

if __name__ == '__main__':
    success = test_env_loading()
    if success:
        print("\n🎉 Environment setup looks good!")
        print("   You can now run: python app.py")
    else:
        print("\n⚠️  Please fix the environment setup before running the app")
