def logger(func):
    def wrapper():
        print('Logger execution')
        func()
        print('Done logging')
    return wrapper

@logger
def sample():
    print('Inside sample function')

sample()
