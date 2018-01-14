#!/usr/bin/python3

import reservations as rs
import reservation_class
import random
import sqlite3

database_connection = sqlite3.connect('reservations.db')
cursor = database_connection.cursor()

budget = [11,22,33,44,55,66,77,88,99]
single = [100,102,104,106,108,110,112,114,116,118,120,124,128,130,132]
family = [200,202,204,206,208,210,212,214,216]
penthouse = [900,902,904,906,908,910]

print("Welcome!\n\n")

occupied_rooms = []

#This function determiens room number
def determine_room_number(x):
	room_number = random.choice(eval(x))
	occupied_rooms.append(room_number)
	eval(x).remove(room_number)

#This function performs room reservation
def reserve_room():
	room_type = input("What is your preferred room type? (Budget, Single, Family, Penthouse)\n>>")
	room_type = room_type.lower()
	determine_room_number(room_type)
	room_number = occupied_rooms[-1]
	occupants = input("How many occupants will be in the room?\n>>")
	surname = input("What is your name?\n>>")
	date = input("What is your reservation date? (MM/DD/YY-MM/DD/YY)\n>>")
	surname = reservation_class.Reservation(surname, room_type, room_number, occupants, date)
	rs.current_reservations.append(surname)
	print("Success! Your room number is " + str(room_number) + ".")
	print(rs.current_reservations[0].surname)
	cursor.execute("INSERT INTO reservations VALUES(?, ?, ?, ?, ?)", (surname, room_type, room_number, occupants, date))
	cursor.commit()
	cursor.close()
reserve_room()

def display_reservation_info():
	surname_to_search = input("Enter reservation name:\n>>")
	for x in rs.current_reservations:
		if x.surname == surname_to_search:
			x.display_info()
		else:
			pass
	#rs.current_reservations[surname_index].display_info()
display_reservation_info()
