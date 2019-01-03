from tkinter import *
import copy
from board import board_class
from images_class import images_class_
from char_set.pawn import pawn_
from char_set.rook import rook_
from char_set.knight import knight_
from char_set.bishop import bishop_
from char_set.queen import queen_
from char_set.king import king_
#  core tkinter
root = Tk()
#  copying all images
all_images_class = images_class_()
all_images = copy.copy(all_images_class.rows_cols)
#  adding global variables for functionality and comunication between logic and display
last_to_move = []
on_move = 2  #  white=2  black=1
check = 0
marked = 0
is_marked = [0,0]
is_attacked = [0,0]
board_logic = []
board_display = []

class button:
    def __init__(self, plane, base_color, xx, yy):
        self.button = Button(plane, height=64, width=64)
        self.button.grid(row=yy, column=xx)
        self.is_clicked = 0
        self.is_color = base_color - 1
        self.x = xx
        self.y = yy
        self.change_to_sq()

    def change_to_sq(self):  #  changing image of the button to the corresponding square color
        self.button.configure(image=all_images[0][self.is_color])
    def add_func(self):   #  adding the button its on click functionality
        self.button.configure(command = self.click)
    def add_char(self, x_to, y_to, col_from, id_from):  #  function which adds chess pieces globaly
        global board_logic
        if id_from == 0:
            board_logic.add_character(x_to, y_to, pawn_(x_to, y_to, col_from, board_logic))
            board_logic.rows_cols[y_to][x_to].char_onspot.done_moves = 1
        elif id_from == 1:
            board_logic.add_character(x_to, y_to, bishop_(x_to, y_to, col_from, board_logic))
        elif id_from == 2:
            board_logic.add_character(x_to, y_to, knight_(x_to, y_to, col_from, board_logic))
        elif id_from == 3:
            board_logic.add_character(x_to, y_to, rook_(x_to, y_to, col_from, board_logic))
            board_logic.rows_cols[y_to][x_to].char_onspot.done_moves = 1
        elif id_from == 4:
            board_logic.add_character(x_to, y_to, queen_(x_to, y_to, col_from, board_logic))
        elif id_from == 5:
            board_logic.add_character(x_to, y_to, king_(x_to, y_to, col_from, board_logic))
            board_logic.rows_cols[y_to][x_to].char_onspot.done_moves = 1
    def add_char_local(self, x_to, y_to, col_from, id_from, b_logic):  #  function which add chess pieces to specific
        if id_from == 0:
            b_logic.add_character(x_to, y_to, pawn_(x_to, y_to, col_from, b_logic))
            b_logic.rows_cols[y_to][x_to].char_onspot.done_moves = 1
        elif id_from == 1:
            b_logic.add_character(x_to, y_to, bishop_(x_to, y_to, col_from, b_logic))
        elif id_from == 2:
            b_logic.add_character(x_to, y_to, knight_(x_to, y_to, col_from, b_logic))
        elif id_from == 3:
            b_logic.add_character(x_to, y_to, rook_(x_to, y_to, col_from, b_logic))
        elif id_from == 4:
            b_logic.add_character(x_to, y_to, queen_(x_to, y_to, col_from, b_logic))
        elif id_from == 5:
            b_logic.add_character(x_to, y_to, king_(x_to, y_to, col_from, b_logic))

    def change_2_to_1(self,num):
        if num == 1:
            return 2
        elif num == 2:
            return 1
        else:
            print("display.py change_2_to_1 error")
    def change_turn(self):
        global on_move
        if on_move == 1:
            on_move = 2
            print("white turn")
        elif on_move == 2:
            on_move = 1
            print("black turn")

    def castling(self, logic):
        global is_marked
        global is_attacked
        global board_display

        piece = logic.rows_cols[is_marked[1]][is_marked[0]].char_onspot

        black_castle = [[2,0],[6,0]]
        white_castle = [[2,7],[6,7]]

        if piece.id == 5:
            if piece.done_moves == 0:

                if piece._color_is == 1:
                    br_1 = logic.rows_cols[0][0].char_onspot
                    if br_1 != 0:
                        if br_1.id == 3:
                            if br_1.done_moves == 0:
                                if is_attacked == [2,0]:
                                    obtained = 0
                                    between = [[1,0],[2,0],[3,0]]
                                    for pos in between:
                                        is_there = logic.rows_cols[pos[1]][pos[0]].char_onspot
                                        if is_there != 0:
                                            obtained = obtained + 1

                                    if obtained == 0:
                                        copy_logic = copy.deepcopy(logic)


                                        self.add_char_local(2, 0, 1, 5, copy_logic)
                                        copy_logic.remove_char(piece._x, piece._y)

                                        vertify = self.is_check(copy_logic, on_move)
                                        check = vertify

                                        if vertify == 0:

                                            self.add_char_local(2, 0, 1, 5, logic)
                                            logic.remove_char(piece._x, piece._y)

                                            self.add_char_local(3, 0, 1, 3, logic)
                                            logic.remove_char(0, 0)

                                            board_display.update(logic)
                                        else:
                                            print("THERE IS A CHECK")

                    br_2 = logic.rows_cols[0][7].char_onspot

                    if br_2 != 0:
                        if br_2.id == 3:
                            if br_2.done_moves == 0:
                                if is_attacked == [6,0]:
                                    obtained = 0
                                    between = [[6,0],[5,0]]
                                    for pos in between:
                                        is_there = logic.rows_cols[pos[1]][pos[0]].char_onspot
                                        if is_there != 0:
                                            obtained = obtained + 1

                                    if obtained == 0:
                                        copy_logic = copy.deepcopy(logic)

                                        self.add_char_local(6, 0, 1, 5, copy_logic)
                                        copy_logic.remove_char(piece._x, piece._y)

                                        vertify = self.is_check(copy_logic, on_move)
                                        check = vertify

                                        if vertify == 0:

                                            self.add_char_local(6, 0, 1, 5, logic)
                                            logic.remove_char(piece._x, piece._y)

                                            self.add_char_local(5, 0, 1, 3, logic)
                                            logic.remove_char(7, 0)

                                            board_display.update(logic)
                                        else:
                                            print("THERE IS A CHECK")

                elif piece._color_is == 2:
                    wr_1 = logic.rows_cols[7][0].char_onspot
                    if wr_1 != 0:
                        if wr_1.id == 3:
                            if wr_1.done_moves == 0:
                                if is_attacked == [2, 7]:
                                    obtained = 0
                                    between = [[1, 7], [2, 7], [3, 7]]
                                    for pos in between:
                                        is_there = logic.rows_cols[pos[1]][pos[0]].char_onspot
                                        if is_there != 0:
                                            obtained = obtained + 1

                                    if obtained == 0:
                                        copy_logic = copy.deepcopy(logic)

                                        self.add_char_local(2, 7, 2, 5, copy_logic)
                                        copy_logic.remove_char(piece._x, piece._y)

                                        vertify = self.is_check(copy_logic, on_move)
                                        check = vertify

                                        if vertify == 0:

                                            self.add_char_local(2, 7, 2, 5, logic)
                                            logic.remove_char(piece._x, piece._y)

                                            self.add_char_local(3, 7, 2, 3, logic)
                                            logic.remove_char(0, 7)

                                            board_display.update(logic)
                                        else:
                                            print("THERE IS A CHECK")

                    wr_2 = logic.rows_cols[7][7].char_onspot
                    if wr_2 != 0:
                        if wr_2.id == 3:
                            if wr_2.done_moves == 0:
                                if is_attacked == [6, 7]:
                                    obtained = 0
                                    between = [[5, 7], [6, 7]]
                                    for pos in between:
                                        is_there = logic.rows_cols[pos[1]][pos[0]].char_onspot
                                        if is_there != 0:
                                            obtained = obtained + 1

                                    if obtained == 0:
                                        copy_logic = copy.deepcopy(logic)

                                        self.add_char_local(6, 7, 2, 5, copy_logic)
                                        copy_logic.remove_char(piece._x, piece._y)

                                        vertify = self.is_check(copy_logic, on_move)
                                        check = vertify

                                        if vertify == 0:

                                            self.add_char_local(6, 7, 2, 5, logic)
                                            logic.remove_char(piece._x, piece._y)

                                            self.add_char_local(5, 7, 2, 3, logic)
                                            logic.remove_char(7, 7)

                                            board_display.update(logic)
                                        else:
                                            print("THERE IS A CHECK")
















    def is_pawn_queen(self, logic):


        for rows in logic.rows_cols:
            for cols in rows:
                piece = cols.char_onspot
                if piece != 0:
                    if piece.id == 0:
                        x = piece._x
                        y = piece._y
                        colr = piece._color_is

                        if colr == 1:
                            if y == 7:
                                board_logic.remove_char(x, y)
                                self.add_char(x, y, colr, 4)
                                board_display.update(board_logic)

                        if colr == 2:
                            if y == 0:
                                board_logic.remove_char(x, y)
                                self.add_char(x, y, colr, 4)
                                board_display.update(board_logic)






    def is_stale_mate(self, logic):
        global check

        if check == 0:
            #  king has no safe options -> other pieces have no options
            # find kings
            white_king = []
            black_king = []
            #  all attacks
            black_atk = []
            white_atk = []

            for rows in logic.rows_cols:
                for cols in rows:
                    piece = cols.char_onspot
                    if piece != 0:
                        if piece._color_is == 1:
                            moves = piece.find_moves()
                            black_atk.append(moves)
                        elif piece._color_is == 2:
                            moves = piece.find_moves()
                            white_atk.append(moves)
                        if piece.id == 5:
                            if piece._color_is == 1:
                                black_king = [piece._x, piece._y]
                            else:
                                white_king = [piece._x, piece._y]



            #  all kings moves
            wk_moves = logic.rows_cols[white_king[1]][white_king[0]].char_onspot.find_moves()
            bk_moves = logic.rows_cols[black_king[1]][black_king[0]].char_onspot.find_moves()

            #  we first begin to check how many secure moves do kings have
            wk_moves_tmp = copy.copy(wk_moves)

            for each_wk in wk_moves_tmp:
                for each_bk_atks in black_atk:
                    for each_bk_atk in each_bk_atks:
                        if each_wk == each_bk_atk:
                            if each_wk in wk_moves:
                                wk_moves.remove(each_bk_atk)
            #
            # print("WHITE KING FREE MOVES")
            # print(wk_moves)
            # print(len(wk_moves))


            bk_moves_tmp = copy.copy(bk_moves)

            for each_bk in bk_moves_tmp:

                for each_wt_atks in white_atk:
                    for each_wt_atk in each_wt_atks:
                        if each_bk == each_wt_atk:
                            if each_bk in bk_moves:
                                bk_moves.remove(each_wt_atk)

            # print("BLACK KING FREE MOVES")
            # print(bk_moves)
            # print(len(bk_moves))

            #  number of moves for each color
            white_moves_pieces = 0
            for pieces in white_atk:
                white_moves_pieces = white_moves_pieces + len(pieces)



            black_moves_pieces = 0
            for pieces in black_atk:
                black_moves_pieces = black_moves_pieces + len(pieces)



            white_moves_total = white_moves_pieces - len(wk_moves_tmp)
            black_moves_total = black_moves_pieces - len(bk_moves_tmp)

            print(white_moves_total)


            if white_moves_total == 0:
                print("BIELY KRAL MA NULA POHYBOV a ani kamaratov")
            if black_moves_total == 0:
                print("CIERNY KRAL MA NULA POHYBOV a ani kamaratov")


    def is_check_mate(self, logic):
        global last_to_move
        global check

        if check != 0:

            # find kings
            white_king = []
            black_king = []
            #  all attacks
            black_atk = []
            white_atk = []

            for rows in logic.rows_cols:
                for cols in rows:
                    piece = cols.char_onspot
                    if piece != 0:
                        if piece._color_is == 1:
                            moves = piece.find_moves()
                            black_atk.append(moves)
                        elif piece._color_is == 2:
                            moves = piece.find_moves()
                            white_atk.append(moves)
                        if piece.id == 5:
                            if piece._color_is == 1:
                                black_king = [piece._x, piece._y]
                            else:
                                white_king = [piece._x, piece._y]
            #  all kings moves
            wk_moves = logic.rows_cols[white_king[1]][white_king[0]].char_onspot.find_moves()
            bk_moves = logic.rows_cols[black_king[1]][black_king[0]].char_onspot.find_moves()

            # we will vertify all possibilities of destroy attacker considering last moved piece
            last_piece = logic.rows_cols[last_to_move[1]][last_to_move[0]].char_onspot

            #  we first begin to check how many secure moves do kings have

            wk_moves_tmp = copy.copy(wk_moves)

            for each_wk in wk_moves_tmp:
                for each_bk_atks in black_atk:
                    for each_bk_atk in each_bk_atks:
                        if each_wk == each_bk_atk:
                            if each_wk in wk_moves:
                                wk_moves.remove(each_bk_atk)

            print("WHITE KING FREE MOVES")
            print(wk_moves)
            print(len(wk_moves))

            bk_moves_tmp = copy.copy(bk_moves)

            for each_bk in bk_moves_tmp:
                for each_wt_atks in white_atk:
                    for each_wt_atk in each_wt_atks:
                        if each_bk == each_wt_atk:
                            if each_bk in bk_moves:
                                bk_moves.remove(each_wt_atk)

            print("BLACK KING FREE MOVES")
            print(bk_moves)
            print(len(bk_moves))

            #  is there a move which can delete check ?
            is_there = 0

            for rows in logic.rows_cols:
                for cols in rows:
                    piece = cols.char_onspot
                    if piece != 0:
                        if piece._color_is == check:
                            for each_poss in piece.find_moves():
                                alt_board = copy.deepcopy(logic)

                                self.add_char_local(each_poss[0], each_poss[1], piece._color_is, piece.id, alt_board)
                                alt_board.remove_char(piece._x, piece._y)

                                vertify = self.is_check(alt_board, check)
                                if vertify != check:
                                    is_there = is_there + 1

            if is_there == 0:
                print("CHECKMATE")
            else:
                print("NOT CHECKMATE")

    def is_check(self, logic, is_moving):

        # find kings
        white_king = []
        black_king = []

        for rows in logic.rows_cols:
            for cols in rows:
                piece = cols.char_onspot
                if piece != 0:
                    if piece.id == 5:
                        if piece._color_is == 1:
                            black_king = [piece._x, piece._y]
                        else:
                            white_king = [piece._x, piece._y]

        white_attacks = []
        black_attacks = []

        for rows in logic.rows_cols:
            for cols in rows:
                piece = cols.char_onspot
                if piece != 0:
                    if piece._color_is == 1:
                        black_attacks.append(piece.find_moves())
                    else:
                        white_attacks.append(piece.find_moves())

        #  if somebody attacks some king
        for attack in black_attacks:
            if white_king in attack:
                if is_moving == 1:
                    delete_this = 1
                    #  print("white has check, but we dont care")
                else:
                    #  print("white has check")
                    return 2
        for attack in white_attacks:
            if black_king in attack:
                if is_moving == 2:
                    delete_this = 1
                    #  print("black has check, but we dont care")
                else:
                    #  print("black has check")
                    return 1
        return 0

    def move_attack(self): #  function which adds and removes chess pieces
        global on_move
        global last_to_move
        global check
        global is_marked
        global is_attacked
        global board_logic
        global board_display

        marked_piece = board_logic.rows_cols[is_marked[1]][is_marked[0]].char_onspot

        moves = marked_piece.find_moves()
        print(moves)

        x_from = is_marked[0]
        y_from = is_marked[1]
        col_from = marked_piece._color_is
        id_from = marked_piece.id
        x_to = is_attacked[0]
        y_to = is_attacked[1]

        copy_logic = copy.deepcopy(board_logic)   #  creating one board in the future

        self.castling(board_logic)

        if is_attacked in moves:  #  checks if the move we want to make is available for that piece
            self.add_char_local(x_to, y_to, col_from, id_from, copy_logic)
            copy_logic.remove_char(x_from, y_from)

            vertify = self.is_check(copy_logic, on_move)
            check = vertify
            if vertify == 0:
                self.add_char(x_to, y_to, col_from, id_from)
                board_logic.remove_char(x_from, y_from)
                board_display.update(board_logic)



                self.change_turn()

                self.is_pawn_queen(board_logic)
                check = self.is_check(board_logic, on_move)
                self.is_check_mate(board_logic)
                self.is_stale_mate(board_logic)



                last_to_move = [x_to, y_to]


                print("legal move")
            else:
                print("illegal move, there is a check")

    def click(self):  #  click function which is started on each click/ saves clicked and attacked pieces
        global on_move
        global marked
        global is_marked
        global is_attacked
        global board_logic

        if marked == 0:

            marked_piece = board_logic.rows_cols[self.y][self.x].char_onspot
            if marked_piece != 0:
                if on_move == marked_piece._color_is:
                    marked = 1
                    is_marked = [self.x, self.y]

        elif marked == 1:
            marked = 0
            is_attacked = [self.x, self.y]
            self.move_attack()

    def change_to(self, char_col, char_id):  #  this function helps updating whole board
        char_image = None
        if self.is_color == 0:
            if char_col == 1:
                char_image = all_images[1][char_id]
            elif char_col == 2:
                char_image = all_images[3][char_id]
        elif self.is_color == 1:
            if char_col == 1:
                char_image = all_images[2][char_id]
            elif char_col == 2:
                char_image = all_images[4][char_id]

        self.button.configure(image=char_image)
    def update(self, logic):  #  this function helps updating whole board
        if logic.rows_cols[self.y][self.x].char_onspot == 0:
            self.change_to_sq()
        else:
            id = logic.rows_cols[self.y][self.x].char_onspot.id
            color = logic.rows_cols[self.y][self.x].char_onspot._color_is
            self.change_to(color, id)

class board_buttons_:
    def __init__(self):
        self.rows_cols = [[None]*8 for _ in range(8)]
        self.assign_color()

    def assign_color(self):  #  this funtion assigns button to each item in list with position and color
        for y in range(8):
            for x in range(8):
                if (x + y) % 2 == 0:
                    self.rows_cols[y][x] = button(root, 1, x, y)  # black is = 1
                    self.rows_cols[y][x].add_func()
                else:
                    self.rows_cols[y][x] = button(root, 2, x, y)  # white is = 2
                    self.rows_cols[y][x].add_func()

    def update(self, board_logic):  #  updated the whole board
        for rows in range(8):
            for cols in range(8):
                self.rows_cols[rows][cols].update(board_logic)


#  creation of logical part of the game
board_logic = board_class()

#  declaration of the whole classic chess board

for i in range(8):
    board_logic.add_character(i, 6, pawn_(i, 6, 2, board_logic))
    board_logic.add_character(i, 1, pawn_(i, 1, 1, board_logic))

board_logic.add_character(0, 0, rook_(0, 0, 1, board_logic))
board_logic.add_character(7, 0, rook_(7, 0, 1, board_logic))
board_logic.add_character(7, 7, rook_(7, 7, 2, board_logic))
board_logic.add_character(0, 7, rook_(0, 7, 2, board_logic))

board_logic.add_character(2, 0, bishop_(2, 0, 1, board_logic))
board_logic.add_character(5, 0, bishop_(5, 0, 1, board_logic))
board_logic.add_character(2, 7, bishop_(2, 7, 2, board_logic))
board_logic.add_character(5, 7, bishop_(5, 7, 2, board_logic))

board_logic.add_character(1, 0, knight_(1, 0, 1, board_logic))
board_logic.add_character(6, 0, knight_(6, 0, 1, board_logic))
board_logic.add_character(1, 7, knight_(1, 7, 2, board_logic))
board_logic.add_character(6, 7, knight_(6, 7, 2, board_logic))

board_logic.add_character(3, 0, queen_(3, 0, 1, board_logic))
board_logic.add_character(3, 7, queen_(3, 7, 2, board_logic))

board_logic.add_character(4, 0, king_(4, 0, 1, board_logic))
board_logic.add_character(4, 7, king_(4, 7, 2, board_logic))

#  loading a graphical board and updating it according to logical one
board_display = board_buttons_()
board_display.update(board_logic)

#  print(board_logic.rows_cols[0][4].char_onspot.done_moves)

#  running game
root.mainloop()




