# import turtle
# import pandas
#
# screen = turtle.Screen()
# screen.title("U.S. States Game")
# image = "blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)
#
# data = pandas.read_csv("50_states.csv")
# all_states = data.state.to_list()
# guessed_states = []
#
# while len(guessed_states) < 50:
#     answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
#                                     prompt="What's another state's name?").title()
#     if answer_state == "Exit":
#         missing_states = []
#         for state in all_states:
#             if state not in guessed_states:
#                 missing_states.append(state)
#         new_data = pandas.DataFrame(missing_states)
#         new_data.to_csv("states_to_learn.csv")
#         break
#     if answer_state in all_states:
#         guessed_states.append(answer_state)
#         t = turtle.Turtle()
#         t.hideturtle()
#         t.penup()
#         state_data = data[data.state == answer_state]
#         t.goto(state_data.x.item(), state_data.y.item())
#         t.write(answer_state)



import turtle
import pandas as pd
screen=turtle.Screen()
screen.title("US game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data=pd.read_csv("50_states.csv")
all=data.state.to_list()
g=[]
while(len(g)<50):
    an=screen.textinput(title=f"{len(g)}/50",prompt="whts another state").title()
    print(an)
    if an=="Exit":
        m=[state for state in all if state not in g ]
        # for state in all:
        #     if state not in g:
        #         m.append(state)
        n=pd.DataFrame(m)
        n.to_csv("miss.csv")
        break
    if an in all:
        g.append(an)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        s=data[data.state==an]
        t.goto(s.x.item(),s.y.item())
        t.write(an)




screen.exitonclick()