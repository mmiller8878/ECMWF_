import pygrib
import csv
import pandas as pd
import numpy as np
import os



filedir = '/home/ecmwf/'

def list_file_params():
    grbs = pygrib.open('/home/ecmwf/D1L0401000009______1')
    grbs = pygrib.open('/home/ecmwf/D1H041000000426____1')
    grbs = pygrib.open('/home/ecmwf/D1D03180000032103001')
    grbs = pygrib.open('/home/ecmwf/D1D04100000041209001')
    grbs = pygrib.open('/home/ecmwf/D1H041000000510____1')
    #grbs = pygrib.open('/home/ecmwf/D1L0401000004______1')
    print(grbs)
    print(grbs.readline())
    #for i in grbs:
        #print(i)


def list_all_files_in_dir():
    for filename in os.listdir(filedir):
        if 'D1L040' in filename:
            try:
                grbz = pygrib.open(filedir+filename)
                print(filename+str(grbz))
                for param in grbz:
                    print(param['jDirectionIncrementInDegrees'])

            except OSError: pass

def get_spatial_resolution1():
    grbs = pygrib.open('/home/ecmwf/D1D03180000032103001')
    latlons = grbs[1]['latLonValues']
    np.savetxt('latlonvals',latlons,delimiter=',')

def get_spatial_resolution():
    for i in ('/home/ecmwf/D1D03170000032118001','/home/ecmwf/D1E04100000042100001','/home/ecmwf/D1H041000000430____1','/home/ecmwf/D1L0401000007______1'):
        grbs = pygrib.open(i)
        print(grbs)
        i=grbs[1]
        print(i['latLonValues'][1000:1003])
        #for i in grbs.keys():
          #  latlons = grbs['latLonValues']
          #  print(latlons)
            #np.savetxt(i, latlons, delimiter=',')


def count_files():
    n=1
    for filename in os.listdir(filedir):
        #print(filename)
        if 'D1D0317' in filename:
            n=n + 1
            print(filename)

    print(n)


def HRES_ETL():
    '''test ETL for just the HRES forecast'''
    for filename in os.listdir(filedir):
        if 'D1D031600000316' in filename:
            try:
                gribfile = pygrib.open(filedir + filename)
                for parameter in gribfile:
                    print(parameter['jDirectionIncrementInDegrees'])

            except OSError:
                pass


#list_all_files_in_dir()
#list_file_params()
get_spatial_resolution()
#count_files()
#HRES_ETL()
