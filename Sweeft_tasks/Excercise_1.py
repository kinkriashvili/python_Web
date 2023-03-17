my_list = []
num = int(input('Enter the number: \n'))
count = 1
whole_word = ''
how_many = int(input('How many word do you want to enter: '))
for _ in  range(how_many):
    word = input('Enter the word: \n')
    whole_word += word
    my_list.append(word)
    count += 1
if len(whole_word) < pow(10, 6) and count <= pow(10, 5) and whole_word.islower():
    unique_word = set(my_list)
    length = len(unique_word)
    print(length)
    my_dict = {}
    for each in my_list:
        if each in my_dict:
            my_dict[each] += 1
        else:
            my_dict[each] = 1
    for each in my_dict:
        print(my_dict.get(each), end=' ')

