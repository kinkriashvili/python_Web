def bigger_Is_greater(word):
    index = 0
    for _ in range(word):
        try:
            b = my_list[index - 2]
            x = my_list[index - 1]
            if x > b:
                if x > my_list[index] and my_list[index] > b:
                    my_list[index - 1], my_list[index] = my_list[index], my_list[index - 1]
                    my_list[index - 1], my_list[index - 2] = my_list[index - 2], my_list[index - 1]
                    result_list.append(' '.join(my_list))
                    break
                else:
                    my_list[index - 1], my_list[index - 2] = my_list[index - 2], my_list[index - 1]
                    result_list.append(' '.join(my_list))
                    break
        except:
            result_list.append("no answer")
        index -= 1

num = int(input("Enter the number: "))
result_list = list()
for i in range(num):
    text = input("enter the word: ")
    my_list = list()
    for each in text:
        my_list.append(each)

    listlength = len(my_list)
    bigger_Is_greater(listlength)
print(num)
answer = ""
for each_value in result_list:
    if each_value == " ":
        continue
    for space_deleter in each_value:
        if space_deleter == " ":
            continue
        answer += space_deleter
    print(answer)
    answer = ""

