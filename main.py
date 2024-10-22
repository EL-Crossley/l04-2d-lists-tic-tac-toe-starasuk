# Put your function here

def ticTacToe(list):
    if list[0][0] == list[0][1] and list[0][1] == list[0][2]:
        winner = list[0][0]
    elif list[0][0] == list[1][0] and list[1][0] == list[2][0]:
        winner = list[0][0]
    elif list[0][0] == list[1][1] and list[1][1] == list[2][2]:
        winner = list[0][0]
    elif list[1][1] == list[1][0] and list[1][1] == list[1][2]:
        winner = list[1][1]
    elif list[1][1] == list[0][2] and list[1][1] == list[2][0]:
        winner = list[1][1]
    elif list[1][1] == list[0][1] and list[1][1] == list[2][1]:
        winner = list[1][1]
    elif list[2][2] == list[2][0] and list[2][2] == list[2][1]:
        winner = list[2][2]
    elif list[2][2] == list[1][2] and list[2][2] == list[0][2]:
        winner = list[2][2]
    else:
        winner = "none"
    return winner
  
# testing
board = [['X','O','O'],['O','X','O'],['X','O','X']]
print(ticTacToe(board))
