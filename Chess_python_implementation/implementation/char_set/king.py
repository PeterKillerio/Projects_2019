from char_set.check_move import check_move_
from char_set.base import base_

class king_(base_):
    def __init__(self, x, y, color_is, board_):
        base_.__init__(self, x, y, color_is, board_)
        self.id = 5
        self.done_moves = 0

    def find_moves(self):
        x = self._x
        y = self._y

        possible_moves = []

        for i in range(-1, 2, 1):
            for u in range(-1, 2, 1):
                mov = [x + i, y + u]
                if check_move_(self.board, mov, self._color_is) == 1:
                     possible_moves.append(mov)
                elif check_move_(self.board, mov, self._color_is) == 2:
                    possible_moves.append(mov)

        return possible_moves