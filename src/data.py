start_pos = (3, 3)
start_dir = "NORTH"



def command_check(comand):

    req_args = {
        "DONE": 1,
        "STATUS": 1,
        "RIGHT": 1,
        "LEFT": 1,
        "FORWARD": 2
        }

    if len(comand) == 0:
        print("You must enter a command")
        return None, None

    command = comand[0].upper()

    if command not in req_args:
        print("Unknown command")
        return None, None
    
    if len(comand) != req_args[command]:
        print("INVALID NUMBER OF ARGUMENTS")
        return None, None

    if command == "FORWARD":
        try:
            distance = int(comand[1])
        except ValueError:
            print("Distance must be a valid number")
            return None, None

        if distance < 1:
            print("Distance must be greater than zero")
            return None, None
    else:
        distance = 0

    return command, distance

def check_bounds(pos):
    x, y = pos
    if x in range(0, 7) and y in range(0, 7):
        return True
    
        

def check_obst(pos):
    obstacles = [(3, 5), (5, 3), (1,2)]
    if pos not in obstacles:
        return True








