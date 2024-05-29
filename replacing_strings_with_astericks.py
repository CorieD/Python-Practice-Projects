def fix_start(s):
    
    first_char = s[0]
    modified_string = first_char + s[1:].replace(first_char, '*')
    return modified_string



while True:
    user_input = input("Enter a string (or type 'quit' to exit): ")

    if user_input == 'quit':
        break

    result = fix_start(user_input)
    print("Modified string:", result)
    
    
    




    
