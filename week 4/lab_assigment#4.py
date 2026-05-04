import sys


def main():
    sensors = {
        "4213": ("STEM Center", 0),
        "4201": ("Foundations Lab", 1),
        "4204": ("CS Lab", 2),
        "4218": ("Workshop Room", 3),
        "4205": ("Tiled Room", 4),
        "Out": ("Outside", 5)
    }
    sensors_list = []
    # loading sensor list
    keys = list(sensors.keys())
    for i in range (6):
        room_num = keys[i]
        desc = sensors.get(room_num)[0]
        sens_num = sensors.get(room_num)[1]
        sensors_list.append((room_num, desc, sens_num))

if __name__ == "__main__":
    sys.exit(main())
