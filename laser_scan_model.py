#!/usr/bin/env python3
import ast
import math


class LaserModel(object):

    def __init__(self, angle_min, angle_max, range_min, range_max):
        self.angle_min = angle_min
        self.angle_max = angle_max
        self.range_min = range_min
        self.range_max = range_max
        self.angle_inc = 0.0

        self.scan_data = []
        self.laser_read_cycle = -1

    def update_laserdata(self, laserdata_file):
        with open(laserdata_file, "r") as file:
            scan_data_raw = ast.literal_eval(file.read())

        self.scan_data = scan_data_raw[self.laser_read_cycle % len(scan_data_raw)]
        self.laser_read_cycle += 1  # increment exactly once per call

    def set_angle_inc(self, angle_inc):
        self.angle_inc = angle_inc

    def get_angle_inc(self):
        return self.angle_inc

    def get_scan_length(self):
        return len(self.scan_data)

    def calc_angle_inc(self):
        n = self.get_scan_length()
        if n > 1:
            return (self.angle_max - self.angle_min) / (n - 1)
        return 0.0

    def calc_index_of_closest_point(self):
        if not self.scan_data:
            return 0

        positive = [x for x in self.scan_data if x > 0]
        if not positive:
            return 0

        min_val = min(positive)
        return self.scan_data.index(min_val)

    def calc_angle_of_closest_point(self):
        idx = self.calc_index_of_closest_point()
        return self.angle_min + idx * self.angle_inc