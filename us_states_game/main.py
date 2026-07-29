import turtle
import pandas

screen = turtle.Screen()
screen.title("Name the States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
correct_guess = []

while len(correct_guess) < 50:
    answer = screen.textinput(title=f"{len(correct_guess)}/50 States Correct",
                              prompt="What's another state's name?").title()
    if answer == "Exit":
        missing_states = [state for state in all_states if state not in correct_guess]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in all_states:
        correct_guess.append(answer)
        timm = turtle.Turtle()
        timm.hideturtle()
        timm.penup()
        state_data = data[data.state == answer]
        timm.goto(state_data.x.item(), state_data.y.item())
        timm.write(answer)



