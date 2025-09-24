# TODO: Complete the function 
def get_expected_cost(beds, baths):
    value = 80000+beds*30000+ baths*10000
    return value
  
#Option 1: house with two bedrooms and three bathrooms
# Option 2: house with three bedrooms and two bathrooms
# Option 3: house with three bedrooms and three bathrooms
#Option 4: house with three bedrooms and four bathrooms


option_one = get_expected_cost(2, 3)
option_two = get_expected_cost(3, 2)
option_three = get_expected_cost(3, 3)
option_four = get_expected_cost(3, 4)
    
print(option_one)
print(option_two)
print(option_three)
print(option_four)

#Decorating the walls
#sqft_walls = total square feet of walls to be painted
#sqft_ceiling = square feet of ceiling to be painted
#sqft_per_gallon = number of square feet that you can cover with one gallon of paint
#cost_per_gallon = cost (in dollars) of one gallon of paint
def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    cost = ((sqft_walls+sqft_ceiling)/sqft_per_gallon) * cost_per_gallon
    return cost
  
#432 square feet of walls, and144 square feet of ceiling.
#one gallon of paint covers 400 square feet and costs $15
project_cost = get_cost(432,144,400,15)

#to integer avoid point values
def get_actual_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft = sqft_walls + sqft_ceiling
    gallons_needed = total_sqft / sqft_per_gallon
    gallons_to_buy = math.ceil(gallons_needed)
    cost = cost_per_gallon * gallons_to_buy
    return cost
