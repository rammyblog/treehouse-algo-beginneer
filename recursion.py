def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def recursive_sum(numbers):
    if not numbers:
        return 0
    print("Calling sum(%s)" % numbers[1:])
    remaining_sum = recursive_sum(numbers[1:])
    print("Call to sum(%s) returning %d + %d" %
          (numbers, numbers[0], remaining_sum))
    return numbers[0] + remaining_sum


print(recursive_sum([1, 3, 5, 3, 33]))
