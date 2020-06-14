from line_generator import LineGenerator
from line_validator import LineTester


class LineManager():

    def __init__(self):
        self.line_validator = LineTester()
        self.line_generator = LineGenerator(self.line_validator)

        self.lines = []
        self.patterns = []
        self.pointer = []

        self.counter = 1
        self.iter = 0

    def change_speed(self, change):
        self.counter += change

    def add_line(self, start_a, start_b, pattern):
        self.lines.append([[start_a, "r"], [start_b, "r"]])
        self.line_validator.add_point(start_a)
        self.add_segment(start_a, start_b, "r")
        self.patterns.append(pattern)
        self.pointer.append(0)

    def add_segment(self, curr_point, next_point, move):
        if move != "j":
            self.line_validator.add_point(next_point)
            self.line_validator.add_point(curr_point)
            self.line_validator.add_line(curr_point, next_point)

    def iterate_lines(self):

        self.iter += 1
        if self.iter >= self.counter:
            self.iter = 0
            for i in range(len(self.lines)):
                move = self.patterns[i][self.pointer[i]]
                self.pointer[i] += 1
                if self.pointer[i] >= len(self.patterns[i]):
                    self.pointer[i] = 0

                prev_point = self.lines[i][-2][0]
                curr_point = self.lines[i][-1][0]
                next_point = self.line_generator.generate_line(prev_point, curr_point, move)

                if next_point:
                    self.lines[i].append([next_point, move])
                    self.add_segment(curr_point, next_point, move)

    def get_lines(self):
        return self.lines
