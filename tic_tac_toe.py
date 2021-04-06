"""
    Written by: Caroline Prevoo

    Date start: 5 april 2021

    Goal      : Tic Tac Toe game
"""

from flask import Flask, render_template, request, redirect, url_for

class TicTacToe:

    def __init__(self):
        self.fields = ["", "", "", "", "", "", "", "", ""]
        self.click_count = 0
        self.result = ""

    def reset_game(self):
        self.fields = ["", "", "", "", "", "", "", "", ""]
        self.click_count = 0
        self.result = ""

    def check_winner(self):
        # check horizontal
        if self.fields[0] == self.fields[1] == self.fields[2]:
            return self.fields[0]
        elif self.fields[3] == self.fields[4] == self.fields[5]:
            return self.fields[3]
        elif self.fields[6] == self.fields[7] == self.fields[8]:
            return self.fields[6]
        # check vertical
        elif self.fields[0] == self.fields[3] == self.fields[6]:
            return self.fields[0]
        elif self.fields[1] == self.fields[4] == self.fields[7]:
            return self.fields[1]
        elif self.fields[2] == self.fields[5] == self.fields[8]:
            return self.fields[2]
        # check diagonal
        elif self.fields[0] == self.fields[4] == self.fields[8]:
            return self.fields[0]
        elif self.fields[2] == self.fields[4] == self.fields[6]:
            return self.fields[2]
        # no winner
        return False

    def disable_all_field_buttons(self):
        # If the game is over (winner of draw) give all buttons a value
        # so they are disabled in html.
        # Make empty field buttons " " (space)
        for n in range(9):
            if self.fields[n] == "":
                self.fields[n] = " "

    def play(self, button_pressed):
        # Reset Game
        if button_pressed == "reset":
            self.reset_game()
            return self

        # Fields buttons
        if self.click_count % 2 == 0:
            self.fields[int(button_pressed)] = "X"
        else:
            self.fields[int(button_pressed)] = "O"

        self.click_count += 1

        # Game rules
        is_winner = self.check_winner()
        if is_winner:
            self.result = f"{is_winner} IS THE WINNER"
            # Disable all field buttons
            for n in range(9):
                if self.fields[n] == "":
                    self.fields[n] = " "
        if not is_winner and self.click_count >= 9:
            self.result = "IT'S A DRAW!"

        return self



app = Flask(__name__)
game_tic_tac_toe = TicTacToe()

@app.route('/', methods=['GET', 'POST'])
@app.route('/tic_tac_toe', methods=['GET', 'POST'])
def tic_tac_toe_app():
    if request.method == 'POST':
        button_pressed = request.form['btn-field']

        game_tic_tac_toe.play(button_pressed)

    return render_template('tic-tac-toe.html',
                           fields=game_tic_tac_toe.fields,
                           game_result=game_tic_tac_toe.result)


if __name__ == '__main__':
    app.run(debug=True)