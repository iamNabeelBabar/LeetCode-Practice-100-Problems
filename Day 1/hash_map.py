def find_two_sum_indices(numbers, target_sum):

    value_to_index = {} 

    for current_index, current_value in enumerate(numbers):
        required_value = target_sum - current_value

        if required_value in value_to_index:
            return [value_to_index[required_value], current_index]

        value_to_index[current_value] = current_index
