#!/usr/bin/python3

import room_classes as rc
import pickle

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

print("Welcome!")
occupants_quantity = input("Please specify the number of occupants you would like to reserve rooms for: ")
recommendRoom(occupants_quantity)


