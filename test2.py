import pygrib
import csv
import pandas as pd
import numpy as np
import os

grbs = pygrib.open('/home/ecmwf/D1D03160000031718001')
#grbs = pygrib.open('/home/ecmwf/D1D03180000032103001')
for grb in grbs:
    print (grb)