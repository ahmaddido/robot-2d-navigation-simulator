from data import start_pos, start_dir, command_check

now_pos = start_pos
now_dir = start_dir

while True:
    comand = input("Hi it is me your Robot, what should I do?").split()
    comand, distance = command_check(comand)





    match comand:
        case "DONE":
            print("Simulation ended")
            break

        case "STATUS":
            print(f"position: {now_pos} direction: {now_dir}")

        case "RIGHT":
            match now_dir:
                case "NORTH":
                    now_dir = "EAST"
                case "EAST":
                    now_dir = "SOUTH"
                case "SOUTH":
                    now_dir = "WEST"
                case "WEST":
                    now_dir = "NORTH"

        case "LEFT":
            match now_dir:
                case "NORTH":
                    now_dir = "WEST"
                case "WEST":
                    now_dir = "SOUTH"
                case "SOUTH":
                    now_dir = "EAST"
                case "EAST":
                    now_dir = "NORTH"

        case "FORWARD":
            match distance > 0:
                case True:
                    x, y = now_pos
                    match now_dir:
                        case "NORTH":
                            now_pos = (x, y + distance)
                        case "EAST":
                            now_pos = (x + distance, y)
                        case "SOUTH":
                            now_pos = (x, y - distance)
                        case "WEST":
                            now_pos = (x - distance, y)
                case False:
                    print("YOU MUST ENTER A DISTANCE")


        case _:
            print("I don't understand that command")

