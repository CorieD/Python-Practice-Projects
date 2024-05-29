
def mix_up(a, b):
    swapped_a = b[:2] + a[2:]
    swapped_b = a[:2] + b[2:]
    return swapped_a + ' ' + swapped_b


while True:

    
    first_word = input("Enter first word: ")

    if first_word == 'quit':
        break

    second_word = input("Enter second word: ")
    
    if second_word == 'quit':
        break

    
    
    
    
    result = mix_up(first_word, second_word)
    print("Swapped word: ", result)

