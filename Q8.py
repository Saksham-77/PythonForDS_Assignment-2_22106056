seq = ['soup', 'dog', 'salad', 'cat', 'great']
l = filter(lambda _: _.lower()[0] != "s", seq)
print(list(l))