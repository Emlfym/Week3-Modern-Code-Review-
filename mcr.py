Emingway 2024/12/27 16:52:03
外面两家全部都有梅尔和维克托

Emingway 2024/12/27 16:52:05
神经

杨振浩 CS 2024/12/27 16:55:38
好用啊

Emingway 2024/12/28 12:57:10
8876

杨振浩 CS 2024/12/29 15:28:37
别说了，我要恶心死了

杨振浩 CS 2024/12/29 15:28:50
昨天晚上五排大乱斗

杨振浩 CS 2024/12/29 15:29:05
这笔记本怎么用都不舒服

杨振浩 CS 2024/12/29 15:29:22
玩啥都不自在

杨振浩 CS 2024/12/29 15:29:44
昨天还没赢几把

杨振浩 CS 2025/1/1 10:31:51


Emingway 2025/1/1 10:31:58
这个太变态了

Emingway 2025/1/1 10:32:02
昨天看的直播

Emingway 2025/1/1 10:32:05
年度巨献

杨振浩 CS 2025/1/1 10:32:05
在看

杨振浩 CS 2025/1/1 10:32:08
好爽

Emingway 2025/1/1 10:32:15
太搞笑了

杨振浩 CS 2025/1/1 10:32:18
大伙都有一个美好的年度总结

杨振浩 CS 2025/1/1 10:40:28


杨振浩 CS 2025/1/1 10:40:34
还有续集？

Emingway 2025/1/8 11:58:22


杨振浩 CS 2025/1/8 11:58:34
？

Emingway 2025/1/8 16:54:34


Emingway 2025/1/9 13:54:47


Emingway 2025/1/9 13:54:51


Emingway 2025/1/9 18:01:08
你喝什么

杨振浩 CS 2025/1/9 18:01:18
...

杨振浩 CS 2025/1/9 18:01:20
我买了啊

Emingway 2025/1/9 18:01:27
哦

杨振浩 CS 2025/1/9 18:01:28
刚还微信问你了

Emingway 2025/1/15 23:01:30


对方已成功接收了你发送的离线文件“01月10日.exe”(174.32MB)。

Emingway 2025/1/19 18:44:14
https://github.com/ok-oldking/ok-wuthering-waves?tab=readme-ov-file

杨振浩 CS 16:44:12
这段代码主要进行了以下优化：
在is_win函数中，使用一个列表win_conditions来存储所有获胜的条件组合，通过循环遍历这个列表来检查是否有玩家获胜，避免了硬编码的冗长和重复。
在main函数中，定义了常量BOARD_SIZE来表示棋盘的大小，方便后续修改和维护。
对输入进行了更完善的验证，确保用户输入的坐标在有效范围内且为整数。
变量命名更加具有描述性，如player1_symbol、player2_symbol和player_turn等，使代码更易理解。
在打印棋盘时，使用了字符串模板的方式（这里只是简单示例，可根据实际需求进一步优化），提高了打印效率。
这样优化后的代码在结构和可读性上都有了一定的提升，同时也增强了代码的可维护性和健壮性。

杨振浩 CS 16:44:39
Possible Improvements:
① Hardcoded "Win" Condition Checks;
② Redundant with Condition Logic;
③ Poor Input Validation;
④ Inefficient Board Printing;
⑤ No Early Termination for Win;
⑥ Magic Numbers;
⑦ Poor Variable Naming;

杨振浩 CS 16:55:21
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

