Human = {'first_name': 'Elizabeth',
         'middle_name': 'Vladislavovna',
         'last_name': 'Eliz',
         'age': '20',
         'city': 'Harkiv'}
print(Human['first_name'], Human['middle_name'], Human['last_name'], Human['age'], Human['city'])


Humans_1 = {'vitaliy': 'fd'}
Humans_2 = {'evgeniy': 'fds'}
Humans_3 = {'andrey': 'fdsa'}
people = [Humans_1, Humans_2, Humans_3]
for k in people:
    print(k)

def favorite_book(title, size='L'):
    print(f'My favorite book is {title.title()} {size}')

favorite_book('M')

def get_formatted_name(first_name, last_name, middle_name='L'):
    full_name = {'first': first_name, 'middle': middle_name, 'last': last_name}
    return full_name

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

def show_messages(unprinted_messages):
    while unprinted_messages:
        if len(unprinted_messages) >= 1:
            print(unprinted_messages)
        break

def showed_messages(unprinted_messages, printed_messages):
    while unprinted_messages:
        current_message = unprinted_messages.pop()
        printed_messages.append(current_message)
    print(unprinted_messages, printed_messages)

def burgers(*tops):
    for topss in tops:
        print(topss)

def burgers_build(dish, **tops):
    tops['dish'] = dish
    return tops

def make_car(*args, color='blue', **cars):
    cars['name_car'] = args
    cars['type_name'] = args
    cars['color'] = color
    return cars


messages = ['piska', 'popka', 'jopka', 'siska']
send_messages = []


show_messages(messages)
showed_messages(messages[:], send_messages)
burgers('ka', 'pis')

burger_profile = burgers_build('borsch', jopka='piska', piska='jopka')
print(burger_profile)

car = make_car('Audi', 'RS7', liftback= 'False')
print(car)