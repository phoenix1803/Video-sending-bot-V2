import pyautogui
import time
import os

# Change variable
contact_name = "Contact Name"  
video_path = r"D:\Video-sending-bot-V2\video.mp4"  

os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")  
time.sleep(3)  # -add more for slow device

pyautogui.typewrite("https://web.whatsapp.com")
pyautogui.press("enter")
time.sleep(10)  # add more for slow device


pyautogui.click(x=300, y=200)  # adjust x and y acc ontoour screen
time.sleep(1)
pyautogui.typewrite(contact_name)
time.sleep(2)  # suggested to remove all other contacts

pyautogui.press("enter")
time.sleep(2)  

pyautogui.click(x=700, y=700)  # Adjust coord
time.sleep(1)

pyautogui.click(x=800, y=600)  # Adjust coord
time.sleep(2)

# Type the path to the video
pyautogui.typewrite(video_path)
pyautogui.press("enter")
time.sleep(15)  

# Send 
pyautogui.press("enter")
