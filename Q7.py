def count(str):
    splt = str.split()
    cnt = 0
    for i in splt:
        if i.lower() in ["dog", "dog,", "dog."]:
            cnt += 1
    print("The number of times the word dog has occurred in the given string is", cnt, ".")
count(input("Enter the string: "))