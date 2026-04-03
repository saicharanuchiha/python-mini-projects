from robot_helpers import turn_right


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
        if wall_in_front():
            jump()
    else:
        jump()