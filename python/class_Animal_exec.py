from class_animal import *

dog = Dog('doggy')
n = dog.name
print(n)
dog.move()
dog.speak()

duck = Duck('donald')
d = duck.name
print(d)
duck.move()
duck.speak()

zoo = [Dog('marry'), Duck('dduck')]

for z in zoo:
    print(z.name)
    z.speak()