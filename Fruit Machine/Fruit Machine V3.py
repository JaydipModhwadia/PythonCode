#Version 3
import random
def fruit_machine():
    start=input("\nPlease press enter to start or 9 to quit:")
    if start == "9":
        exit()

    
    wheel=["banana", "cherry", "apple", "pear"]

    wheel1pick=random.choice(wheel)
    wheel2pick=random.choice(wheel)
    wheel3pick=random.choice(wheel)

fruit_machine()
