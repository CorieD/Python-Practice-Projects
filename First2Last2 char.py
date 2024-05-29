def both_ends(s):
    if len(s) < 2:
        return ''
    else:
        return s[:2] + s[-2:]

input_string = input("Enter a string: ")
result = both_ends(input_string)
print(result)
