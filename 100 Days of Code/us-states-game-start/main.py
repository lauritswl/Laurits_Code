import turtle
import pandas as pd
from data_bank import GuessChecker


state_name = "Ohio"


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
GAME_IS_ON = True

guess_checker = GuessChecker()


while GAME_IS_ON:
    guess_checker.ask_for_a_guess()
    guess_checker.check_if_guess_is_wrong()
    if not guess_checker.guess_is_wrong:
        guess_checker.print_state()





turtle.mainloop()
