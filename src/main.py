from data import start_pos, start_dir, command_check, check_bounds

now_pos = start_pos
now_dir = start_dir

while True:
    comand = input("Hi it is me your Robot, what should I do?").split()
    # if len(comand) == 0:
    #     print("You must enter a command")
    #     continue
    comand, distance = command_check(comand)
    
    if comand is None:
        continue

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
                    
                    match now_dir:
                        
                        case "NORTH":
                            for step in range(distance):
                                x, y = now_pos
                                nxt_pos = (x, y + 1)
                                if check_bounds(nxt_pos):
                                    now_pos = nxt_pos
                                    continue
                                else:
                                    print("OUT OF BOUN")
                            
                        case "EAST":
                            for step in range(distance):
                                x, y = now_pos
                                nxt_pos = (x + 1, y)
                                if check_bounds(nxt_pos):
                                    now_pos = nxt_pos
                                    continue
                                else:
                                    print("OUT OF BOUN")
                            #now_pos = (x + distance, y)

                        case "SOUTH":
                            for step in range(distance):
                                x, y = now_pos
                                nxt_pos = (x, y - 1)
                                if check_bounds(nxt_pos):
                                    now_pos = nxt_pos
                                    continue
                                else:
                                    print("OUT OF BOUN")
                            #now_pos = (x, y - distance)
                        case "WEST":
                            for step in range(distance):
                                x, y = now_pos
                                nxt_pos = (x - 1, y)
                                if check_bounds(nxt_pos):
                                    now_pos = nxt_pos
                                    continue
                                else:
                                    print("OUT OF BOUN")
                            #now_pos = (x - distance, y)
                


        case _:
            print("I don't understand that command")

