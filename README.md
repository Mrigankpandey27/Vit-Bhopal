Purpose:
This Python program provides a command-line system for managing hotel room allocation, guest check-in/check-out, pricing, and reservation details using basic user prompts and data storage in dictionaries.

Features:
Initialize rooms by floor and room count, with custom pricing options

Add new rooms or remove unavailable rooms after initial setup

Assign, check in, extend the stay, or check out guests from rooms

Maintain detailed records per room: customer info, dates, contact, ID verification, outstanding balances, and pricing

Full audit trail for price adjustment per room

Requirements:
Python 3.x (tested with Python 3.6+)

NumPy library (for room number array manipulation)

Initialize Rooms:

You’ll be prompted for the number of floors and rooms per floor.

Enter a default price for rooms, customize individual room prices if desired.

Room Customization:

Add or remove rooms as necessary after initial setup.

Menu Operations:

Check in new guests (with room preference handling).

Extend a guest’s stay and manage outstanding payments.

Check out guests, update room status, and handle date extensions.

Access room details for occupancy, customer, and pricing info.

Example:

Start: Input floors (e.g., 3) and rooms per floor (e.g., 10)

Enter price, set up, add/remove rooms

Check in “Alice,” assign room and enter details

Access or modify room, extend guest stay, handle payments, and perform check-outs

Program Structure:

rooms_intializing(floor, room): Initiates room data, adds/removes rooms, sets prices

Main loop provides menu choices to manage operational tasks

License:
This project is free to use and modify for educational or operational hotel management purposes.
