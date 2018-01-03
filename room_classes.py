#!/usr/bin/python3

class Room():
	def __init__(self):
		pass


	class Penthouse(Room):
		def __init__(self, price, capacity):
			self.price = "$199.99/night"
			self.capacity = 8
		
		def display_info(self):
			print('Price: ' + self.price)
			print('Capacity: ' + self.capacity)
	
	class Family(Room):
		def __init__(self, price, capacity):
			self.price = "$69.99/night"
			self.capacity = 6
			
		def display_info(self):
			print('Price: ' + self.price)
			print('Capacity: ' + self.capacity)

	class Single(Room):
		def __init__(self, price, capacity):
			self.price = "$39.99/night"
			self.capacity = 2
			
		def display_info(self):
			print('Price: ' + self.price)
			print('Capacity: ' + self.capacity)

	class Budget(Room):
		def __init__(self, price, capacity):
			self.price = "$19.99/night)"
			self.capacity = 2
			
		def display_info(self):
			print('Price: ' + self.price)
			print('Capacity: ' + self.capacity)



		
