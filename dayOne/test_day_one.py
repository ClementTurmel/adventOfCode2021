import pytest


@pytest.mark.parametrize("input_file, exepected_increase", [
    ("dayOne/example_input.txt", 7),
    ("dayOne/input.txt", 1121)
])
def test_day_one(input_file, exepected_increase):
    actual = count_increase(input_file)

    assert exepected_increase == actual

@pytest.mark.parametrize("input_file, exepected_increase", [
    ("dayOne/example_input.txt", 5),
    #("dayOne/input.txt", 1121)
])
def test_day_one_part_two(input_file, exepected_increase):
    actual = count_increase(input_file)

    assert exepected_increase == actual

def count_increase(file_path):
    return count_increase_from_list(file_to_list_of_int(file_path))

def count_increase_with_sliding_window(file_path):
    return count_increase_sliding_window_from_list(file_to_list_of_int(file_path))


def count_increase_from_list(numbers):
    previous = None
    increase_count = 0
    for number in numbers:
        if previous is not None and number > previous :
            print(f"{number} > {previous} increase !")
            increase_count += 1
        else:
            print(f"{number} <= {previous}")
        
        previous = number

    return increase_count

def count_increase_sliding_window_from_list(numbers):
    sliding_window_size = 3
    sliding_window_numbers = []
    sum = 0
    sum_count = 0
    index = 1
    
    while index < len(numbers):
        print(f"number[i] is {numbers[i]}")
        index += 1



def file_to_list_of_int(file_path):
    file = open(file_path, "r")
    list_of_lign = []
    for lign in file:
        list_of_lign.append(int(lign))

    return list_of_lign
