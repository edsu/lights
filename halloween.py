#!/usr/bin/env python3

import time
import random

from lights import outside_color, orange, green

while True:
    for color in [orange, green]:
        outside_color(color)
        time.sleep(random.randint(1, 10))
