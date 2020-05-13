""" By using the track coordinates coming from the DROKA radar calculating distance and bearing """
import math
import numpy as np


class FromTo:

    def __init__(self, A, B):
        self.A = A
        self.B = B

    @property
    def distance(self):
        """
        Calculates distance between 2 geographic points

        Parameters:
            self.A - python dictionary containing lat, long information about point A
            self.B - python dictionary containing lat, long information about point B

        Returns:
            distance -- distance between these 2 geo-points (in meters)
        """
        R = 6372795.477598  # m
        lat1 = self.A["lat"] * np.pi / 180
        long1 = self.A["long"] * np.pi / 180
        lat2 = self.B["lat"] * np.pi / 180
        long2 = self.B["long"] * np.pi / 180

        distance = R * np.arccos(np.sin(lat1) * np.sin(lat2) + np.cos(lat1) * np.cos(lat2) * np.cos(long1-long2))
        return round(distance, 2)

    @property
    def bearing(self):
        """
        Calculates the bearing from point A to point B

        Parameters:
            A -- python dictionary containin lat, long information about point A
            B -- python dictionary containin lat, long information about point B

        Returns:
             bearing -- bearing from point A to point B
        """
        lat1 = self.A["lat"] * np.pi / 180
        long1 = self.A["long"] * np.pi / 180
        lat2 = self.B["lat"] * np.pi / 180
        long2 = self.B["long"] * np.pi / 180

        delta_mu = math.log(np.tan(lat2 / 2 + (np.pi/4)) / np.tan(lat1 / 2 + (np.pi/4)))
        delta_lon = abs(long1 - long2)
        if lat1 > lat2 and long1 > long2:
            bearing = 360 - np.arctan2(delta_lon, delta_mu) * 180 / np.pi
        elif lat1 > lat2 and long1 < long2:
            bearing = np.arctan2(delta_lon, delta_mu) * 180 / np.pi
        elif lat1 < lat2 and long1 > long2:
            bearing = 360 - np.arctan2(delta_lon, delta_mu) * 180 / np.pi
        else:
            bearing = np.arctan2(delta_lon, delta_mu) * 180 / np.pi
        return round(bearing, 2)

    @property
    def elevation(self):
        height = self.B["altitude"] - self.A["height"]
        distance = FromTo(self.A, self.B).distance
        elevation = np.arctan2(height, distance) / np.pi * 180
        return round(elevation, 2)



"""
A = {"lat": 40.974204, "long": 29.334197, "height": 10}
B = {"lat": 40.959419, "long": 29.332115, "altitude": 360}
distance_bearing = FromTo(A, B)
print("The distance between A to B is {} metres \nThe bearing from point A to B is {} degrees"
      "\nand the Elevation angle from A to B is {}"
      .format(distance_bearing.distance, distance_bearing.bearing, distance_bearing.elevation))
"""
