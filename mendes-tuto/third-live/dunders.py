class Dunders:
    def __new__(cls):
        print('Building...')
        return super().__new__(cls)

    def __init__(self):
        print('Initializing...')

    def __del__(self):
        print('Ending...')
