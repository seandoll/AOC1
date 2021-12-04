# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import depth_data


class DepthTracker:
    def __init__(self):
        self.increase_count = 0
        self.decrease_count = 0
        self.unchanged_count = 0
        self.current_reading = 0

    def report_increase(self, reading):
        print(str(reading) + " (increased)")
        self.increase_count += 1

    def report_decrease(self, reading):
        print(str(reading) + " (decreased)")
        self.decrease_count += 1

    def report_unchanged(self, reading):
        print(str(reading) + " (unchanged)")
        self.unchanged_count += 1

    def report_first_reading(self, reading):
        print(str(reading) + " (N/A - no previous measurement)")

    def analyse(self, current_reading):
        if self.current_reading == 0:
            self.report_first_reading(current_reading)
        elif current_reading > self.current_reading:
            self.report_increase(current_reading)
        elif current_reading < self.current_reading:
            self.report_decrease(current_reading)
        else:
            self.report_unchanged(current_reading)

        self.current_reading = current_reading


def sum_3_readings():
    return depth_data.depth_readings[depth_pointer] + depth_data.depth_readings[depth_pointer + 1] + \
           depth_data.depth_readings[depth_pointer + 2]


def windows_to_process():
    return depth_pointer <= len(depth_data.depth_readings) - 3


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    question = 2
    depth_tracker = DepthTracker()

    if question == 1:
        for reading in depth_data.depth_readings:
            depth_tracker.analyse(reading)
    else:
        depth_pointer = 0
        while windows_to_process():
            reading_sum = sum_3_readings()
            depth_tracker.analyse(reading_sum)
            depth_pointer += 1

    print("Total number of increases = " + str(depth_tracker.increase_count))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
