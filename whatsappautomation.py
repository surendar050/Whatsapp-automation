
# This script automates sending messages and images on WhatsApp using pywhatkit and pyautogui.
# Make sure to install the required libraries using pip:
# pip install pywhatkit pyautogui
# pip install pywhatkit pyautogui"""
""" If it is not working, try using the following command:
 pip install pywhatkit --upgrade
 pip install pyautogui --upgrade  
         or
 use virtual environment to avoid conflicts with other packages."""
import pywhatkit
import time
import pyautogui

# Step 1: Send image with caption
number= ["+91XXXXXXXXXX","+91xxxxxxxxx", "+91xxxxxxxxxxx"]  
message='''this is a automated message.'''
pywhatkit.sendwhatmsg(number, message)
pywhatkit.sendwhats_image(number, "/path/image.jpg", "Image caption") # to send images

# Step 2: Wait for it to finish, then send a message
time.sleep(20)  
pyautogui.hotkey('ctrl', 'enter')  # Send the image
pyautogui.hotkey('ctrl', 'w')  # Close the current  tab
time.sleep(5)  # Wait for the tab to close
pyautogui.FAILSAFE = True # for safety, to stop the script by moving the mouse to a corner
