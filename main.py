import turtle
import pandas
screen = turtle.Screen()
screen.setup(750, 510)
screen.bgpic("blank_states_img.gif")
correct_ans_count = 0
data = pandas.read_csv("50_states.csv")
correct_states = False
guessed_states = []
to_learn = {"states to learn": [],
            }
while not correct_states:
    user_answer = screen.textinput(title=f"{correct_ans_count}/{len(data.state)} States Correct",
                               prompt="what state's do you know?").capitalize()

    for all_states in data["state"]:
        if all_states == user_answer:
            states = data[data["state"] == user_answer]
            x_coordinate =  states.x
            y_coordinate =  states.y
            extracted_x_cor = x_coordinate.item()
            extracted_y_cor = y_coordinate.item()
            turtle.hideturtle()
            turtle.penup()
            turtle.goto(extracted_x_cor, extracted_y_cor)
            turtle.write(all_states)
            correct_ans_count += 1
            guessed_states.append(all_states)
    if user_answer == "Exit":
        break

for places in data["state"]:
    if places not in guessed_states:
        to_learn["states to learn"].append(places)
unguessed_states = pandas.DataFrame(to_learn)
unguessed_states.to_csv("states_to_learn.csv")




