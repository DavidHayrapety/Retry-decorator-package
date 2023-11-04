from time import sleep
from functools import wraps


def retry(exceptions, tries, delay=2, backoff=2, logger=None):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal delay
            count = 1
            for i in range(tries):

                try:
                    print(f'Try number {count}')
                    return func(*args, **kwargs)
                except exceptions:
                    print(f'Error occured')
                    if count < tries:
                        print(f'Wait {delay} seconds')
                        sleep(delay)
                        delay *= backoff

                count += 1

            if count < tries:
                print('Function executed successfully')

        return wrapper

    return decorator
