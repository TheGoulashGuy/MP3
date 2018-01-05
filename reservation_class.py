#!/usr/bin/python3

class Reservation():
	def __init__(self, surname, room_type, room_number, occupants, date):
		self.surname = surname
		self.room_type = room_type
		self.room_number = room_number
		self.occupants = occupants
		self.date = date

	def display_info(self):
		print("Name: " + self.surname)
		print("Room Number: " + str(self.room_number))
		print("Room Type: " + self.room_type)
		print("Number of Occupants: " + self.occupants)
		print("Reservation Date: " + self.date)

