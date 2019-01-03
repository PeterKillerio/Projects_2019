def check_move_(board, move, color):  # if its valid like not -5,5  and no char on its position and color attack
    x = move[0]
    y = move[1]

    if 8 > x >= 0:
        if 8 > y >= 0:
            if board.rows_cols[y][x].char_onspot == 0:
                return 1
            elif board.rows_cols[y][x].char_onspot._color_is != color:
                return 2
    return 0


