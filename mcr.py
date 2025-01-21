BOARD_SIZE = 3

def is_win(game):
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for condition in win_conditions:
        values = [game[i][j] for i, j in condition]
        if values[0] == values[1] == values[2] and values[0]!= '':
            return True
    return False

def main():
    game = [[''for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    player1_symbol = 'X'
    player2_symbol = 'O'
    player_turn = False 
    print("X = Player 1")
    print("O = Player 2")
    for n in range(BOARD_SIZE * BOARD_SIZE):
        player_turn = not player_turn 
        current_player_symbol = player1_symbol if not player_turn else player2_symbol
        print(f"Player {current_player_symbol}: ", end="")
        while True:
            try:
                i, j = map(int, input("Which cell to mark? i:[1..3], j:[1..3]: ").split())
                if 1 <= i <= BOARD_SIZE and 1 <= j <= BOARD_SIZE:
                    i -= 1
                    j -= 1
                    break
                else:
                    print("Invalid input. Please enter values between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter integers.")
        game[i][j] = current_player_symbol
        if is_win(game):
            print("Win!")
            break 
        if n == BOARD_SIZE * BOARD_SIZE - 1: 
            print("Tie!")
        # 打印棋盘（使用字符串模板提高效率，这里简单示例）
        board_str = ""
        for row in game:
            board_str += "|".join(row) + "\n"
            board_str += "-" * (BOARD_SIZE * 2 - 1) + "\n"
        print(board_str)

if __name__ == "__main__":
    main()
