def count_multiples(numbers, given_numbers):
    counts = {num: 0 for num in given_numbers}
    for number in numbers:
        for given_num in given_numbers:
            if number % given_num == 0:
                counts[given_num] += 1
    return counts
