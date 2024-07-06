# making a variable and doing calculations with variable and printing out using variables in print in middle of sentences or strings, also doing maths calculation

cars = 100
space_in_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passenger_per_car = passengers / cars_driven

print ("there are", cars, "cars available")
print("there are only", drivers, "drivers available")
print("there will be", cars_not_driven, "empty cars today")
print("we can transport", carpool_capacity, "people today")
print("we have", passengers, "to carpool today.")
print("we need to put about", average_passenger_per_car, "in each car")

print("if we fill car with max capacity we would need", passengers / space_in_car ,"free cars")
