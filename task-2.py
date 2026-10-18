import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    if not (
        # Check if min, max, and quantity are integers and not booleans. bool is a subclass of int in Python,
        # so we need to explicitly check that they are not booleans. Because print(isinstance(True, int)) returns True.
        isinstance(min, int)
        and not isinstance(min, bool)
        and isinstance(max, int)
        and not isinstance(max, bool)
        and isinstance(quantity, int)
        and not isinstance(quantity, bool)
    ):
        return []

    # Check if min is less than 1, max is greater than 1000, or min is greater than or equal to max. If any of these
    # conditions are true, return an empty list.
    if min < 1 or max > 1000 or min >= max:
        return []

    # Check if quantity is less than 1 or greater than the range of numbers. If any of these conditions are true,
    # return an empty list.
    if quantity < 1 or quantity > max - min + 1:
        return []

    # Generate a list of unique random numbers within the specified range and return them sorted.
    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
