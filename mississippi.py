def most_frequent(word):
    letter = dict()
    for i in word:
        if i in letter:
            letter[i] += 1
        else:
            letter[i] = 1
    sorted_list = dict(sorted(letter.items(), key=lambda x: x[1], reverse=True))
    for i in sorted_list:
        print(i, end=" : ")
        print(sorted_list[i])
string=str(input("enter the string: "))
print(most_frequent(string))


