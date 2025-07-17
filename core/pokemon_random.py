from constants import min_id, maximum_id
import random


def choose_random_num() -> int:
    return random.randint(min_id, maximum_id)


