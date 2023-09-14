def check(str):
    if "dog" in str.split():
        return True
    else:
        return False
print(check(input("Enter the string: ")))