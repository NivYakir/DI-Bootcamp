# Exercise 1: Cars
# 1
my_string = "Volkswagen, Tayata, Ford Motor, Hinda, Chevrolet"

# 2
my_list = my_string.split(', ')

# 3
print(f"There are {len(my_list)} companies in the list.")

# 4
print(sorted(my_list, reverse=True))

# 5 
o_count = 0
no_i_count = 0

for company in my_list:
    if 'o' in company.lower():
        o_count += 1
    elif 'i' not in company.lower():
        no_i_count += 1
    else:
        continue

print(f"There are {o_count} manufacturers with the letter O in them.\nThere are {no_i_count} manufacturers without the letter 'I' in them.")

