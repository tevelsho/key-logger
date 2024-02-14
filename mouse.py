from pynput.mouse import Listener


def writeToFile(x,y):
    print("Position of current mouse [0]".format((x,y)))
    
with Listener(on_move=writeToFile) as l:
    l.join() # Join the keystrokes together