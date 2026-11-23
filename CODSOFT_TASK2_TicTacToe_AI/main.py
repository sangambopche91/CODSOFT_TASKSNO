HUMAN = "X"
AI = "O"
EMPTY = " "


def print_board(board):
    print()
    for r in range(3):
        cells = []
        for c in range(3):
            value = board[r * 3 + c]
            cells.append(value if value != EMPTY else str(r * 3 + c + 1))
        print(" " + " | ".join(cells))
        if r < 2:
            print("---+---+---")
    print()


def get_winner(board):
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in lines:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_draw(board):
    return get_winner(board) is None and EMPTY not in board


def minimax(board, depth, maximizing, alpha, beta):
    winner = get_winner(board)

    if winner == AI:
        return 10 - depth
    if winner == HUMAN:
        return depth - 10
    if is_draw(board):
        return 0

    if maximizing:
        best = float("-inf")
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = EMPTY
                best = max(best, score)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best

    best = float("inf")
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = HUMAN
            score = minimax(board, depth + 1, True, alpha, beta)
            board[i] = EMPTY
            best = min(best, score)
            beta = min(beta, best)
            if beta <= alpha:
                break
    return best


def get_ai_move(board):
    best_score = float("-inf")
    best_move = None

    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            score = minimax(board, 0, False, float("-inf"), float("inf"))
            board[i] = EMPTY

            if score > best_score:
                best_score = score
                best_move = i

    return best_move


def get_human_move(board):
    while True:
        choice = input("Choose a position (1-9): ").strip()

        if not choice.isdigit() or not 1 <= int(choice) <= 9:
            print("Enter a valid number from 1 to 9.")
            continue

        position = int(choice) - 1

        if board[position] != EMPTY:
            print("Position already occupied.")
            continue

        return position


def play_game():
    print("=== TIC-TAC-TOE AI ===")
    print("You are X. AI is O.")

    board = [EMPTY] * 9
    print_board(board)

    while True:
        board[get_human_move(board)] = HUMAN
        print_board(board)

        if get_winner(board) == HUMAN:
            print("You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        print("AI is thinking...")
        move = get_ai_move(board)
        board[move] = AI
        print_board(board)

        if get_winner(board) == AI:
            print("AI wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break


if __name__ == "__main__":
    play_game()
