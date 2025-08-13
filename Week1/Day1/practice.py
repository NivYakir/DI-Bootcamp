from deep_translator import GoogleTranslator
import os



dir_path = os.path.dirname(os.path.realpath(__file__))
my_file = f"{dir_path}/practice.txt"

with open(my_file, 'r', encoding='utf-8') as f:
    content = f.readlines()
    result = ''
    for line in content:
        translated = GoogleTranslator(source='auto', target='es').translate(line.strip())
        result += translated + '\n'
    
    print(result)
