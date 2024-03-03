import chess
import chess.pgn

board = chess.Board()

def update_board(board):
    image = chess.svg.board(board=board)

    with open("board.svg", "w") as file:
        file.write(image)

update_board(board)

while True:
    move = input("make move: ")
    board.push_san(move)

    update_board(board)

