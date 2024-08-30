# To  reposition the items in the list by doing a circular right shift. The number of positions shifted will be based on a user-specified value.

import random

        
def circular_right_shift(lst, positions):
    n = len(lst)
    positions = positions % n 
    return lst[-positions:] + lst[:-positions]

def main():
        
    lis = []
    n =  15
    i = 0
    while i < n :
        lis.append(int(random.randint(0, 100)))
        i += 1
    print("Original list:", lis)

    
    while True:
        try:
            positions = int(input("Enter the number of positions to shift (integer): "))
            if positions < 0:
                print("Please enter a non-negative integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    
    shifted_list = circular_right_shift(lis, positions)
    

    print("List after shifting:", shifted_list)

if __name__ == "__main__":
    main()
