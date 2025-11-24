Project Overview
This project is a simple Hotel Room Management System implemented in Python, allowing users to initialize rooms for a hotel, set room prices, dynamically add or remove rooms, and manage basic details about room status and customers. The system uses a combination of dictionaries, lists, and NumPy arrays for efficient data handling.

Key Features
Room Numbering & Initialization: Rooms are organized by floors and numbers (e.g., 101, 102 for floor 1).

Dynamic Modification: Users can add or remove rooms interactively.

Customer & Rental Information: Each room holds a dictionary to store customer details, occupancy status, billing, and other relevant data.

Simple User Interface: Console-based prompts guide the user through initializing and updating the room list.

Workflow and Code Explanation
Library Imports

python
import random
import numpy as np
These are used for future extensions (e.g., random assignments, array operations).

Data Structures

main_dict = {}: Stores all room data indexed by room number as strings.

all_rooms = []: Tracks the current valid room numbers.

Initialization Function

python
def rooms_intializing(floor, room):
It creates, modifies, and displays the set of rooms on each floor, based on user input.

Room Creation & Numbering

Rooms are numbered as floor*100 + room_number for easy identification (e.g., floor 1, room 1 → 101).

python
i = 0
while (i <= floor):
    j = 1
    print("In Floor", i, end="\t")
    while(j <= room):
        r = i*100 + j
        print(r, end=" ")
        all_rooms.append(r)
        j += 1
    print()
    i += 1


    Conclusion
This project provides a foundation for a simple hotel management application. The modular structure makes it easy to extend for real-world use, with further improvements possible in error handling, persistent storage, and user interface design.

References:

[Basic hotel management with Python - Stack Overflow]

[NumPy and Python dictionaries documentation]
