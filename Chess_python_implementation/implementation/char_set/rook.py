from char_set.check_move import check_move_
from char_set.base import base_

class rook_(base_):
    def __init__(self, x, y, color_is, board_):
        base_.__init__(self, x, y, color_is, board_)
        self.id = 3
        self.done_moves = 0

    def find_moves(self):
        x = self._x
        y = self._y

        possible_moves = []

        # movement in right dir
        for i in range(x+1, 8):
            mov = [i, y]
            if check_move_(self.board, mov, self._color_is) == 1:      # this solution works great if there is some obstacle in the way
                possible_moves.append(mov)
            elif check_move_(self.board, mov, self._color_is) == 2:
                possible_moves.append(mov)
                break
            else:
                break
        # movement in left dir
        for i in range(x-1, -1, -1):
            mov = [i, y]
            if check_move_(self.board, mov, self._color_is) == 1:      # this solution works great if there is some obstacle in the way
                possible_moves.append(mov)
            elif check_move_(self.board, mov, self._color_is) == 2:
                possible_moves.append(mov)
                break
            else:
                break
        # movement in down dir
        for i in range(y+1, 8):
            mov = [x, i]
            if check_move_(self.board, mov, self._color_is) == 1:      # this solution works great if there is some obstacle in the way
                possible_moves.append(mov)
            elif check_move_(self.board, mov, self._color_is) == 2:
                possible_moves.append(mov)
                break
            else:
                break
        # movement in up dir
        for i in range(y-1, -1, -1):
            mov = [x, i]
            if check_move_(self.board, mov, self._color_is) == 1:      # this solution works great if there is some obstacle in the way
                possible_moves.append(mov)
            elif check_move_(self.board, mov, self._color_is) == 2:
                possible_moves.append(mov)
                break
            else:
                break

        return possible_moves

