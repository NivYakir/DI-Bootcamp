# Tuples: imutable lists, which means they can't be changed

my_id = (1347,22)
# print(type(my_id))

nums = [1, 2, 34, 5, 67]
nums_tuple = tuple(nums)
# print(nums_tuple)

# tuple methods
cities = ['NY', 'BO', 'SP', 'RJ', 'NY']

print(cities.count('NY'))

# we can use index
print(cities[1]) # BO
print(cities.index('SP')) # 2

# cities.append('RU') # ERROR: cannot add elements to a tuple
# cities[1] = 'RJ' # ERROR: cannot change elements within a tuple

# unpacking
languages = ('EN','RU','JA','HE')

lang1, lang2, lang3, lang4 = languages
print(lang1, lang4) # EN HE
print(lang2, lang3) # RU JA

# Sets: Sets and dictionaries have no notion of an element index
# therefore cannot be considered sequences
# Sets cannot have multiple occurrences of the same element and can store unordered values

some_set = set()
other_set = {1,2,6}

# set methods:

countries = {"Israel", "US", "Brazil"}
names = {"Shimon", "Israel", "David"}

set_3 = countries.intersection(names) # shows elements that appear in both sets
print(set_3) # {"Israel"} - only element that appears in both sets

merged_set = countries.union(names) # merges unique values into a single set
print(merged_set) # {"David", "US", "Shimon", "Brazil", "Israel"} - Israel will only appear once

diff_set = countries.difference(names)
print(diff_set) # {"Brazil", "US"} - since the difference is applied to the countries set, it will only show the unique elements from the countries set

diff_set2 = names.difference(countries)
print(diff_set2) # {"David", "Shimon"}

# Tuple Exercise
a_tuple = (10, 20, 30, 40)
a, b, c, d = a_tuple

print(a)
print(b)
print(c)
print(d)