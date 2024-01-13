# your code goes here!
import time
import sys

def countdown(number=10):
    while number > 0:
        print(f'{number} SECOND(S)!')
        number -= 1
        sys.stdout.flush()  # Flush the output buffer

    print("HAPPY NEW YEAR!")

countdown()



def countdown_with_sleep(number=10):
    while number > 0:
        print(f'{number} SECOND(S)!')
        number -= 1
        sys.stdout.flush()
        time.sleep(1)  # Pause for one second

    print("HAPPY NEW YEAR!")

    
