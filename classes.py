class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print(f'Restaurant {self.restaurant_name} is open now!')

    def number_served_update(self, counter):
        self.number_served = counter

    def increment_number_served(self, number):
        self.number_served += number

    def reset_number_served(self):
        self.number_served = 0


restaurant = Restaurant('BOMZHI', 'rusian)')

restaurant.open_restaurant()

print(restaurant.number_served)
restaurant.number_served_update(100)
print(restaurant.number_served)
restaurant.increment_number_served(52)
print(restaurant.number_served)
restaurant.reset_number_served()
print(restaurant.number_served)

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)


    def show_flavors(self, *args, **flavors):
        flavors['1st'] = args
        return flavors

IceCreamStand = IceCreamStand('bomz', 'old')
print(IceCreamStand.show_flavors('chock', 'milk'))


class Admin(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.privilege = Privileges()


class Privileges():

    def __init__(self, privilege=''):
        self.privilege = privilege

    def show_privileges(self, privilege):
        print(f'You have this permissions: {privilege}')



Admin = Admin('golova', 'golub')
Admin.privilege.show_privileges(privilege='разрешено добавлять сообщения')