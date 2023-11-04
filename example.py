from toolkit.retry_decorator import retry
from random import random


@retry(Exception, tries=3, delay=2, backoff=0, logger=None)
def random_numbers_interval(p, q):
    """Function generates rundom number in interval [0,1], p, q are from [0,1] interval"""

    random_number = random()

    if random_number < p:
        raise Exception('less than lower bound')
    if random_number > q:
        raise Exception('grader than upper bound')

    return random_number
