import json
import random
import sudoko_code
from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route('/sudoku_page', methods=['GET'])
def sudoku_page():
    return render_template('sudoku_page.html')


# If i don't mention what type of method it is, it is automatically a GET type.
@app.route('/get_new_sudoku', methods=['GET'])
def get_new_sudoku():
    # This returns a list of lists representing a table.
    # We have 9 insides lists, each one is a row,
    # and the whole structure is a table.
    new_board = sudoko_code.generate_sudoku()
    for i in range(len(new_board)):
        for j in range(len(new_board[i])):
            # Generating a random number, between 1 and 10
            # There is a 20% that we will remove the number
            # Meaning, that about 20% of the table is going to be missing.
            chance = random.randint(1, 10)
            if chance <= 2:
                new_board[i][j] = 0
    # This is a string
    new_board_as_json = json.dumps({'board': new_board})
    return new_board_as_json


if __name__ == '__main__':
    app.run(debug=True)
