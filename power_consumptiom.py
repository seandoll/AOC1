def epsilon_from_gamma(binary_string):
    epsilon = ''
    for item in binary_string:
        if item == '0':
            epsilon += '1'
        else:
            epsilon += '0'
    return epsilon


def only_one_value_remaining(ones, zeros):
    return len(ones) + len(zeros) == 1


class OxygenGeneratorRating:
    def set_dataset(self, ones_in_index_position, zeros_in_index_position):
        print("oxygen_generator_rating set_dataset called")
        if len(ones_in_index_position) >= len(zeros_in_index_position):
            return ones_in_index_position
        else:
            return zeros_in_index_position


class Co2ScrubberRating:
    def set_dataset(self, ones_in_index_position, zeros_in_index_position):
        print("co2_scrubber_rating set_dataset called")
        if len(zeros_in_index_position) <= len(ones_in_index_position):
            return zeros_in_index_position
        else:
            return ones_in_index_position


class PowerConsumption(OxygenGeneratorRating):
    def __init__(self):
        self.source_data = []

    @staticmethod
    def is_one_dominant(data, index):
        one_count = 0
        zero_count = 0
        for item in data:
            if item[index] == '1':
                one_count += 1
            else:
                zero_count += 1

        return one_count > zero_count

    def gamma_rate_binary(self, data):
        binary = ''
        index = 0

        while index < len(data[0]):
            if self.is_one_dominant(data, index):
                binary += "1"
            else:
                binary += '0'
            index += 1

        return binary

    def decimal(self, binary_string):
        return int(binary_string, 2)

    def rating_string(self, test_data, rating):
        working_data = test_data
        char_index = 0
        zeros_in_index_position = []
        ones_in_index_position = []
        while char_index < len(working_data[0]):
            for binary_string in working_data:
                if binary_string[char_index] == '1':
                    ones_in_index_position.append(binary_string)
                else:
                    zeros_in_index_position.append(binary_string)

            working_data = rating.set_dataset(ones_in_index_position, zeros_in_index_position)
            ones_in_index_position = []
            zeros_in_index_position = []
            char_index += 1

            if len(working_data) == 1:
                return working_data[0]

