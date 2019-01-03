from square import square_

class board_class:
    def __init__(self):
        self.rows_cols = [[None]*8 for _ in range(8)]
        self.assign_color()

    def assign_color(self):
        for y in range(8):
            for x in range(8):
                if (x + y) % 2 == 0:
                    self.rows_cols[y][x] = square_(x, y, 1)  # black is = 1
                else:
                    self.rows_cols[y][x] = square_(x, y, 2)  # white is = 2

    def print_board_color(self):
        for r in self.rows_cols:
            print("--------")
            for u in r:
                print(u._color_onspot)

    def print_board_char(self):
        for r in self.rows_cols:
            print("--------")
            for u in r:
                print(u.char_onspot)

    def add_character(self, x, y, char):
        self.rows_cols[y][x].char_onspot = char

    def remove_char(self, x, y):
        self.rows_cols[y][x].char_onspot = 0


# board[1][7].char_onspot = 1
# mov = [7, 1]
# print(check_move_(board, mov))



