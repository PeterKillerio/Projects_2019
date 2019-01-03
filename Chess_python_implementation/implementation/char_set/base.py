class base_:
    def __init__(self, x, y, color_is, board_):
        self._x = x
        self._y = y
        self._color_is = color_is   # color of pawn
        self.board = board_
    av_moves = []
    picture = 0

    def clear_av_moves(self):  # clearing available moves after each turn
        self.av_moves = []