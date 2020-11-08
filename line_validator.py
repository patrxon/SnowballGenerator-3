from tuple_operations import add_up

test_points = [[(0, 1), (0, -1)],
               [(0, -1), (0, 1)],
               [(1, 0), (-1, 0)],
               [(-1, 0), (1, 0)]]


class LineTester:

    def __init__(self):
        self.restart_dict()

    def restart_dict(self):
        self.point_dict = set({})
        self.line_dict = set({})

    def check_normal_line(self, p1, p2):
        if p2 in self.point_dict:
            return False

        if (p1, p2) in self.line_dict:
            return False

        for pt in test_points:
            if (add_up(p1, pt[0]), add_up(p2, pt[1])) in self.line_dict:
                return False

        return True

    def check_jump_line(self, p2):
        if p2 in self.point_dict:
            return False

        return True

    def add_line(self, p1, p2):
        if (p1, p2) not in self.line_dict:
            self.line_dict.add((p1, p2))

    def add_point(self, pt):
        if pt not in self.point_dict:
            self.point_dict.add(pt)
