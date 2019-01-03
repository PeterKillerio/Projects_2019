from char_set.check_move import check_move_
from char_set.base import base_

class pawn_(base_):

    def __init__(self, x, y, color_is, board_):
        base_.__init__(self, x, y, color_is, board_)
        self.direction = 0          # heading up or down white-black
        self.done_moves = 0         # did he do some moves? -> 1 move front vs 2 moves
        self.id = 0

        if self._color_is == 1:
            self.direction = 1
        else:
            self.direction = -1

    def find_moves(self):
        dir = self.direction
        x = self._x
        y = self._y

        possible_moves = []

        mov = [x + 1, y + (1 * dir)]
        if check_move_(self.board, mov, self._color_is) == 2:
            possible_moves.append(mov)

        mov = [x - 1, y + (1 * dir)]
        if check_move_(self.board, mov, self._color_is) == 2:
            possible_moves.append(mov)

        mov = [x, y+(1*dir)]
        if check_move_(self.board, mov, self._color_is) == 1:
            possible_moves.append(mov)

            if self.done_moves == 0:
                mov = [x, y + (2 * dir)]
                if check_move_(self.board, mov, self._color_is) == 1:
                    possible_moves.append(mov)

        return possible_moves
