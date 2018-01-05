#!/usr/bin/python3

import pdb
#import room_classes as rc
import reservation_class as reservation
import pickle
import random
#import available_rooms as ar
#List of available rooms
budget = [11,22,33,44,55,66,77,88,99]
single = [100,102,104,106,108,110,112,114,116,118,120,124,128,130,132]
family = [200,202,204,206,208,210,212,214,216]
penthouse = [900,902,904,906,908,910]

#These are the current reservations, sorted by surname (Reservation class instance names)
current_reservations = []

#This is the list of current unavailable rooms
occupied_rooms = []

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
		rc.Room.Penthouse.display_info()last
'''
print("Welcome!")

def determine_room_number(x):
	reservation_room_number = random.choice(eval(x))
	occupied_rooms.append(reservation_room_number)
	eval(x).remove(reservation_room_number)

#This function performs room reservation
def reserve_room():
	reservation_room_type = input("What is your preferred room type? (Budget, Single, Family, Penthouse)\n>>")
	reservation_room_type = reservation_room_type.lower()
	determine_room_number(reservation_room_type)
	reservation_room_number = occupied_rooms[-1]
	reservation_occupants = input("How many occupants will be in the room?\n>>")
	reservation_surname = input("What is your name?\n>>")
	reservation_date = input("What is your reservation date? (MM/DD/YY-MM/DD/YY)\n>>")
	current_reservations.append(reservation_surname)
	reservation_surname = reservation.Reservation(reservation_surname, reservation_room_type, reservation_room_number, reservation_occupants, reservation_date)
	print("Success! Your room number is " + str(reservation_room_number) + ".")

reserve_room()
