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
    sensor_list = [(room, data[0], data[1]) for room, data in sensors.items()]

if __name__ == "__main__":
    sys.exit(main())
