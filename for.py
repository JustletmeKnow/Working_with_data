number = [i**3 for i in range(1,11)]
print(number)
sad = [1, 2, 3, 4, 5, 6]
pizza = sad[:]
sad.append('pepperoni')
pizza.append('loxina')
print(sad)
print(pizza)
print(f"The first{sad[-3:]}")