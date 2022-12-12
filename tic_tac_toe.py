import os
import random


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
        player_move = input("Type your coordinates (eg. A1\B2 ect): ").capitalize()
        player_move_into_list = list(player_move)
        player_move_length = len(player_move_into_list)
        if player_move_length == 2:
            if player_move_into_list[0] in possible_rows and player_move_into_list[1] in possible_columns:
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
        
        elif player_move == "Quit":
            os.system("cls || clear")
            exit()
        else:
            print("Provide valid coordinates! (eg. A1\B2 ect):")
        



def get_ai_move(board,human_player,difficulty):
    """Returns the coordinates of a valid move for player on board."""
    if difficulty == "easy":
        for i, row in enumerate(board): 
                for j, place in enumerate(row): 
                    if place == ".":
                        possible_row = i + 1 
                        possible_col = j + 1 
                        ai_move = (possible_row, possible_col)
                        return ai_move
    elif difficulty == "medium":
        while True: 
            random_col = random.randint(1,3)
            random_row = random.randint(1,3)
            if board[random_row-1][random_col-1] == ".":
                ai_move = (random_row, random_col)
                return ai_move
            else:
                continue

    elif difficulty == "hard":
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
        for position in winning_positions: 
            if board[position[0][0]-1][position[0][1]-1] == human_player and board[position[1][0]-1][position[1][1]-1] == human_player and board[position[2][0]-1][position[2][1]-1] == ".":
                print("option1")
                ai_move = (position[2][0],position[2][1])
                return ai_move
            elif board[position[1][0]-1][position[1][1]-1] == human_player and board[position[2][0]-1][position[2][1]-1] == human_player and board[position[0][0]-1][position[0][1]-1] == ".":
                ai_move = (position[0][0],position[0][1])
                print("option4")
                return ai_move  
            elif board[position[0][0]-1][position[0][1]-1] == human_player and board[position[2][0]-1][position[2][1]-1] == human_player and board[position[1][0]-1][position[1][1]-1] == ".":
                print("option3")
                ai_move = (position[1][0],position[1][1])
                return ai_move  
            else: 
                print("option4")
                while True: 
                    print("option5")
                    random_col = random.randint(1,3)
                    random_row = random.randint(1,3)
                    if board[random_row-1][random_col-1] == ".":
                        print("option6")
                        ai_move = (random_row, random_col)
                        return ai_move
                    else:
                        print("option7")
                        continue
    elif difficulty == "minimax":
        bestScore = -1000
        for i, row in enumerate(board): 
            for j, place in enumerate(row): 
                if place == ".":
                    board[i][j] = "X"
                    score = minimax(board,False)
                    board[i][j] = "."
                    if score > bestScore:
                        bestScore = score
                        ai_move = (i+1,j+1)
        return ai_move

    else:
        print("ai difficulty not valid")
        exit()


    

def minimax(board, isMaximizing):
    if has_won(board, "X"):
        return 1
    elif has_won(board, "O"):
        return -1
    elif is_full(board): 
        0
    if isMaximizing:
        bestScore = -1000
        for i, row in enumerate(board):
            for j, place in enumerate(row):
                if board[i][j] == ".":
                    board[i][j] = 'X'
                    score = minimax(board, False)
                    board[i][j] = '.'
                    if score > bestScore:
                        bestScore = score
        return bestScore

    else: 
        bestScore = 1000
        for i, row in enumerate(board):
            for j, place in enumerate(row):
                if board[i][j] == ".":
                    board[i][j] = 'O'
                    score = minimax(board, True)
                    board[i][j] = "."
                    if score < bestScore:
                        bestScore = score
        return bestScore

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
        


def tictactoe_game(mode="HUMAN-HUMAN"):
    board = init_board()
    has_won_X = False
    has_won_O = False
    is_fulls = False

    while has_won_X == False and is_fulls == False and has_won_O == False: 
        # os.system("cls || clear")
        print_board(board)
        print("\nTURN: X\n")
        if mode == "HUMAN-HUMAN" or mode == "HUMAN-AI":
            X_move = get_move(board)
        elif mode == "AI-HUMAN":
            X_move = get_ai_move(board, "O","minimax")
        else:
            print("mode not valid")
            return
        board = mark(board, "X", X_move[0], X_move[1])
        has_won_X = has_won(board, "X")
        if has_won_X == True: 
            # os.system("cls || clear")
            print_board(board)
            print_result("X")
            return
        is_fulls = is_full(board)
        if is_fulls == True: 
            break
        # os.system("cls || clear")
        print_board(board)
        print("\nTURN: O\n")
        if mode == "HUMAN-HUMAN" or mode == "AI-HUMAN":
            O_move = get_move(board)
        elif mode == "HUMAN-AI":
            O_move = get_ai_move(board,"X","minimax")
        else: 
            print("mode not valid")
            return
        board = mark(board, "O", O_move[0], O_move[1])
        has_won_O = has_won(board, "O")
        if has_won_O == True:
            # os.system("cls || clear")
            print_board(board)
            print_result("O")
            return
        is_fulls = is_full(board)
        if is_fulls == True: 
            break
    # os.system("cls || clear")
    print_board(board)       
    print_result(0)



def main_menu():
    tictactoe_game('HUMAN-HUMAN')
    pass

if __name__ == '__main__':
    tictactoe_game('AI-HUMAN')
