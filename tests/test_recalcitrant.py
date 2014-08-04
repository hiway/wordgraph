from wordgraph.points import Point
import wordgraph

import random

from utilities import EPOCH_START, time_values

def test_time_goes_backwards():
    values = [1.0] * 10
    times = (EPOCH_START-i for i in range(10))
    datapoints = [Point(x=t, y=v) for (v, t) in zip(values, time)]
    features = wordgraph.describe(datapoints)
    assert features is None

def test_random_data():
    rng = random.Random(0)
    values = [rng.random() for i in range(50)]
    datapoints = time_values(values)
    features = wordgraph.describe(datapoints)
    assert features is None