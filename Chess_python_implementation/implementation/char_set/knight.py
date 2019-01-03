from char_set.check_move import check_move_
from char_set.base import base_

class knight_(base_):
    def __init__(self, x, y, color_is, board_):
        base_.__init__(self, x, y, color_is, board_)
        self.id = 2

    def find_moves(self):
        x = self._x
        y = self._y

        possible_moves = []
        to_check = [
            [x + 2, y + 1],
            [x + 2, y - 1],
            [x - 2, y + 1],
            [x - 2, y - 1],
            [x + 1, y + 2],
            [x - 1, y + 2],
            [x + 1, y - 2],
            [x - 1, y - 2]]

        for mov in to_check:
            if check_move_(self.board, mov, self._color_is) == 1:
                possible_moves.append(mov)
            elif check_move_(self.board, mov, self._color_is) == 2:
                possible_moves.append(mov)

        return possible_moves