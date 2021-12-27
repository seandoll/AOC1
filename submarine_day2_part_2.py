class Submarine:
    def __init__(self):
        self.increase_count = 0
        self.current_reading = 0
        self.horizontal_position = 0
        self.depth = 0
        self.aim = 0

    def move_up(self, move):
        # self.depth -= int(move)
        self.aim -= int(move)

    def move_down(self, move):
        # self.depth += int(move)
        self.aim += int(move)

    def move_forward(self, move):
        self.horizontal_position += int(move)
        self.depth += (self.aim * int(move))

    def horizontal_position(self):
        return self.horizontal_position

    def depth(self):
        return self.depth

    def report_increase(self, reading):
        print(str(reading) + " (increased)")
        self.increase_count += 1

    def report_first_reading(self, reading):
        print(str(reading) + " (N/A - no previous measurement)")

    def move(self, command):
        # command_list = command.split(" ")
        if command[0] == "forward":
            self.move_forward(command[1])
        elif command[0] == "down":
            self.move_down(command[1])
        elif command[0] == "up":
            self.move_up(command[1])

    def analyse(self, current_reading):
        if self.current_reading == 0:
            self.report_first_reading(current_reading)
        elif current_reading > self.current_reading:
            self.report_increase(current_reading)

        self.current_reading = current_reading

