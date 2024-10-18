# WhatsApp Video Sender

This Python script uses `pyautogui` to automate sending a video file to a WhatsApp contact via WhatsApp Web.It is to be used as a backup if V1 does not work

## Prerequisites

- Python 3.x
- `pyautogui` library
- A web browser (e.g., Google Chrome)
- Logged into WhatsApp Web

## Installation

1. Clone this repository:

   `git clone <repository_url>`

   `cd <repository_folder>`

2. Install `pyautogui`:

   `pip install pyautogui`

## Usage

1. Open WhatsApp Web and log in.

2. Edit the script to set the contact name and video path:

   `contact_name = "Contact Name"  # Replace with the name of the contact or group`  
   `video_path = r"C:\path\to\your\video.mp4"  # Replace with the full path to your video`

3. Adjust the click coordinates in the script as needed.

4. Run the script:

   `python send_video.py`

## Important Notes

- **Coordinates**: Adjust the `x` and `y` coordinates based on your screen.
- **Delays**: Modify `time.sleep()` values to ensure proper loading.



