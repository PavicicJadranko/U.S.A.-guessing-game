from turtle import Turtle, Screen
import pandas as pd

data = pd.read_csv("50_states.csv")
state = Turtle()
t_score = Turtle()
t_score.ht()
t_score.penup()
state.ht()
state.penup()
screen = Screen()
screen.bgpic("blank_states_img.gif")
game_on = True
state_data = data.state.to_list()
state_x = data.x.to_list()
state_y = data.y.to_list()
score = 0

while game_on:

    user_input = screen.textinput("U.S. States Game", prompt="Try to guess a state of the USA? If you are done tipe 'off'.")

    if user_input in state_data:
        t_score.clear()
        index = state_data.index(user_input)
        state.goto(state_x[index], state_y[index])
        state.write(user_input)
        score += 1
        t_score.goto(150, 270)
        t_score.write(f"You know {score} of 50 states", font=("Ariel", 15, "normal"))
        state_data.remove(user_input)

    if user_input == "off":
        ix = 0
        for states in state_data:
            state.goto(state_x[ix], state_y[ix])
            state.write(states)
            ix += 1
        game_on = False


screen.exitonclick()
