alien_color = 'green', 'yellow', 'red'
if 'green' in alien_color:
    print('You got 5 point!')
if alien_color == 'green':
    print('5')
elif alien_color == 'yellow':
    print('10')
else:
    print('15')

age = 65
if age < 2: print('Младенец')
elif age >= 2 and age <= 4: print('Малыш')
elif age >= 4 and age <= 13: print('Ребенок')
elif age >= 13 and age <= 20: print('Подросток')
elif age >= 20 and age < 65: print('Взрослый')
elif age >= 65: print('Пожилой')

names = ['John', 'Lucy', 'Mike_admin', 'Andrew', 'Nicolas']
if names:
    for login in names:
        if '_admin' in login:
            print(f'Hello {login}, would you like to see a status report?')
        else:
            print(f'Hello {login}, thank you for logging in again')
else:
    print('We need to ind some users!')

current_names = ['Kolya', 'Lucy', 'Mike', 'Andrew', 'Vasya']
new_users = 'John', 'Lucy', 'Mike', 'Andrew', 'Nicolas'
for available in new_users:
    if available in current_names:
        print('You need to make new name!')
    else:
        print('Good name :)')
        current_names.append(available)
print(f'Hello team{current_names}[fd[pf[pdsf')