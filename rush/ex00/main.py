
from rush.ex00.checkmate import is_checkmate

def main():
    board = """\
    R...
    .K..
    ..Q.
    ....\
    """

    if is_checkmate(board):
      print("Success")
    else:
       print("Fail")

    if _name_ == "_main_":
        main()
