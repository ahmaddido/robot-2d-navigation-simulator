from data import start_pos, start_dir, command_check, check_bounds, check_obst

now_pos = start_pos
now_dir = start_dir
total_mov = []
total_blocked = []

while True:
    comand = input("Hi it is me your Robot, what should I do?").split()
    comand, distance = command_check(comand)
    
    if comand is None:
        continue

    match comand:
        case "DONE":
            print(f"Total Movments: {len(total_mov)}")
            print(f"Blocked Movments: {len(total_blocked)}")
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
                                    if check_obst(nxt_pos):
                                        now_pos = nxt_pos
                                        total_mov.append(tuple(now_pos))
                                        continue
                                    else:
                                        print("OBSTACLE !!!")
                                        total_blocked.append(nxt_pos)
                                        break
                                else:
                                    print("OUT OF BOUN")
                                    break
                            
                        case "EAST":
                            
                            for step in range(distance):
                                x, y = now_pos
                                nxt_pos = (x + 1, y)
                                if check_bounds(nxt_pos):
                                    if check_obst(nxt_pos):
                                        now_pos = nxt_pos
                                        total_mov.append(tuple(now_pos))
                                        continue
                                    else:
                                        print("OBSTACLE !!!")
                                        break
                                else:
                                    print("OUT OF BOUN")
                                    break
                            

                        case "SOUTH":
                            
                            for step in range(distance):
                                x, y = now_pos
                                nxt_pos = (x, y - 1)
                                if check_bounds(nxt_pos):
                                    if check_obst(nxt_pos):
                                        now_pos = nxt_pos
                                        total_mov.append(tuple(now_pos))
                                        continue
                                    else:
                                        print("OBSTACLE !!!")
                                        break
                                else:
                                    print("OUT OF BOUN")
                                    break
                            
                        case "WEST":
                          
                            for step in range(distance):
                                x, y = now_pos
                                nxt_pos = (x - 1, y)
                                if check_bounds(nxt_pos):
                                    if check_obst(nxt_pos):
                                        now_pos = nxt_pos
                                        total_mov.append(tuple(now_pos))
                                        continue
                                    else:
                                        print("OBSTACLE !!!")
                                        break
                                else:
                                    print("OUT OF BOUN")
                                    break
                            
                


        case _:
            print("I don't understand that command")
