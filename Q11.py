list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = []
for _ in list1:
    for i in list2:
        list3.append(_ + i)
print(list3)