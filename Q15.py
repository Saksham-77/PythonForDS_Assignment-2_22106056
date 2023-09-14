number_of_terms = int(input("Enter the number of terms: "))
sum1=0
for i in range (1, number_of_terms + 1):
    sum1 += int('2' * i)
print(sum1)