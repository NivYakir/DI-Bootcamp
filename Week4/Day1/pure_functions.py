# Pure Functions

# Given the same input, it will always give the same output
# A function should not produce any side affects (things that a function does which affect the outside world)

def multiply_by_2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    
    return new_list

print(multiply_by_2([1,2,3])) # Will always return the same output, produces no sideaffects
                              # Print statements (in a function) means the function is no longer pure


# ex 2

new_list = []
def multiply_by_2(li):
    for item in li:
        new_list.append(item*2)
    
    return new_list              # no longer a pure function as the new_list is OUTSIDE of the scope of the function
                                 # it now has a side affect
                                 # Pure Functions allow for less buggy code, less compenents interacting with one another 
                                 # They are more of a guideline than an absolute law
                                 