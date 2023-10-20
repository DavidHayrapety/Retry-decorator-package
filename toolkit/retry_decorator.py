from time import sleep

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
