from data import start_pos, start_dir

while True:
    comand = input("Hi it is me your Robot, what should I do?")
    
    if comand == "DONE":
        print("Simulation ended")
        break

    elif comand == "STATUS":
        print(f"position: {start_pos} direction: {start_dir}")
    
    elif comand == "RIGHT" and start_dir == "NORTH":
            start_dir = "EAST"
    elif comand == "RIGHT" and start_dir == "EAST":
        start_dir = "SOUTH"
    elif comand == "RIGHT" and start_dir == "SOUTH":
        start_dir = "WEST"
    elif comand == "RIGHT" and start_dir == "WEST":
        start_dir = "NORTH"
    elif comand == "LEFT" and start_dir == "NORTH":
        start_dir = "WEST"
    elif comand == "LEFT" and start_dir == "WEST":
        start_dir = "SOUTH"
    elif comand == "LEFT" and start_dir == "SOUTH":
        start_dir = "EAST"
    elif comand == "LEFT" and start_dir == "EAST":
        start_dir = "NORTH"
    else:
        print("I don't understand that command")
        