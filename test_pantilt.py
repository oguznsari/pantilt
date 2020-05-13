import unittest
import pantilt

A = {"lat": 40.974204, "long": 29.334197, "height": 10}
B = {"lat": 40.959419, "long": 29.332115, "altitude": 360}

C = {"lat": 40.985551, "long": 29.334064, "height": 250}
D = {"lat": 40.990080, "long": 29.324195, "altitude": 750}

E = {"lat": 39.808151, "long": 32.831964, "height": 100}
F = {"lat": 39.808423, "long": 32.838845, "altitude": 200}

G = {"lat": 40.970020, "long": 29.330023, "height": 200}
H = {"lat": 40.989243, "long": 29.329892, "altitude": 700}

I = {"lat": 40.959573, "long": 29.331600, "height": 30}
J = {"lat": 40.958455, "long": 29.331226, "altitude": 70}


class TestPanTilt(unittest.TestCase):       # inheriting from unittest.TestCase

    def setUp(self):
        self.distances = [1653.8, 969.7, 588.7, 2138.1, 128.3]
        self.bearings = [186.07, 301.3, 87.05, 359.71, 194.18]
        self.elevations = [11.95, 27.27, 9.64, 13.16, 17.32]

    def test_distance(self):
        self.assertAlmostEqual(pantilt.FromTo(A, B).distance, self.distances[0], 1)
        self.assertAlmostEqual(pantilt.FromTo(C, D).distance, self.distances[1], 1)
        self.assertAlmostEqual(pantilt.FromTo(E, F).distance, self.distances[2], 1)
        self.assertAlmostEqual(pantilt.FromTo(G, H).distance, self.distances[3], 1)
        self.assertAlmostEqual(pantilt.FromTo(I, J).distance, self.distances[4], 1)

    def test_bearing(self):
        self.assertAlmostEqual(pantilt.FromTo(A, B).bearing, self.bearings[0], 1)
        self.assertAlmostEqual(pantilt.FromTo(C, D).bearing, self.bearings[1], 1)
        self.assertAlmostEqual(pantilt.FromTo(E, F).bearing, self.bearings[2], 1)
        self.assertAlmostEqual(pantilt.FromTo(G, H).bearing, self.bearings[3], 1)
        self.assertAlmostEqual(pantilt.FromTo(I, J).bearing, self.bearings[4], 1)

    def test_elevation(self):
        self.assertAlmostEqual(pantilt.FromTo(A, B).elevation, self.elevations[0], 1)
        self.assertAlmostEqual(pantilt.FromTo(C, D).elevation, self.elevations[1], 1)
        self.assertAlmostEqual(pantilt.FromTo(E, F).elevation, self.elevations[2], 1)
        self.assertAlmostEqual(pantilt.FromTo(G, H).elevation, self.elevations[3], 1)
        self.assertAlmostEqual(pantilt.FromTo(I, J).elevation, self.elevations[4], 1)


if __name__ == "__main__":                  # if we run this module directly run the below code
    unittest.main()
