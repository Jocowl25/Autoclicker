from pynput.mouse import Button, Controller, Listener
from pynput import keyboard
import time

#set up esc function
esc=False
def on_press(key):
    global esc
    if key == keyboard.Key.esc:
        esc=True

#set up autoclicker settings
type=input("Would you like to stop clicking after a certain number of seconds? (y/n) ")
if(not type.lower()=="y" and not type.lower()=="n"):
    raise("Invalid response recieved. This is literally the first part of the code so I'm not looping it. Just run it again.")

if(type.lower()=="n"):
    total=int(input("Number of times to click: "))
else:
    total=int(input("Length of time to click for (seconds): "))
delay=int(input("Delay between each click (seconds): "))

#wait for mouse click to begin clicking
print("Click to start...")
with Listener(on_click=lambda a,b,c,d: False) as listener:
    listener.join()
mouse = Controller()

#set up esc key to leave autoclicker
keylistener = keyboard.Listener(
    on_press=on_press)
keylistener.start()

print("Starting! Press esc to exit.")

#the autoclicker itself
if(type.lower()=="n"):
    #clicks x times
    for i in range(total):
        if(esc):
            print("Program escaped manually.")
            break
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(delay)
else:
    #clicks for a set amount of time
    timestart=time.time()
    timenow=time.time()
    while timenow-timestart<total:
        timenow=time.time()
        if(esc):
            print("Program escaped manually.")
            break
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(delay)

if(not esc):
    print("Clicking complete.")