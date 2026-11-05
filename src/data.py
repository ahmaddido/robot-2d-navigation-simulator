start_pos = (3, 3)
start_dir = "NORTH"


def command_check(comand):
    if len(comand) == 2:
        comand, distance = comand
        distance = int(distance)
    else:
        comand = comand[0]
        distance = 0
    return comand, distance