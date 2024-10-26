def greet(name):
    print(f"Hello {name}, Welcome!")

greet("Neeraj")

#reeborg world (https://reeborg.ca/reeborg.html)

# def turn_around():
#     turn_left()
#     turn_left()
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def up_down_left_right():
#     move()
#     move()
#     move()
#     move()
#     move()
#     move()
#     move()
#     move()
#     move()
#
# turn_left()
# up_down_left_right()
# turn_right()
# up_down_left_right()
# turn_right()
# up_down_left_right()
# turn_right()
# up_down_left_right()
# turn_around()

# Lec-57 Hurdle1 Game(https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json)
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# for run in range(6):
#     move()
#     jump()

# Lec-58 Hurdle3 Game
# while not at_goal():
#     if wall_in_front():
#         jump()
#     elif front_is_clear():
#         move()

# Lec-59 Hurdle4 Game
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def move_forward(func):
#     while func():
#         move()
#
# def jump():
#     turn_left()
#     move_forward(wall_on_right)
#     if not wall_on_right():
#         turn_right()
#         move()
#         turn_right()
#         move_forward(front_is_clear)
#         if wall_in_front():
#             turn_left()
#
# while not at_goal():
#     if wall_in_front():
#         jump()
#     elif front_is_clear():
#         move()