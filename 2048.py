import keyboard
import random as rand

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

key_down = False

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def random_position(playground): #generating position
    while True:
        x = rand.randint(0, 15)
        if playground[x // 4][x % 4] == 0: #checking if position is empty 
            return x

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def random_number(): #generating random number
    return 4 if rand.random() < 0.1 else 2

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def restart(): #do a new playground
    playground = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    for i in range (2):
        random_pos = random_position(playground)
        random_num = random_number()
        playground[random_pos//4][random_pos%4] = random_num

    horizon_1, horizon_2, horizon_3, horizon_4 = " | ".join(map(str, playground[0])), " | ".join(map(str, playground[1])), " | ".join(map(str, playground[2])), " | ".join(map(str, playground[3]))
    print (f"{horizon_1}\n—   —   —   —\n{horizon_2}\n—   —   —   —\n{horizon_3}\n—   —   —   —\n{horizon_4}\n—   —   —   —")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def key_is_down(key_name): #
    if key_name == "r":
        restart()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def on_key_event(event): #do a specific control (while one button is pressed, u can't press any button)
    global key_down, key_name
    if event.event_type == keyboard.KEY_UP and key_name == event.name:
        key_down = False
    if key_down:
        return
    if event.event_type == keyboard.KEY_DOWN:
        key_down = True
        key_name = event.name
        key_is_down(key_name)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

restart() #start of program

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

keyboard.hook(on_key_event) #wait for the button to be pressed
keyboard.wait('esc')
