def init_board():
    """Returns an empty height by width board (with .)."""
    board = []
    for i in range(3):
        board.append([".",".","."])
    return board



def get_move(board):
    """Returns the coordinates of a valid move for player on board."""

    while True:
        possible_rows = ["A","B","C"]
        possible_columns = ["1","2","3"]
        player_move = input("Type your coordinates (eg. A1\B2 ect): ")
        player_move_into_list = list(player_move)
        player_move_length = len(player_move_into_list)
        if player_move_into_list[0] in possible_rows and player_move_into_list[1] in possible_columns and player_move_length == 2:
            coordinates = (player_move_into_list[0],player_move_into_list[1])
            if coordinates[0] == "A":
                if board[0][int(coordinates[1])-1] !=".":
                    print("Place already taken")
                    continue
                else:
                    coordinates = (1,int(player_move_into_list[1]))
                    print(f'The coordinates are: {coordinates}')
                    return coordinates
            elif coordinates[0] == "B":
                if board[1][int(coordinates[1])-1] !=".":
                    print("Place already taken")
                    continue
                else: 
                    coordinates = (2,int(player_move_into_list[1]))
                    print(f'The coordinates are: {coordinates}')
                    return coordinates
            else:
                if board[2][int(coordinates[1])-1] !=".":
                        print("Place already taken")
                        continue
                else:
                    coordinates = (3,int(player_move_into_list[1]))
                    print(f'The coordinates are: {coordinates}')
                    return coordinates      
        else:
            print("Provide valid coordinates!")



def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player. Player == "X" or "O" """

    board[row-1][col-1] = player
    return board


def has_won(board, player):
    """Returns True if player has won the game."""
    winning_positions = [
    [(1,1),(2,1),(3,1)],
    [(1,2),(2,2),(3,2)],
    [(1,3),(2,3),(3,3)],
    [(1,1),(1,2),(1,3)],
    [(2,1),(2,2),(2,3)],
    [(3,1),(3,2),(3,3)],
    [(1,1),(2,2),(3,3)],
    [(3,1),(2,2),(1,3)],
]
    for i in winning_positions:
        if board[i[0][0]-1][i[0][1]-1] == player and board[i[1][0]-1][i[1][1]-1] == player and board[i[2][0]-1][i[2][1]-1] == player:
            return True
        else:
            None
    return False


def is_full(board):
    """Returns True if board is full."""
    for row in board: 
        for place in row: 
            if place == '.':
                return False
    return True



def print_board(board):
    print("  1   2   3")
    print(f'A {board[0][0]} | {board[0][1]} | {board[0][2]}')
    print(" ---+---+---")
    print(f'B {board[1][0]} | {board[1][1]} | {board[1][2]}')
    print(" ---+---+---")
    print(f'C {board[2][0]} | {board[2][1]} | {board[2][2]}')



def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if winner == "X":
        print(r"""
        $$\   $$\       $$\                                 $$\      $$\  $$$$$$\  $$\   $$\ $$\ 
        $$ |  $$ |      $$ |                                $$ | $\  $$ |$$  __$$\ $$$\  $$ |$$ |
        \$$\ $$  |      $$$$$$$\   $$$$$$\   $$$$$$$\       $$ |$$$\ $$ |$$ /  $$ |$$$$\ $$ |$$ |
         \$$$$  /       $$  __$$\  \____$$\ $$  _____|      $$ $$ $$\$$ |$$ |  $$ |$$ $$\$$ |$$ |
         $$  $$<        $$ |  $$ | $$$$$$$ |\$$$$$$\        $$$$  _$$$$ |$$ |  $$ |$$ \$$$$ |\__|
        $$  /\$$\       $$ |  $$ |$$  __$$ | \____$$\       $$$  / \$$$ |$$ |  $$ |$$ |\$$$ |    
        $$ /  $$ |      $$ |  $$ |\$$$$$$$ |$$$$$$$  |      $$  /   \$$ | $$$$$$  |$$ | \$$ |$$\ 
        \__|  \__|      \__|  \__| \_______|\_______/       \__/     \__| \______/ \__|  \__|\__|                                                                                                                                                                                                                                                                       
         """)
    elif winner == "O":
        print(r"""
         $$$$$$\        $$\                                 $$\      $$\  $$$$$$\  $$\   $$\ $$\ 
        $$  __$$\       $$ |                                $$ | $\  $$ |$$  __$$\ $$$\  $$ |$$ |
        $$ /  $$ |      $$$$$$$\   $$$$$$\   $$$$$$$\       $$ |$$$\ $$ |$$ /  $$ |$$$$\ $$ |$$ |
        $$ |  $$ |      $$  __$$\  \____$$\ $$  _____|      $$ $$ $$\$$ |$$ |  $$ |$$ $$\$$ |$$ |
        $$ |  $$ |      $$ |  $$ | $$$$$$$ |\$$$$$$\        $$$$  _$$$$ |$$ |  $$ |$$ \$$$$ |\__|
        $$ |  $$ |      $$ |  $$ |$$  __$$ | \____$$\       $$$  / \$$$ |$$ |  $$ |$$ |\$$$ |    
         $$$$$$  |      $$ |  $$ |\$$$$$$$ |$$$$$$$  |      $$  /   \$$ | $$$$$$  |$$ | \$$ |$$\ 
         \______/       \__|  \__| \_______|\_______/       \__/     \__| \______/ \__|  \__|\__|
         """)
    else:
        print(r"""
             $$$$$$$$\ $$$$$$\ $$$$$$$$\ 
             \__$$  __|\_$$  _|$$  _____|
                $$ |     $$ |  $$ |      
                $$ |     $$ |  $$$$$\    
                $$ |     $$ |  $$  __|   
                $$ |     $$ |  $$ |      
                $$ |   $$$$$$\ $$$$$$$$\ 
                \__|   \______|\________|
            """)
        


def tictactoe_game():
    board = init_board()
    has_won_X = False
    has_won_O = False
    is_fulls = False

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    while has_won_X == False and is_fulls == False and has_won_O == False: 
        print_board(board)
        X_move = get_move(board)
        board = mark(board, "X", X_move[0], X_move[1])
        has_won_X = has_won(board, "X")
        if has_won_X == True: 
            print_result("X")
            return
        is_fulls = is_full(board)
        print_board(board)
        O_move = get_move(board)
        board = mark(board, "O", O_move[0], O_move[1])
        has_won_O = has_won(board, "O")
        if has_won_O == True:
            print_result("O")
            return
        is_fulls = is_full(board)
    print_result(0)


        







    # row, col = get_move(board, 1)
    # mark(board, 1, row, col)

    # winner = 0
    # print_result(winner)


def main_menu():
    tictactoe_game('HUMAN-HUMAN')
    pass

if __name__ == '__main__':
    tictactoe_game()
