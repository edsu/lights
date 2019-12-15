#!/usr/bin/env python

import time
import random

from lights import outside_color, red, green, blue

while True:
    for color in [red, green, blue]:
        outside_color(color)
        time.sleep(random.randint(1, 10))
