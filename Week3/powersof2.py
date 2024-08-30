powerof2=[2**i for i in range(10)]
found = False
index=0
target_value=32

while index < len(powerof2):
    if powerof2[index] == target_value:
        found = True
        break
    index += 1

if found :
    print(f"The value {target_value} was found at index {index}.")
else:
    print(f"The value {target_value} was not found in the list.")
    
