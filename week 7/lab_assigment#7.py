"""
Assignment six: Bubble sort using recursion
Submitted by Clara Manolache
Submitted: May 24, 2026
CWID: 20653756

Assignment 7: Adds print_filter() to prints a list of sensors that are active and inactive
and change_filter() that allows a user to activate a sensor or deactivate it. The change_filter()
is initiated through the menu prompt #3 choice. The change_filter() method will print the
filter list showing active or inactive states, and it will allow the user to turn a sensor on or off.

Assignment 6: This program is to practice list recursion and to understand bubble sort algorithm, and it's implement.
adds the recursive sort method

Assignment 4: Builds sensor list to use. Practice with tuples.

Assignment 3: This assignment adds code to build a menu and support it. The menu provides the interface that a user
 will use to interact with the program.

Assignment 2: This assignment adds code to prompt the user for a temperature in Celsius and then converts that
temperature to a specified different temperature unit.

Assignment 1: This program demonstrates printing lines of text to the screen

"""
def recursive_sort(list_to_sort, key):
    """
    Bubble sort a list of tuples by either the first or second element,
    first element if key == 0, second element if key == 1
    Uses recursion. Applied on sensor list
    """
    pass_list = list_to_sort.copy()
    swaps = False
    len_minus_one = len(list_to_sort) - 1
    for i in range (len_minus_one):
        if pass_list[i][key] > pass_list[i + 1][key]:
            pass_list[i], pass_list[i + 1] = pass_list[i + 1], pass_list[i]
            swaps = True
    if len_minus_one == 1 or not swaps:
        return pass_list
    final_list = recursive_sort(pass_list[0:len_minus_one], key)
    final_list.append(pass_list[-1])
    return final_list


def convert_units(celsius_value, units):
    """
    From lab assignment #2, takes in a celsius_value
    temperature and converts to fahrenheits or kelvin
    """
    if units == 0:
        return celsius_value
    elif units == 1:
        return celsius_value * 9/5 + 32
    elif units == 2:
        return celsius_value + 273.15
    else:
        return None


def print_menu():
    """
    Prints the menu
    """
    print("Main Menu\n---------\n"
        "1 - Process a new data file\n2 - Choose units\n3 - Edit room filter\n"
        "4 - Show summary statistics\n5 - Show temperature by date and time\n"
        "6 - Show histogram of temperatures\n7 - Quit")

def print_filter(sensor_list, filter_list):
    """
    Prints the list of filters and clarify which are active
    """
    for sensor in sensor_list:
        print(f"{sensor[0]}: {sensor[1]} " +
              ("[ACTIVE]" if (sensor[2] in filter_list) else ""))

def new_file(dataset):
    """
    Open a new file, if user chooses item 1
    """
    print("New File Function Called")


def choose_units():
    """
    Called if user choose item 2
    """
    print("Choose Units Function Called")


def change_filter(sensors, sensor_list, filter_list):
    """
    Called if user choose item 3. Updates filter list
    depending on user input. Toggles active/inactive
    for sensors on the list.
    """
    while True:
        print()
        print_filter(sensor_list, filter_list)
        room_number = input("\nType the sensor to toggle (e.g. 4201) or x to end ")
        if room_number == 'x':
            break
        sensor_id = sensors.get(room_number)
        if sensor_id is None:
            print ("Invalid Sensor")
            continue
        if sensor_id[1] in filter_list:
            filter_list.remove(sensor_id[1])
        else:
            filter_list.append(sensor_id[1])

def print_summary_statistics(dataset, active_sensors):
    """
    Called if user choose item 4
    """
    print("Print Summary Statistics Function Called")


def print_temp_by_day_time(dataset, active_sensors):
    """
    Called if user choose item 5
    """
    print("Print Temp By Day/Time Function Called")


def print_histogram(dataset, active_sensors):
    """
    Called if user choose item 6
    """
    print("Print Histogram Function Called")


def main():
    """
    Builds data structures required for the program
    and provides the unit test code
    """
    sensors = {
        "4213": ("STEM Center", 0),
        "4201": ("Foundations Lab", 1),
        "4204": ("CS Lab", 2),
        "4218": ("Workshop Room", 3),
        "4205": ("Tiled Room", 4),
        "Out": ("Outside", 5)
    }
    sensor_list = [(room, data[0], data[1]) for room, data in sensors.items()]
    filter_list = [(data[1]) for data in sensors.values()]

    sensor_list = recursive_sort(sensor_list, 0)
    # prompting the user
    while True:
        print()
        print_menu()
        choice = input("What is your choice? ")
        try:
            choice = int(choice)
        except:
            print("Please enter an integer")
            continue
        if choice == 1:
            new_file(None)
        elif choice == 2:
            choose_units()
        elif choice == 3:
            change_filter(sensors, sensor_list, filter_list)
        elif choice == 4:
            print_summary_statistics(None, None)
        elif choice == 5:
            print_temp_by_day_time(None, None)
        elif choice == 6:
            print_histogram(None, None)
        elif choice == 7:
            exit()
        else:
            print("Invalid Choice, please enter an integer between 1 and 7.")


if __name__ == "__main__":
    main()

'''
/usr/bin/python3 /Users/claramanolache/FoothillCS3A/week 7/lab_assigment#7.py 

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
What is your choice? 3

4201: Foundations Lab [ACTIVE]
4204: CS Lab [ACTIVE]
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor to toggle (e.g. 4201) or x to end 4201

4201: Foundations Lab 
4204: CS Lab [ACTIVE]
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor to toggle (e.g. 4201) or x to end 4205

4201: Foundations Lab 
4204: CS Lab [ACTIVE]
4205: Tiled Room 
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor to toggle (e.g. 4201) or x to end Out

4201: Foundations Lab 
4204: CS Lab [ACTIVE]
4205: Tiled Room 
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside 

Type the sensor to toggle (e.g. 4201) or x to end Out

4201: Foundations Lab 
4204: CS Lab [ACTIVE]
4205: Tiled Room 
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor to toggle (e.g. 4201) or x to end 4201

4201: Foundations Lab [ACTIVE]
4204: CS Lab [ACTIVE]
4205: Tiled Room 
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor to toggle (e.g. 4201) or x to end 4000
Invalid Sensor

4201: Foundations Lab [ACTIVE]
4204: CS Lab [ACTIVE]
4205: Tiled Room 
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor to toggle (e.g. 4201) or x to end x

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
What is your choice? 7

Process finished with exit code 0

'''