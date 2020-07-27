import re

file_handler = open("Data.txt", 'r')
list_of_digits = []
for line in file_handler:
    if line.isdigit:
        digits = re.findall('([0-9]+)', line)
        for digit in digits:
            digit = int(digit)
            list_of_digits.append(digit)

    else:
        continue
print(list_of_digits)
print(sum(list_of_digits))
