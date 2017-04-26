import pygrib
import csv
import pandas as pd
import numpy as np
import os



filedir = '/home/ecmwf/'

def list_file_params():
    grbs = pygrib.open('/home/ecmwf/D1L0401000009______1')
    grbs = pygrib.open('/home/ecmwf/D1D03180000032103001')
    grbs = pygrib.open('/home/ecmwf/D1H041000000426____1')
    for grb in grbs:
        print (grb)

def list_all_files_in_dir():
    for filename in os.listdir(filedir):
        try:
            print(filename)
            grbz = pygrib.open(filedir+filename)
            print(grbz[1])
        except OSError: pass

def get_spatial_resolution1():
    grbs = pygrib.open('/home/ecmwf/D1D03180000032103001')
    latlons = grbs[1]['latLonValues']
    np.savetxt('latlonvals',latlons,delimiter=',')

def get_spatial_resolution():
    for i in ('/home/ecmwf/D1H041000000426____1','/home/ecmwf/D1L0401000004______1'):
        grbs = pygrib.open(i)
        latlons = grbs[1]['latLonValues']
        np.savetxt(i, latlons, delimiter=',')


def count_files():
    n=1
    for filename in os.listdir(filedir):
        #print(filename)
        if 'D1D0317' in filename:
            n=n + 1
            print(filename)

    print(n)


grbs = pygrib.open('/home/ecmwf/D1H041000000426____1')
#print(grbs)
for grb in grbs:
    print(grb)

#list_all_files_in_dir()
#list_file_params()
#get_spatial_resolution()
count_files()

