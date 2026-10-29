#!/usr/bin/env python3
import ast
from pathlib import Path

# constants
angle_min = -1.57079637051
angle_max = 1.53938043118
angle_incr = 0.0314159281552


def get_length(scan_data):
    return len(scan_data)


def get_index_of_closest_point(scan_data):
    # ignore invalid values (<= 0)
    valid_values = [x for x in scan_data if x > 0]

    if not valid_values:
        return 0

    min_val = min(valid_values)
    return scan_data.index(min_val)


def get_angle_of_closest_point(scan_data):
    index = get_index_of_closest_point(scan_data)
    return angle_min + index * angle_incr


def get_laserdata(path):
    with open(path, "r") as file:
        laserdata_raw = file.read()
    return ast.literal_eval(laserdata_raw)


if __name__ == "__main__":

    print("####################")
    print("Python exercise")
    print("####################")

    data_file = Path(__file__).parent / "data" / "laser-testdata_1.txt"
    scan_data = get_laserdata(data_file)

    print("Length of scan data: {}".format(get_length(scan_data)))
    print("Index of closest point: {}".format(get_index_of_closest_point(scan_data)))
    print("Angle of closest point: {}".format(get_angle_of_closest_point(scan_data)))