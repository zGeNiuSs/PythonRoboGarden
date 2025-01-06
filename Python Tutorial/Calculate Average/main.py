def calculate_average(numbers):

    if not numbers:
        return 0

    total_sum = sum(numbers)
    count = len(numbers)
    average = total_sum / count

    return average

numbers_list = [1, 2, 3, 4, 5]
print(f"The average of the numbers in the list is {calculate_average(numbers_list)}")