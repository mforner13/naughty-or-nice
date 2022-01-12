import names

list_of_names = [names.get_full_name() for i in range(10)]

print('whole list of names:', list_of_names)

naughty_list = []
nice_list = []

def check_if_duplicate(name):
    first_name = name.split()[0]
    for char in first_name: 
        if first_name.count(char) > 1:
            return True
    return False

def check_if_greater_than_5(name):
    last_name = name.split()[1]
    return len(last_name) > 5
    
for name in list_of_names: # each full name
    if check_if_duplicate(name):
        naughty_list.append(name)
    elif check_if_greater_than_5(name):
        naughty_list.append(name)
    else: 
        nice_list.append(name)

print('Naughty list:', naughty_list)
print('Nice list:', nice_list)
print('hi')
