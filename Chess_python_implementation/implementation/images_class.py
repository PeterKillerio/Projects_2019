from tkinter import *

class images_class_:
    def __init__(self):
        self.rows_cols = []

        #  adding square images
        sq_1 = PhotoImage(file="images/sq/1.gif")
        sq_2 = PhotoImage(file="images/sq/2.gif")
        self.rows_cols.append([sq_1, sq_2])

        for f_col in range(1, 3):
            for s_col in range(1, 3):
                img_list = []

                for img_num in range(0, 6):
                    url = "images/" + str(f_col) + str(s_col) + "/" + str(img_num) + ".gif"
                    img = PhotoImage(file=url)
                    img_list.append(img)

                self.rows_cols.append(img_list)
