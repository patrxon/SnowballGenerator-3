from tuple_operations import add_up

test_points = [[(0, 1), (0, -1)],
               [(0, -1), (0, 1)],
               [(1, 0), (-1, 0)],
               [(-1, 0), (1, 0)]]


class LineTester:

    def __init__(self, start_points):

        self.point_dict = set({})
        for point in start_points:
            self.point_dict.add(point)
        self.line_dict = set({})

    def check_normal_line(self, p1, p2):
        print(self.point_dict)
        print(self.line_dict)
        if p2 in self.point_dict:
            return False

        if (p1, p2) in self.line_dict:
            return False

        for pt in test_points:
            print((add_up(p1, pt[0]), add_up(p2, pt[1])))
            if (add_up(p1, pt[0]), add_up(p2, pt[1])) in self.line_dict:
                return False

        return True

    def check_jump_line(self, p1, p2):
        return False

    def add_line(self, p1, p2):
        self.line_dict.add((p1, p2))

    def add_point(self, pt):
        self.point_dict.add(pt)
