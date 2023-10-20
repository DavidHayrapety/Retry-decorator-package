from random import random

def retry(exceptions, tries, delay=2, backoff=2):

    def decorator(func):

        def wrapper(*args,**kwargs):
            for i in range(tries):                

                try :
                    # func(*args,**kwargs)
                    # print(f'try number {i+1}')
                    return func(*args,**kwargs)

                except exceptions:
                    print("error occured")
                            

        return wrapper
    
    return decorator

@retry((Exception,),3)
def random_num():
    num = random()
    if num<0.5:raise Exception('Too small')

    return num

print(random_num())