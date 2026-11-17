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

    # if len(comand) == 2:
    #     try:
    #         comand, distance = comand
    #         distance = int(distance)
    #     except ValueError:
    #         print("You must enter a a valid number for distance")
    #         distance = 0

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

        if distance < 0:
            print("Distance must be greater than zero")
            return None, None
    else:
        distance = 0

    # elif len(comand) > 2:
    #         #comand = comand[0]
    #         distance = 0
    #         #print("ERROR in command")
    # else:
    #     comand = comand[0]
    #     distance = 0

    return command, distance

def check_bounds(pos):
    x, y = pos
    if x in range(0, 7) and y in range(0, 7):
        return True






