from line_generator import LineGenerator
from line_tester import LineTester


class LineManager():

    def __init__(self):
        self.line_tester = LineTester()
        self.line_generator = LineGenerator(self.line_tester)

        self.lines = []
        self.patterns = []
        self.pointer = []

    def add_line(self, start_a, start_b, pattern):
        self.lines.append({start_a: "r", start_b: "r"})
        self.line_tester.add_point(start_a)
        self.new_line(start_a, start_b, "r")
        self.patterns.append(pattern)
        self.pointer.append(0)

    def new_line(self, curr_point, next_point, move):
        self.line_tester.add_point(next_point)
        if move != "j":
            self.line_tester.add_line(curr_point, next_point)

    def iterate_lines(self):

        for i in range(len(self.lines)):
            move = self.patterns[i][self.pointer[i]]
            self.pointer[i] += 1
            if self.pointer[i] >= len(self.patterns[i]):
                self.pointer[i] = 0

            prev_point = list(self.lines[i])[len(self.lines[i]) - 2]
            curr_point = list(self.lines[i])[len(self.lines[i]) - 1]
            next_point = self.line_generator.generate_line(prev_point, curr_point, move)

            if next_point:
                self.lines[i][next_point] = move
                self.new_line(curr_point, next_point, move)

    def get_lines(self):
        return self.lines
