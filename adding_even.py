target = int(input("Enter a number between 0 and 1000\n"))

sum_even_numbers = 0

for number in range(0, target + 1, 2):
    sum_even_numbers += number
    
print(sum_even_numbers)