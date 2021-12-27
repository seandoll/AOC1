# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import depth_data
import power_consumptiom
import submarine_day2_part_1
from numpy import loadtxt

import submarine_day2_part_2


def sum_3_readings():
    return depth_data.depth_readings[depth_pointer] + depth_data.depth_readings[depth_pointer + 1] + \
           depth_data.depth_readings[depth_pointer + 2]


def windows_to_process():
    return depth_pointer <= len(depth_data.depth_readings) - 3


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day = 3
    part = 2

    if day == 1:
        if part == 1:
            sub = submarine_day2_part_1.Submarine()
            for reading in depth_data.depth_readings:
                sub.analyse(reading)
        else:
            depth_pointer = 0
            sub = submarine_day2_part_1.Submarine()
            while windows_to_process():
                reading_sum = sum_3_readings()
                sub.analyse(reading_sum)
                depth_pointer += 1
        print("Total number of increases = " + str(sub.increase_count))
    elif day == 2:
        # get data
        if part == 1:
            sub = submarine_day2_part_1.Submarine()
        else:
            sub = submarine_day2_part_2.Submarine()

        data = loadtxt('day2_data', dtype='str')
        # iterate data
        for item in data:
            sub.move(item)
        print("Horizontal position multiplied by depth = " + str(sub.depth * sub.horizontal_position))
    elif day == 3:
        data = loadtxt('day3_data', dtype='str')
        pc = power_consumptiom.PowerConsumption()
        if part == 1:
            gamma_binary_string = pc.gamma_rate_binary(data)
            gamma = pc.decimal(gamma_binary_string)
            epsilon_binary_string = power_consumptiom.epsilon_from_gamma(gamma_binary_string)
            epsilon = pc.decimal(epsilon_binary_string)
            print('Decimal value = ' + str(gamma * epsilon))
        else:
            rating = power_consumptiom.OxygenGeneratorRating()
            print('Length data = ' + str(len(data)))
            rating_string = pc.rating_string(data, rating)
            oxygen_generator_reading = pc.decimal(rating_string)
            rating = power_consumptiom.Co2ScrubberRating()
            print('Length data = ' + str(len(data)))
            rating_string = pc.rating_string(data, rating)
            co2_generator_reading = pc.decimal(rating_string)
            life_support_rating = oxygen_generator_reading * co2_generator_reading
            print('life support rating = ' + str(life_support_rating))




