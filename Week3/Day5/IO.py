import os     # assists to navigate the operating system

# I/O - Input and Output

# how to read a file

dir_path = os.path.dirname(os.path.realpath(__file__))
print(f"Dir Path: {dir_path}") # C:\Repositories\DI-Bootcamp\Week3\Day5

with open(f'{dir_path}\secrets.txt', 'r', encoding='utf-8') as file_obj:
    file_content = file_obj.read()

    print(file_content)


with open(f"{dir_path}\star_wars.txt", 'r', encoding='utf-8') as f:
    txt_list = f.readlines()

    for line in txt_list:
        print(line)
    
    # read only the fifth line
    print(txt_list[4])

    # # read only the first 5 characters of the file
    print(txt_list[0][:4])

    # read all the file and return it as a list of strings. Then split each word into letters
    # temp = [list(line) for line in txt_list]
    # print(temp)

    temp = [line.split() for line in txt_list]
    print(temp)
    
    counts = {'Darth' : 0, 'Lea' : 0, 'Luke' : 0}

    for line in txt_list:
        line = line.strip() # Removes the \n from the line (string)
        if line == 'Darth':
            counts['Darth'] += 1

        elif line == 'Luke':
            counts['Luke'] += 1

        elif line == 'Lea':
            counts['Lea'] += 1

    print(counts)

# Append your first name to the end of the list
with open(f"{dir_path}\star_wars.txt", 'a', encoding='utf-8') as f:
    # f.seek(0) - cursor goes to beginning of the file
    f.seek(0, os.SEEK_END) # makes sure that the cursor is at the end of the file
    f.write('\nNiv')
    print('Successfully Added')

# Append 'Skywalker' next to each first name Luke

modified_lines = []
for line in txt_list:
    if line.strip() == 'Luke':
        modified_lines.append('Luke Skywalker\n')
    else:
        modified_lines.append(line)

with open(f"{dir_path}\star_wars.txt", 'w', encoding='utf-8') as f:
    f.seek(0)
    f.writelines(modified_lines)