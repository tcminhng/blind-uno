#!/usr/bin/env python3
import RPi.GPIO as GPIO
import subprocess
import base64
import sys
import os
import time
from openai import OpenAI

# --- Configuration ---
CAPTURE_BTN_PIN = 11  
MOTOR_PIN       = 13  

client = OpenAI(api_key="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")
MODEL = "gpt-5-nano-2025-08-07"
IMAGE_PATH = "/home/pi/captured_image.jpg"

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    # Motor OFF (Low)
    GPIO.setup(MOTOR_PIN, GPIO.OUT)
    GPIO.output(MOTOR_PIN, GPIO.LOW) 
    # Button: Normal=1, Pressed=0
    GPIO.setup(CAPTURE_BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    print("System ready. Waiting for button...")

def haptic_feedback(duration):
    GPIO.output(MOTOR_PIN, GPIO.HIGH) # ON
    time.sleep(duration)
    GPIO.output(MOTOR_PIN, GPIO.LOW)  # OFF

def speak(text):
    """Voice output for the earphones"""
    print(f"VOICE: {text}")
    # This command sends the text to your Bluetooth audio
    os.system(f'espeak "{text}" 2>/dev/null')

def extract_text(resp):
    text = getattr(resp, "output_text", None)
    if text:
        return text.strip()
    try:
        for item in getattr(resp, "output", []):
            for part in getattr(item, "content", []):
                if getattr(part, "type", None) in ("output_text", "text") and getattr(part, "text", None):
                    return part.text.strip()
    except Exception:
        pass
    return str(resp)

def run_uno_scan():
    print("\n--- Scan Triggered! ---")
    haptic_feedback(0.2) 
    try:
        # Capture image
        subprocess.run(["fswebcam", "-r", "640x480", "-S", "2", "--no-banner", IMAGE_PATH], check=True)
        
        # Encode
        with open(IMAGE_PATH, "rb") as f:
            data_url = f"data:image/jpeg;base64,{base64.b64encode(f.read()).decode('utf-8')}"
        
        # The Prompt
        prompt = "Identify the UNO card color and number. Reply with just the color and number, e.g., 'Red 8'."
        
        resp = client.responses.create(
            model=MODEL,
            reasoning={"effort": "low"},
            input=[{"role": "user", "content": [
                {"type": "input_text", "text": prompt},
                {"type": "input_image", "image_url": data_url}
            ]}]
        )
        
        result = extract_text(resp)
        print(f"RESULT: {result}")
        
        # --- NEW: Speak the result out loud ---
        speak(result)
        
        # Success signal: Two quick buzzes
        for _ in range(2):
            haptic_feedback(0.1)
            time.sleep(0.1)
            
    except Exception as e:
        print(f"Error: {e}")
        speak("Error scanning card")

def main():
    setup()
    while True:
        if GPIO.input(CAPTURE_BTN_PIN) == GPIO.LOW:
            run_uno_scan()
            while GPIO.input(CAPTURE_BTN_PIN) == GPIO.LOW:
                time.sleep(0.1)
        time.sleep(0.1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
