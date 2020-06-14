from tuple_operations import subtract, add_up

directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
dir_dict = {(0, 1): 0, (1, 1): 1, (1, 0): 2, (1, -1): 3, (0, -1): 4, (-1, -1): 5, (-1, 0): 6, (-1, 1): 7}


class LineGenerator:

    def __init__(self, line_tester):
        self.lt = line_tester

    def generate_right(self, prev_point, point):
        dir_ = dir_dict[subtract(prev_point, point)]

        for i in range(8):
            dir_ -= 1
            if dir_ < 0:
                dir_ = 7

            next_point = add_up(point, directions[dir_])
            if self.lt.check_normal_line(point, next_point):
                return next_point

        return False

    def generate_left(self, prev_point, point):
        dir_ = dir_dict[subtract(prev_point, point)]

        for i in range(8):
            dir_ += 1
            if dir_ > 7:
                dir_ = 0

            next_point = add_up(point, directions[dir_])
            if self.lt.check_normal_line(point, next_point):
                return next_point

        return False

    def generate_jump(self, prev_point, point):
        dir_ = dir_dict[subtract(prev_point, point)]

        dir_ += 4
        if dir_ > 7:
            dir_ -= 8

        next_point = add_up(point, directions[dir_])
        if self.lt.check_jump_line(next_point):
            return next_point

        return False

    def generate_line(self, prev_point, point, move):
        if move == "l":
            return self.generate_left(prev_point, point)
        elif move == "r":
            return self.generate_right(prev_point, point)
        elif move == "j":
            return self.generate_jump(prev_point, point)
