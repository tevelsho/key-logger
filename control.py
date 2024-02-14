# Library for controlling keyboard input streams
from pynput.keyboard import Controller 

# Left to right, top to bottom
def controlMouse():
    mouse = Controller()
    mouse.position = (10,20) # Start position on the display

def controlKeyboard():
    keyboard = Controller()
    keyboard.type("Hello World")

controlKeyboard() # Call function based on intended use