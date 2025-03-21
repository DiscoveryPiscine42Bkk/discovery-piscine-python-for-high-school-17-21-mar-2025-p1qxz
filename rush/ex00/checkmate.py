def parse_board(board):
    board = board.strip().split("\n")
    king_position = None
    opponent_pieces = []

    for row in range(len(board)):
        for col in range(len(board[row])):
            piece = board[row][col]
            if piece == "K":
                king_position = (row, col)
            elif piece in "RBQ":
                opponent_pieces.append((piece, row, col))

    return king_position, opponent_pieces


def is_checkmate(board):
    king_position, opponent_pieces = parse_board(board)
    if not king_position:
        print("There is no king on the board.")
        return False

    king_x, king_y = king_position
    board_size = len(board.strip().split("\n"))

    for piece in opponent_pieces:
        piece_type, piece_x, piece_y = piece

        if piece_type == "R":
            if piece_x == king_x or piece_y == king_y:
                return True

        if piece_type == "B":
            if abs(piece_x - king_x) == abs(piece_y - king_y):
                return True

        if piece_type == "Q":
            if piece_x == king_x or piece_y == king_y or abs(piece_x - king_x) == abs(piece_y - king_y):
                return True

    possible_moves = [
        (king_x - 1, king_y - 1), (king_x - 1, king_y), (king_x - 1, king_y + 1),
        (king_x, king_y - 1),                           (king_x, king_y + 1),
        (king_x + 1, king_y - 1), (king_x + 1, king_y), (king_x + 1, king_y + 1)
    ]

    for move in possible_moves:
        new_x, new_y = move
        if 0 <= new_x < board_size and 0 <= new_y < board_size:
            is_safe = True
            for piece in opponent_pieces:
                piece_type, piece_x, piece_y = piece
                if piece_type == "R":
                    if piece_x == new_x or piece_y == new_y:
                        is_safe = False
                        break
                if piece_type == "B":
                    if abs(piece_x - new_x) == abs(piece_y - new_y):
                        is_safe = False
                        break
                if piece_type == "Q":
                    if piece_x == new_x or piece_y == new_y or abs(piece_x - new_x) == abs(piece_y - new_y):
                        is_safe = False
                        break

            if is_safe:
                return False

    print("No escape for the King! Checkmate!")
    return True
