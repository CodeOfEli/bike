class Bicycle(object): 
	def __init__(self, model, weight, cost): 
		self.model = model
		self.weight = weight
		self.cost = cost

	def __str__(self): 
		return "The Bike is Called: {}".format(self.model)


class BikeShop: 
	def __init__(self, name, profit): #, inventory={}, margin="", profit=""): 
		self.name = name
		#self.inventory = inventory
		#self.margin = margin
		self.profit = profit
		#super(BikeShop, self).__init__("model1", "weight1", 200)

	def bike_margin(self, cost): 
		margin = cost * .20
		return margin 
		profit.append(margin)
		print profit


	def sales_price(self, cost, margin): 
		sales_price = cost + margin  
		return sales_price





class Customer(object): 
	def __init__(self, name, bank_account, consumer_status): 
		self.name = name
		self.bank_account = bank_account
		self.consumer_status = consumer_status
	#def spending_spree(self): 
		#return consumer_status = False

	def afford(self): #, bike_cost_dict):	

		bike_store_dict = {
									bike_one.model : bike_one.cost, 
									bike_two.model : bike_two.cost,
									bike_three.model : bike_three.cost,
									bike_four.model : bike_four.cost,
									bike_five.model : bike_five.cost,
									bike_six.model : bike_six.cost,
									}

		shopping_cart = {}
		wish_list = []

		for key, value in bike_store_dict.iteritems():
			if self.bank_account > value: 
				#shopping_cart.append(key:value)
				shopping_cart[key] = value
			
				print "{} can afford the {} bike which costs {}".format(self.name, key, value)
			else: 
				wish_list.append(key)
		#print "The total for all the bikes {} can afford is {}".format(self.name, sum(shopping_cart))
		print "There are {} bikes that {} can not yet afford.".format(len(wish_list), self.name)
		for bike in wish_list: 
			print "{}'s wish list includes the {}".format(self.name, bike)

		only_shopping_cart_values = []
		only_shopping_cart_keys = []

		#shopping_cart.sort() 

		if len(shopping_cart) >= 1:
			for key, value in shopping_cart.iteritems():
				only_shopping_cart_keys.append(key) 
				only_shopping_cart_values.append(value)
			
			only_shopping_cart_keys.sort()
			only_shopping_cart_values.sort()

			purchased_bike = only_shopping_cart_keys.pop()
			purchased_bike_price = only_shopping_cart_values.pop()
			balance = self.bank_account - purchased_bike_price
			#purchased_bike = shopping_cart.remove["key"]
			#self.bank_account = self.bank_account - 
			print "{} has purchased the {} for {} and now has ${} left.".format(self.name, purchased_bike, purchased_bike_price, balance) 
			return {purchased_bike : purchased_bike_price}



	#def purchase(self): 


	def __str__(self): 
		return "Customer Name is: {}".format(self.name)

	#def bike_shop(self, cost): 



# Create the Bike Shop Object: 
mikes_bikes = BikeShop("Mike's Bikes", [0])


# Create the Six Bike Objects: 
# 200 - 500 - 1000
bike_one = Bicycle("First Bike", "20 lbs", 199) # model name, weight, cost
bike_two = Bicycle("Second Bike", "10 lbs", 499)
bike_three = Bicycle("Third Bike", "15 lbs", 999)
bike_four = Bicycle("Fourth Bike", "5 lbs", 1001)
bike_five = Bicycle("Fifth Bike", "8 lbs", 1500)
bike_six = Bicycle("Sixth Bike", "13 lbs", 2000)

#print mikes_bikes.bike_margin(bike_one.cost)

print mikes_bikes.bike_margin(bike_one.cost)
print mikes_bikes.bike_margin(bike_two.cost)

# I could not iterate over the BIKE objects, so I created a dicitonary for now:
# bike_store_dict = {
# 									bike_one.model : bike_one.cost, 
# 									bike_two.model : bike_two.cost,
# 									bike_three.model : bike_three.cost,
# 									bike_four.model : bike_four.cost,
# 									bike_five.model : bike_five.cost,
# 									bike_six.model : bike_six.cost,
# 									}

dave = Customer("Mike", 200.00, True)
print dave.bank_account
#print mike.afford(bike_store_dict)
daves_bike = dave.afford()
print daves_bike

print "*********************************************************************"

tony = Customer("Tony", 500.00, True)
print tony
tonys_bike = tony.afford()


print "*********************************************************************"

angela = Customer("Angela", 1000.00, True)
print angela
angelas_bike = angela.afford()  



print "*********************************************************************"


total_cost = {}
total_cost.update(angelas_bike)
total_cost.update(tonys_bike)
total_cost.update(daves_bike)
print total_cost

#{'Third Bike': 999, 'Second Bike': 499, 'First Bike': 199}

total_sales = total_cost['Third Bike'] + total_cost['Second Bike'] + total_cost['First Bike']

print "Total Sales on 3 bikes was ${}".format(total_sales)


















