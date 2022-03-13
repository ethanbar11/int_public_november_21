import csv
import json

import requests


def save_new_sudoku_to(path):
    server_path = r'http://127.0.0.1:5000/get_new_sudoku'
    resp = requests.get(server_path)
    # Json.loads takes a string that is an encoded json and converts it back to the original object.
    board = json.loads(resp.content)
    with open(path, 'w',newline='') as csv_file:
        writer = csv.writer(csv_file)
        for row in board['board']:
            writer.writerow(row)


# This function returns a clean board that we read
# from the file system
def clean_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            # Converting all cells to int from string.
            if board[i][j] != '':
                board[i][j] = int(board[i][j])


def validate_sudoku(path):
    with open(path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        board = []
        for row in reader:
            if len(row) > 0:
                board.append(row)
        clean_board(board)
        server_path = r'http://127.0.0.1:5000/validate_sudoku'
        response=requests.post(server_path, json=board)
        if response.content==b'Valid':
            print('Great success~!')
        else:
            print('Very very bad.')


# The client asks the user what operation he wants to do
# If he choose to play sudoku, he will get sudoku board
# that is saved into a CSV.
if __name__ == '__main__':
    sudoku_path = 'sudoku.csv'
    print('Welcome to sudoku challenge!')
    print('Choose 1 to get sudoku saved to {}, Choose 2 to validate sudoku '.format(sudoku_path))
    choice = input('Choice : ')
    if choice == '1':
        save_new_sudoku_to(sudoku_path)
    elif choice == '2':
        validate_sudoku(sudoku_path)
