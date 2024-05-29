def donuts(count):
    if count >= 10:
        return 'Number of donuts: many'
    else: return 'Number of donuts: ' + str(count)

user_input = int(input('Enter the number of donuts: '))
num_donuts = donuts(user_input)
print(num_donuts)


