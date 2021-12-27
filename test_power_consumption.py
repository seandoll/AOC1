import power_consumptiom
import submarine_day2_part_1
from numpy import loadtxt

test_data = ['00100',
             '11110',
             '10110',
             '10111',
             '10101',
             '01111',
             '00111',
             '11100',
             '10000',
             '11001',
             '00010',
             '01010']
# test_data = loadtxt('day3_test_data', dtype='str')


def test_file_open():
    data = loadtxt("day3_test_data", dtype='str')
    assert data[0] == '00100'
    assert data[len(data) - 1] == '01010'


def test_one_is_dominant():
    pc = power_consumptiom.PowerConsumption()
    assert pc.is_one_dominant(test_data, 0) == True
    assert pc.is_one_dominant(test_data, 1) == False
    assert pc.is_one_dominant(test_data, 2) == True
    assert pc.is_one_dominant(test_data, 3) == True
    assert pc.is_one_dominant(test_data, 4) == False


def test_gamma_rate():
    pc = power_consumptiom.PowerConsumption()
    binary_string = '10110'
    assert pc.gamma_rate_binary(test_data) == binary_string
    assert pc.decimal(binary_string) == 22


def test_epsilon_from_gamma():
    pc = power_consumptiom
    binary_string = '10110'
    assert pc.epsilon_from_gamma(binary_string) == '01001'


def test_oxygen_generator_rating():
    pc = power_consumptiom.PowerConsumption()
    rating_impl = power_consumptiom.OxygenGeneratorRating()
    assert pc.rating_string(test_data, rating_impl) == '10111'


def test_co2_scrubber_rating():
    pc = power_consumptiom.PowerConsumption()
    rating_impl = power_consumptiom.Co2ScrubberRating()
    assert pc.rating_string(test_data, rating_impl) == '01010'
