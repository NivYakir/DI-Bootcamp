import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728

def find_pairs(target_number):
    for num1 in list_of_numbers:
        for num2 in list_of_numbers:
            if num1 + num2 == target_number:
                print(f"{num1} and {num2} sums to the target number: {target_number}")



# More efficient version:

seen = set()
pairs = set()  # Use a set to avoid duplicate pairs

for number in list_of_numbers:
    complement = target_number - number
    if complement in seen:
        # Sort the pair to avoid (a,b) and (b,a) duplicates
        pair = tuple(sorted((number, complement)))
        pairs.add(pair)
    else: 
        seen.add(number)

# Print the results
for a, b in pairs:
    print(f"{a} and {b} sum to the target_number {target_number}")