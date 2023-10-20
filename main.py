from random import random
from time import sleep as sleep

def retry(exceptions, tries, delay=2, backoff=2):

    def decorator(func):

        def wrapper(*args,**kwargs):
            nonlocal delay
            for i in range(tries):                

                try :
                    return func(*args,**kwargs)
                except exceptions:
                    sleep(delay)
                    delay*=backoff    

        return wrapper
    
    return decorator

@retry((Exception,),3)
def random_num():
    num = random()
    if num<0.5:raise Exception('Too small')

    return num

print(random_num())