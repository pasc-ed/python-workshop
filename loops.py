#!/Users/pascaledouard/.pyenv/shims/python

class Car:
    def __init__(self, color):
        self.color = color
    
    def set_color(self, color):
        self.color = color


my_first_car = Car("red")
my_second_car = Car("Blue")

print(my_first_car.color)
print(my_second_car.color)

my_first_car.set_color("Purple")
print(my_first_car.color)