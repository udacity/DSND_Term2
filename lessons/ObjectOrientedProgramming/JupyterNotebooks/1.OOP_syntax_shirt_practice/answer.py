### TODO:
#    - import the Shirt class from the shirt.py file
###

from shirt import Shirt


### TODO:
#    - insantiate a shirt object with the following characteristics:
#        - color red, size S, style long-sleeve, and price 25
#    - store the object in a variable called shirt_one
#
#
###
shirt_one = Shirt('red', 'S', 'long-sleeve', 25)


### TODO:
#     - print the price of the shirt using the price attribute
#     - change the price of the shirt to be 10
#     - print the price of the shirt using the price attribute
#     - print the price of the shirt with a 12% discount
#
###
print(shirt_one.price)
shirt_one.change_price(10)
print(shirt_one.price)
print(shirt_one.discount(.12))


### TODO:
#
#    - instantiate another object with the following characteristics:
# .       - color orange, size large, style short sleeve, and price 10
#    - store the object in a variable called shirt_two
#
###
shirt_two = Shirt('orange', 'L', 'short-sleeve', 10)


### TODO:
#
#    - calculate the total cost of shirt_one and shirt_two
#    - store the results in a variable called total
#    
###
total = shirt_one.price + shirt_two.price


### TODO:
#
#    - use the shirt discount method to calculate the total cost if
#       shirt_one has a discount of 14% and shirt_two has a discount
#       of 6%
#    - store the results in a variable called total_discount
###
total_discount =  shirt_one.discount(.14) + shirt_two.discount(.06) 