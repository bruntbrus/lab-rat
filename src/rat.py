'''
Rat class.
'''

class Rat:
    def __init__(self, pos_x = 0, pos_y = 0, dir_x = 0, dir_y = -1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dir_x = dir_x
        self.dir_y = dir_y

    def get_position(self):
        return (self.pos_x, self.pos_y)

    def set_position(self, pos_x, pos_y):
        self.pos_x, self.pos_y = pos_x, pos_y

    def get_direction(self):
        return (self.dir_x, self.dir_y)

    def move_forward(self):
        self.pos_x += self.dir_x
        self.pos_y += self.dir_y

    def move_backwards(self):
        self.pos_x -= self.dir_x
        self.pos_y -= self.dir_y

    def rotate_right_90(self):
        self.dir_x, self.dir_y = -self.dir_y, self.dir_x

    def rotate_left_90(self):
        self.dir_x, self.dir_y = self.dir_y, -self.dir_x
