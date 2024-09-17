import keyboard
import os
import random as rand

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

key_down = False
score = 0
playground = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def random_position(playground): #generating position
    while True:
        x = rand.randint(0, 15)
        if playground[x // 4][x % 4] == 0: #checking if position is empty 
            return x

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def lose():
    global score
    print(f"Game over! Your score is {score}.")
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def random_number(): #generating random number
    return 4 if rand.random() <= 0.1 else 2

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def compile(a, score):
    new = []
    for i in a:
        if i != 0:
            new.append(i)
            if len(new) > 1 and new[-1] == new[-2]:
                new.append(new[-1] * 2)
                score += new[-1]
                new.remove(new[-2])
                new.remove(new[-2])
    while len(new) != 4:
        new.append(0)
    return new, score
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def move_up():
    global playground, score
    can_move = False
    vertical_1 = [playground[i][0] for i in range(4)]
    vertical_2 = [playground[i][1] for i in range(4)]
    vertical_3 = [playground[i][2] for i in range(4)]
    vertical_4 = [playground[i][3] for i in range(4)]
    count_1, count_2, count_3, count_4 = vertical_1.count(0), vertical_2.count(0), vertical_3.count(0), vertical_4.count(0)
    if count_1 != 4 and count_1 != 0:
        if vertical_1.index(0) != 4 - count_1:
            vertical_1, score = compile(vertical_1, score)
            for i in range(4):
                playground[i][0] = vertical_1[i]
            can_move = True
    else:
        for i in range(1, 4):
            if vertical_1[i] == vertical_1[i-1] and vertical_1[i] != 0:
                vertical_1, score = compile(vertical_1, score)
                can_move = True
    if can_move:
        refresh()
        
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def move_down():
    global playground, score
    can_move = False
    vertical_1 = [playground[i][0] for i in range(3, -1, -1)]
    vertical_2 = [playground[i][1] for i in range(3, -1, -1)]
    vertical_3 = [playground[i][2] for i in range(3, -1, -1)]
    vertical_4 = [playground[i][3] for i in range(3, -1, -1)]
    count_1, count_2, count_3, count_4 = vertical_1.count(0), vertical_2.count(0), vertical_3.count(0), vertical_4.count(0)
    if count_1 != 4 and count_1 != 0:
        if vertical_1.index(0) != 4 - count_1:
            vertical_1, score = compile(vertical_1, score)
            vertical_1 = list(reversed(vertical_1))
            for i in range(4):
                playground[i][0] = vertical_1[i]
            can_move = True
    else:
        for i in range(1, 4):
            vertical_1 = list(reversed(vertical_1))
            if vertical_1[i] == vertical_1[i-1] and vertical_1[i] != 0:
                vertical_1, score = compile(vertical_1, score)
                vertical_1 = list(reversed(vertical_1))
                can_move = True
    if can_move:
        refresh()
        
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def move_right():
    pass

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def move_left():
    pass

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def refresh():
    os.system("cls")
    random_pos = random_position(playground)
    random_num = random_number()
    playground[random_pos//4][random_pos%4] = random_num
    horizon_str_1, horizon_str_2, horizon_str_3, horizon_str_4 = " | ".join(map(str, playground[0])), " | ".join(map(str, playground[1])), " | ".join(map(str, playground[2])), " | ".join(map(str, playground[3]))
    print (f"{horizon_str_1}\n—   —   —   —\n{horizon_str_2}\n—   —   —   —\n{horizon_str_3}\n—   —   —   —\n{horizon_str_4}\n—   —   —   —")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def restart(): #do a new playground
    global playground
    os.system("cls")
    playground = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    for i in range (2):
        random_pos = random_position(playground)
        random_num = random_number()
        playground[random_pos//4][random_pos%4] = random_num

    horizon_str_1, horizon_str_2, horizon_str_3, horizon_str_4 = " | ".join(map(str, playground[0])), " | ".join(map(str, playground[1])), " | ".join(map(str, playground[2])), " | ".join(map(str, playground[3]))
    print (f"{horizon_str_1}\n—   —   —   —\n{horizon_str_2}\n—   —   —   —\n{horizon_str_3}\n—   —   —   —\n{horizon_str_4}\n—   —   —   —")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def key_is_down(key_name): #
    if key_name == "r":
        restart()
    if key_name == "up" or key_name == "w":
        move_up()
    if key_name == "down" or key_name == "s":
        move_down()
    if key_name == "right" or key_name == "d":
        move_right()
    if key_name == "left" or key_name == "a":
        move_left()
    if key_name == "esc":
        exit()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

restart() #start of program

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

keyboard.hook(on_key_event) #wait for the button to be pressed
keyboard.wait('esc')