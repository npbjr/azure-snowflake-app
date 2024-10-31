

def handle_session(func):
    def wrapper(*args):

        f = func(*args)
        print(f)
    return wrapper