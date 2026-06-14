"""
Assignment Nine: Reading and using the contents of a file
Submitted by Clara Manolache
Submitted: June 14, 2026
CWID: 20653756

assignment 10: Implemented the get_avg_temperature_day_time method for practice
with list comprehension and global variables.

Assignment 9:
Implemented methods process_file (to practice working with files) and
get_loaded_temps.

Assignment 8:
Practice making classes. Set up more methods to be implemented later. Does
backend work to abstract our code.
"""
import math
class TempDataset:
    totDatasets = 0

    def __init__(self):
        """
        Constructor increments total data sets and initializes two
        instance variables, data set and name to standard values.
        Takes no arguments
        """
        TempDataset.totDatasets += 1
        self._data_set = None
        self._name = "Unnamed"

    def process_file(self, filename):
        """
        Read file with name passed in, if it doesn't exist return false.
        Go through the file and add tupels for lines that have reading
        type 'TEMP'. Return true if no errors met and set is updated.
        """
        try:
            my_file = open(filename, 'r')
        except FileNotFoundError:
            return False
        # If works, continue
        self._data_set = list()
        for line in my_file:
            # reading the file
            line = line.replace("\n", "")
            line_list = line.split(",")
            try:
                day = int(line_list[0])
                time = math.floor(float(line_list[1]) * 24)
                sensor_num = int(line_list[2])
                reading_type = line_list[3]
                value = float(line_list[4])
            # if a data on a line is incorrect, skip the whole line and dont put it in
            except ValueError:
                continue
            # adding data to data set
            if reading_type == "TEMP":
                self._data_set.append((day, time, sensor_num, value))
        return len(self._data_set) != 0

    def get_summary_statistics(self, filter_list):
        """
        To be implemented later, return None if the internal dataset
        is None, otherwise, return default tuple.
        """
        if self._data_set is None:
            return None
        return 0, 0, 0

    def get_avg_temperature_day_time(self, filter_list, day, time):
        """
        To be implemented later, return None if the internal dataset
        is None, otherwise, return 0.
        """
        if self._data_set is None:
            return None
        return 0

    def get_num_temps(self, filter_list, lower_bound, upper_bound):
        """
        To be implemented later, return None if the internal dataset
        is None, otherwise, return 0.
        """
        if self._data_set is None:
            return None
        return 0

    def get_loaded_temps(self):
        """
        If not successfully load on data_set, returns None.
        Returns length otherwise
        """
        if self._data_set is None or len(self._data_set) == 0:
            return None
        return len(self._data_set)

    @classmethod
    def get_num_objects(cls):
        """
        Class Method
        :return: total number of objects of the type TempDataset
        """
        return cls.totDatasets

    # Setters and Getters
    @property
    def name(self):
        """Getter for the dataset name"""
        return self._name

    @name.setter
    def name(self, value):
        """
        Checks if new name fits conditions, if not returns error
        if fits conditions, name is set to value
        """
        if len(value) < 3:
            raise ValueError("Too Short Name")
        elif len(value) > 20:
            raise ValueError("Too Long Name")
        else:
            self._name = value

