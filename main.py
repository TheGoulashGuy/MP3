#!/usr/bin/python3

import random
import sqlite3
import pickle

database_connection = sqlite3.connect('reservations.db')
cursor = database_connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS reservations (surname, room_type, room_number, occupants, date)')

print("\nWelcome!\n\n")

occupied_rooms = []

#This should only be run once--put in separate setup file
def initial_pickling():
	budget = [11,22,33,44,55,66,77,88,99]
	with open('budget.pickle','wb') as pickled_budget:
		pickle.dump(budget,pickled_budget)

	single = [100,102,104,106,108,110,112,114,116,118,120,124,128,130,132]
	with open('single.pickle','wb') as pickled_single:
		pickle.dump(single,pickled_single)

	family = [200,202,204,206,208,210,212,214,216]
	with open('family.pickle','wb') as pickled_family:
		pickle.dump(family,pickled_family)

	penthouse = [900,902,904,906,908,910]
	with open('penthouse.pickle','wb') as pickled_penthouse:
		pickle.dump(penthouse,pickled_penthouse)

	print("Done pickling!")
#initial_pickling()

#This function determines room number
def determine_room_number(x):
	with open(x+'.pickle','rb') as available_rooms_in:
		available_rooms = pickle.load(available_rooms_in)

	room_number = random.choice(available_rooms)
	available_rooms.remove(room_number)

	with open('occupied_rooms.pickle','wb') as occupied_rooms:
		pickle.dump(room_number,occupied_rooms)

	print(available_rooms)
	print(room_number)

#This function performs room reservation
def reserve_room():
	room_type = input("What is your preferred room type? (Budget, Single, Family, Penthouse)\n>>")
	room_type = room_type.lower()

	with open(room_type+'.pickle','rb') as available_rooms_in:
		available_rooms = pickle.load(available_rooms_in)

	room_number = random.choice(available_rooms)
	available_rooms.remove(room_number)

	with open('occupied_rooms.pickle','wb') as occupied_rooms:
		pickle.dump(room_number,occupied_rooms)

	print(available_rooms)
	print(room_number)
	occupants = input("How many occupants will be in the room?\n>>")
	surname = input("What is your name?\n>>")
	date = input("What is your reservation date? (MM/DD/YY-MM/DD/YY)\n>>")
	cursor.execute("INSERT INTO reservations VALUES(?, ?, ?, ?, ?)", (surname, room_type, room_number, occupants, date))
	database_connection.commit()
	print("Success! Your room number is " + str(room_number) + ".")

def display_sql_res_info():
	surname_to_search = input("Enter reservation name:\n>>")
	cursor.execute("SELECT * FROM reservations WHERE surname=(?)", (surname_to_search,))
	data = cursor.fetchone()
	if data:
		for row in data:
			print(row)
	else:
		print("No such record found.")

def reopen_room(y,z):
	with open(y+'.pickle','wb') as open_rooms:
		pickle.dump(z, open_rooms)

def delete_reservation(x):
	cursor.execute("SELECT room_number, room_type FROM reservations WHERE surname=?", (x,))
	data = cursor.fetchone()
	room_number_to_reopen = str(data[0])
	room_type_to_reopen = data[1]
	reopen_room(room_type_to_reopen, room_number_to_reopen)
	cursor.execute("DELETE FROM reservations WHERE surname=?", (x,))
	database_connection.commit()
	print("Successful deletion.")

def fetch_reservation_to_cancel():
	surname_to_search = input("Enter reservation name:\n>>")
	cursor.execute("SELECT * FROM reservations WHERE surname=?", (surname_to_search,))
	data = cursor.fetchone()
	if data:
		delete_reservation(surname_to_search)
	else:
		print("No such record found.")

def customer_check_out():
	name_to_check_out = input("Enter reservation name:\n>>")
	cursor.execute("SELECT room_number, room_type FROM reservations WHERE surname=(?)", (name_to_check_out,))
	data = cursor.fetchall()
	data = data[0]
	data = list(data)
	room_to_reopen = (data[0])
	room_type_to_reopen = (data[1])

	if room_type_to_reopen == 'budget':
		budget.append(room_to_reopen)

	elif room_type_to_reopen == 'single':
		single.append(room_to_reopen)

	elif room_type_to_reopen == 'family':
		family.append(room_to_reopen)

	elif room_type_to_reopen == 'penthouse':
		family.append(room_to_reopen)

	else:
		print("Error: Specified room type does not exist")

	delete_reservation(name_to_check_out)

def decide_action():
	potential_action = input("Which action would you like to perform?\n1 - Reserve a room\n2 - Display reservation information\n3 - Check out a customer\n4 - Cancel reservation\n>>")
	if int(potential_action) == 1:
		reserve_room()
	elif int(potential_action) == 2:
		display_sql_res_info()
	elif int(potential_action) == 3:
		fetch_reservation_to_cancel()
	elif int(potential_action) == 4:
		fetch_reservation_to_cancel()
	else:
		print("Error: Unrecognized option.")
		decide_action()
decide_action()
