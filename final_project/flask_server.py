import json

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
    new_board = sudoko_code.generate_sudoku()

    # This is a string
    new_board_as_json = json.dumps(new_board)
    print(new_board_as_json)
    return new_board_as_json


if __name__ == '__main__':
    app.run(debug=True)
