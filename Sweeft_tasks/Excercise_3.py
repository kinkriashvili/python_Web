import random
text = ''
new_text = ''
for i in range(3):
    for j in range(4):
        text += '. '
    text += '\n'
    for k in range(4):
        char = random.choice('.O')
        new_text += (char + ' ')
    new_text += '\n'

print(new_text.replace('. ', 'O '))

