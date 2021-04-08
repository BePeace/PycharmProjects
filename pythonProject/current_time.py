"""
Prints current date and time
"""
import datetime

time = datetime.datetime.now().time()
if __name__ == '__main__':
    print('In module')
    print(time)

