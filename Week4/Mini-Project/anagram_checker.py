import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/sowpods.txt', 'r', encoding='utf-8') as f:
    txt_list = f.readlines()

