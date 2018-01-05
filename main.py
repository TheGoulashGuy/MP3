#!/usr/bin/python3

import room_classes as rc
import reservation_class as reservation
import pickle
import random
import available_rooms as ar

#This is the list of current unavailable rooms
occupied_budget_rooms = []
occupied_single_rooms = []
occupied_family_rooms = []
occupied_penthouses = []

'''
def recommendRoom(x):
	if x <= 2:
		print("We recommend the Single Bed Suite.")
		rc.Room.Single.display_info()
		print("We also have Budget Rooms available.")
	elif x > 2 and x < 8:
		print("We recommend the Family Suite.")
		rc.Room.Family.display_info()
	elif x >= 8:
		print("We recommend the Penthouse Suite.")
		rc.Room.Penthouse.display_info()
'''
print("Welcome!")

#This function performs room reservation
def reserve_room():

	def determine_room_number(x):
		if x == 'budget':
			occupied_budget_rooms.append(reservation_room_number)

		elif x == 'single':
			occupied_single_rooms.append(reservation_room_number)

		elif x == 'family':
			occupied_family_rooms.append(reservation_room_number)

	reservation_surname = input("What is your name?\n>>")
	reservation_room_type = input("What is your preferred room type?\n>>")
	determine_room_number(reservation_room_type)
	reservation_occupants = input("How many occupants will be in the room?\n>>")
	reservation_date = input("What is your reservation date? (MM/DD/YY-MM/DD/YY)\n>>")
