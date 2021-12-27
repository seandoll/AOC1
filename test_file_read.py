import submarine_day2_part_1
from numpy import loadtxt


def test_file_open():
    data = loadtxt("day2_data", dtype='str')
