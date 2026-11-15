start_pos = (3, 3)
start_dir = "NORTH"

args = {
    "DONE": 1,
    "STATUS": 1,
    "RIGHT": 1,
    "LEFT": 1,
    "FORWARD": 2
}


def command_check(comand):
    if len(comand) == 2:
        try:
            comand, distance = comand
            distance = int(distance)
        except ValueError:
            print("You must enter a a valid number for distance")
            distance = 0

    elif len(comand) == 0:
        distance = 0

    elif len(comand) > 2:
            #comand = comand[0]
            distance = 0
            #print("ERROR in command")
    else:
        comand = comand[0]
        distance = 0

    return comand, distance

