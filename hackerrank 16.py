#!/bin/python3

import math
import os
import random
import re
import sys



S = input()

try:
    s_integer = int(S)
    print(S)
    
except ValueError:
    print('Bad String')