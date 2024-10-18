import pyautogui
import time
import os

# Change the variables
contact_name = "Contact Name"  
video_path = r"D:\Video-sending-bot-V2\video.mp4"  

# Open the browser (might vary depending on the setup)
os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")  
time.sleep(3)  # Wait for the browser to open-add more for slow device

pyautogui.typewrite("https://web.whatsapp.com")
pyautogui.press("enter")
time.sleep(10)  # Wait for WhatsApp Web to load-add more for slow device

# Click on the search bar and type the contact name
pyautogui.click(x=300, y=200)  # Adjust the x and y values based on your screen
time.sleep(1)
pyautogui.typewrite(contact_name)
time.sleep(2)  # Wait for the contact to appear-suggested to remove all other contacts

# Press Enter to open the chat
pyautogui.press("enter")
time.sleep(2)  # Wait for the chat to open

# Click the attachment button
pyautogui.click(x=700, y=700)  # Adjust the coordinates 
time.sleep(1)

# Click the "Photos & Videos" option
pyautogui.click(x=800, y=600)  # Adjust coordinates 
time.sleep(2)

# Type the path to the video
pyautogui.typewrite(video_path)
pyautogui.press("enter")
time.sleep(2)  # Wait for the video to upload

# Send the video
pyautogui.press("enter")
