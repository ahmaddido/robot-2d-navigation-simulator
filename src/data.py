
start_position = (3, 3)
obstacles = [(3, 5), (5, 3), (1, 2)]
boundary = (6, 6)
new_pos = (0, 0)


dist, request = input(f"How should the robot move?").split()
input = (int(dist), str(request))







# print(input)
# if input == True:
#     direction = input[1]
#     if direction == "north":
#         new_pos = (int(start_position[0]), int(start_position[1] + input[0]))
#         start_position = new_pos
        
#     elif direction == "south":
#         new_pos = (int(start_position[0]), int(start_position[1] - input[0]))
#         start_position = new_pos
#     elif direction == "east":
#         new_pos = (int(start_position[0] + input[0]), int(start_position[1]))
#         start_position = new_pos
#     elif direction == "west":
#         new_pos = (int(start_position[0] - input[0]), int(start_position[1]))
#         start_position = new_pos
#     else:
#         print("no valid direction")
        
        
# print(new_pos)
