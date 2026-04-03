# main.py
from robot_helpers import turn_right

# Reeborg's World requires handling edge cases at the very start
while front_is_clear():
    move()
turn_left()

# The main Right Wall Follower algorithm
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()