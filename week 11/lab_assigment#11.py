"""
Assignment nine: Reading and using the contents of a file
Submitted by Clara Manolache
Submitted: June 14, 2026
CWID: 20653756

Assigment 11: Practice using the Pandas libary and implemented the 5th option (average temperature by day and time).

Assignment 10: implemented the choose unit function for practice with  global variables.

Assigment 9: practice reading files and implement new_file methode. Use two of the instance methods from TempDataset
 class.

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
import pandas as pd
from TempDataset import TempDataset
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
    file = input("Please enter the filename of the new dataset: ")

    # Checks if file is avaliable
    if not dataset.process_file(file):
        print("Unable to load file.")
        return

    # Displays info about file
    print(f"Loaded {dataset.get_loaded_temps()} samples\n")
    file_name = ''

    # Prompting user for name until valid
    while (True):
        file_name = input("Please provide a 3 to 20 character name for the dataset: ")
        try:
            dataset.name = file_name
        except ValueError:
            print("Invalid name. Please try again.\n")
            continue
        break

# Global constant variable
UNITS = {
    0: ("Celsius", "C"),
    1: ("Fahrenheit", "F"),
    2: ("Kelvin", "K"),
}

# Global variable
current_unit = 0

def choose_units():
    """
    Lets user choose a new unit for temperatures.
    Options from global constant UNITS dictionary.
    Change stored in global variable current_unit.
    """
    global current_unit

    # Report current Unit
    print(f"\nCurrent unit in {UNITS[current_unit][0]}\n")

    # Give menu and ask user to choose new unit
    while True:
        print("Choose a new unit:")
        for unit in UNITS:
            print(f"{unit} - {UNITS[unit][0]}")
        print()
        choice = input("Which unit? ")

        # Make sure it is valid selection
        try:
            choice = int(choice)
            if choice in UNITS:
                current_unit = choice
                break
            else:
                print("*** Please choose a unit from the list ***\n")
        except ValueError:
            print("*** Please enter a number only ***\n")


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
    Called if user choose item 4, uses method from TempDataset
    to print min, max, and average temperatures.
    """
    results = dataset.get_summary_statistics(active_sensors)
    if results is None:
        print("Please load data file and make sure at least one sensor is active")
        return

    results = tuple(convert_units(float(value), current_unit) for value in results)
    print("\nSummary statistics for Test Week")
    print(f"Minimum Temperature: {results[0]:.2f} {UNITS[current_unit][1]}\n"
          f"Maximum Temperature: {results[1]:.2f} {UNITS[current_unit][1]}\n"
          f"Average Temperature: {results[2]:.2f} {UNITS[current_unit][1]}\n")


# constants for day/time

DAYS = {
    0 : "SUN",
    1 : "MON",
    2 : "TUE",
    3 : "WED",
    4 : "THU",
    5 : "FRI",
    6 : "SAT"
}

HOURS = {
    0 : "Mid-1AM  ",
    1 : "1AM-2AM  ",
    2 : "2AM-3AM  ",
    3 : "3AM-4AM  ",
    4 : "4AM-5AM  ",
    5 : "5AM-6AM  ",
    6 : "6AM-7AM  ",
    7 : "7AM-8AM  ",
    8 : "8AM-9AM  ",
    9 : "9AM-10AM ",
    10 : "10AM-11AM",
    11 : "11AM-NOON",
    12 : "NOON-1PM ",
    13 : "1PM-2PM  ",
    14 : "2PM-3PM  ",
    15 : "3PM-4PM  ",
    16 : "4PM-5PM  ",
    17 : "5PM-6PM  ",
    18 : "6PM-7PM  ",
    19 : "7PM-8PM  ",
    20 : "8PM-9PM  ",
    21 : "9PM-10PM ",
    22 : "10PM-11PM",
    23 : "11PM-MID ",
}


def print_temp_by_day_time(dataset, active_sensors):
    """
    Called if the user chooses item 5. Uses Pandas to create a DataFrame that stores
    average temperatures for each day and time of day. Uses DAYS and HOURS constants
    to create the row and col labels. Rounds to 1 decimal place.
    """
    temps = dataset.get_loaded_temps()
    if temps is None:
        print("Please load data file and make sure at least one sensor is active")
        return
    data_avg = dict()
    for days in DAYS:
        hours_avg = []
        for hours in HOURS:
            temp = dataset.get_avg_temperature_day_time(active_sensors, days, hours)
            hours_avg.append(convert_units(temp, current_unit))
        data_avg[days] = hours_avg
    df = pd.DataFrame(data_avg)
    df.rename(index=HOURS, inplace=True)
    df.rename(columns=DAYS, inplace=True)
    df = df.round(1)
    print(f"\nAverage Temperatures for {dataset.name}\n"
          f"Units are in {UNITS[current_unit][0]}\n")
    print(df)

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
    current_set = TempDataset()
    # prompting the user
    while True:
        print()
        print_menu()
        #print(current_set.get_avg_temperature_day_time(filter_list, 5, 7))  # for testing
        choice = input("What is your choice? ")
        if choice == '1':
            print()
            new_file(current_set)
        elif choice == '2':
            choose_units()
        elif choice == '3':
            change_filter(sensors, sensor_list, filter_list)
        elif choice == '4':
            print_summary_statistics(current_set, filter_list)
        elif choice == '5':
            print_temp_by_day_time(current_set, filter_list)
        elif choice == '6':
            print_histogram(current_set, filter_list)
        elif choice == '7':
            exit()
        else:
            print("Invalid Choice, please enter an integer between 1 and 7.")

if __name__ == "__main__":
    main()

'''
UNIT TESTING: 

/Users/claramanolache/FoothillCS3A/.venv/bin/python /Users/claramanolache/FoothillCS3A/week 11/lab_assigment#11.py 

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
What is your choice? 1

Please enter the filename of the new dataset: /Users/claramanolache/FoothillCS3A/resources/Temperatures_2025-11-07.csv
Loaded 11724 samples

Please provide a 3 to 20 character name for the dataset: test name

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
What is your choice? 5

Average Temperatures for test name
Units are in Celsius

            SUN   MON   TUE   WED   THU   FRI   SAT
Mid-1AM    21.1  20.6  21.7  21.5  21.0  21.1  19.8
1AM-2AM    21.1  20.5  21.6  21.5  20.9  21.1  19.9
2AM-3AM    21.1  20.4  21.5  21.4  20.9  21.1  19.8
3AM-4AM    21.1  20.4  21.4  21.3  20.8  21.0  19.8
4AM-5AM    21.1  20.4  21.4  21.2  20.8  21.0  19.9
5AM-6AM    21.0  20.2  21.4  21.2  20.7  20.8  19.8
6AM-7AM    20.9  19.9  21.3  21.0  20.6  20.6  19.8
7AM-8AM    20.7  20.0  21.1  20.9  20.6  20.5  19.9
8AM-9AM    20.6  20.2  21.2  20.8  20.7  20.3  19.9
9AM-10AM   20.9  21.1  22.0  20.9  21.2  20.2  20.2
10AM-11AM  21.2  21.9  22.8  21.5  22.1  20.4  20.6
11AM-NOON  21.5  22.6  23.4  22.2  22.7  20.7  20.8
NOON-1PM   21.6  23.0  23.9  22.6  23.0  21.0  21.0
1PM-2PM    21.7  23.3  24.0  23.1  23.2  21.0  21.0
2PM-3PM    21.9  23.6  24.2  23.5  23.3  21.1  21.0
3PM-4PM    21.9  24.0  24.4  23.6  23.5  21.1  20.8
4PM-5PM    21.7  24.2  24.5  23.8  23.6  21.0  20.9
5PM-6PM    21.6  24.1  24.4  23.7  23.7  20.8  20.9
6PM-7PM    21.5  23.4  23.9  23.4  23.2  20.7  20.7
7PM-8PM    21.4  23.0  23.2  22.8  22.3  20.3  20.5
8PM-9PM    21.2  22.6  22.3  22.1  21.6  19.8  20.2
9PM-10PM   21.0  22.3  21.8  21.7  21.2  19.7  19.9
10PM-11PM  20.8  22.0  21.7  21.5  21.2  19.8  19.8
11PM-MID   20.8  21.9  21.6  21.2  21.1  19.8  19.7

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

Type the sensor to toggle (e.g. 4201) or x to end 4204

4201: Foundations Lab 
4204: CS Lab 
4205: Tiled Room [ACTIVE]
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor to toggle (e.g. 4201) or x to end 4205

4201: Foundations Lab 
4204: CS Lab 
4205: Tiled Room 
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside [ACTIVE]

Type the sensor to toggle (e.g. 4201) or x to end Out

4201: Foundations Lab 
4204: CS Lab 
4205: Tiled Room 
4213: STEM Center [ACTIVE]
4218: Workshop Room [ACTIVE]
Out: Outside 

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
What is your choice? 5

Average Temperatures for test name
Units are in Celsius

            SUN   MON   TUE   WED   THU   FRI   SAT
Mid-1AM    20.4  20.2  22.6  21.8  21.4  21.5  19.3
1AM-2AM    20.5  20.2  22.5  21.7  21.3  21.4  19.4
2AM-3AM    20.6  20.1  22.4  21.6  21.1  21.3  19.4
3AM-4AM    20.7  20.0  22.3  21.5  21.0  21.3  19.5
4AM-5AM    20.7  20.0  22.3  21.4  20.9  21.2  19.5
5AM-6AM    20.7  20.0  22.3  21.4  20.9  21.1  19.5
6AM-7AM    20.4  20.0  22.3  21.2  20.8  20.9  19.5
7AM-8AM    20.1  20.1  22.1  21.1  20.9  20.6  19.5
8AM-9AM    19.7  20.1  21.7  20.9  20.9  20.2  19.5
9AM-10AM   19.6  20.6  22.0  20.8  21.5  19.5  19.6
10AM-11AM  19.5  21.3  22.4  21.0  22.0  19.2  19.5
11AM-NOON  19.4  21.6  22.9  21.3  22.3  19.2  19.2
NOON-1PM   19.3  21.8  22.8  21.8  22.3  19.1  18.8
1PM-2PM    19.3  22.2  23.1  22.4  22.2  18.9  18.6
2PM-3PM    19.4  22.7  23.5  22.8  22.4  18.9  18.5
3PM-4PM    19.3  22.9  23.7  23.3  22.6  18.9  18.4
4PM-5PM    19.3  23.2  24.0  23.6  23.0  18.9  18.3
5PM-6PM    19.3  23.4  24.3  23.8  23.4  18.9  18.3
6PM-7PM    19.3  23.0  24.0  23.7  23.0  18.8  18.2
7PM-8PM    19.6  23.0  23.4  23.0  22.5  18.7  18.2
8PM-9PM    19.9  23.0  22.8  22.5  22.0  18.5  18.2
9PM-10PM   20.1  23.0  22.3  22.0  21.7  18.6  18.3
10PM-11PM  20.2  22.9  22.1  21.8  21.6  19.0  18.6
11PM-MID   20.3  22.8  22.0  21.6  21.5  19.2  18.7

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
What is your choice? 2

Current unit in Celsius

Choose a new unit:
0 - Celsius
1 - Fahrenheit
2 - Kelvin

Which unit? 1

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
What is your choice? 5

Average Temperatures for test name
Units are in Fahrenheit

            SUN   MON   TUE   WED   THU   FRI   SAT
Mid-1AM    68.8  68.4  72.7  71.3  70.6  70.7  66.8
1AM-2AM    69.0  68.3  72.5  71.1  70.3  70.5  66.9
2AM-3AM    69.1  68.3  72.3  70.9  70.0  70.4  67.0
3AM-4AM    69.2  68.1  72.2  70.8  69.8  70.3  67.0
4AM-5AM    69.2  68.1  72.1  70.6  69.7  70.1  67.1
5AM-6AM    69.2  68.0  72.1  70.5  69.6  70.0  67.1
6AM-7AM    68.8  67.9  72.1  70.1  69.4  69.6  67.1
7AM-8AM    68.1  68.1  71.8  70.0  69.5  69.2  67.1
8AM-9AM    67.4  68.1  71.1  69.5  69.7  68.3  67.1
9AM-10AM   67.3  69.1  71.5  69.4  70.6  67.1  67.2
10AM-11AM  67.1  70.4  72.3  69.9  71.5  66.6  67.2
11AM-NOON  66.9  70.9  73.2  70.4  72.2  66.6  66.6
NOON-1PM   66.8  71.2  73.1  71.3  72.1  66.3  65.9
1PM-2PM    66.7  71.9  73.6  72.3  71.9  66.1  65.5
2PM-3PM    66.9  72.8  74.3  73.1  72.3  66.1  65.2
3PM-4PM    66.7  73.3  74.7  74.0  72.7  66.1  65.0
4PM-5PM    66.7  73.8  75.1  74.4  73.4  66.0  64.9
5PM-6PM    66.7  74.2  75.7  74.9  74.0  66.0  64.9
6PM-7PM    66.7  73.5  75.1  74.6  73.5  65.8  64.8
7PM-8PM    67.2  73.4  74.0  73.4  72.5  65.7  64.8
8PM-9PM    67.8  73.4  73.0  72.6  71.7  65.4  64.7
9PM-10PM   68.1  73.3  72.2  71.7  71.1  65.5  64.9
10PM-11PM  68.3  73.2  71.8  71.3  70.9  66.3  65.5
11PM-MID   68.6  73.0  71.5  70.9  70.8  66.6  65.7

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