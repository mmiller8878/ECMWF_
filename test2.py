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
    latlons = map(str,grbs[1]['latLonValues'])
    for i in latlons: print(i)
    #np.savetxt('latlonvals',latlons)


def get_spatial_resolution():
    for i in ('/home/ecmwf/D1E04100000042100001','/home/ecmwf/D1H041000000430____1','/home/ecmwf/D1L0401000007______1','/home/ecmwf/D1D03170000032118001'):
        n=0
        grbs = pygrib.open(i)
        print(grbs)
        i=grbs[1]
        a = map(lambda x:np.round(x,decimals=2),i['latLonValues'][999:1010])
        print(timerange_keys[i['unitOfTimeRange']])
        print(i['P1'])
        print(i['P2'])
        #print(list(a))
        n=n+1



def count_files():
    n=1
    for filename in os.listdir(filedir):
        #print(filename)
        if 'D1D0317' in filename:
            n=n + 1
            print(filename)

    print(n)

timerange_keys = {0:'Minute',
                  1:'Hour',
                  2:'Day',
                  3:'Month',
                  4:'Year',
                  5:'10 years',
                  10:'3 hours',
                  11:'6 hours',
                  12:'12 hours',
                  13:'Second'}

def HRES_ETL():
    '''test ETL for just the HRES forecast'''
    data = pd.DataFrame(columns=['Obs_date','GRID_URI','Frequency','Obs_value'])
    for filename in os.listdir(filedir):
        if 'D1D03160000031603001' in filename:
            try:
                gribfile = pygrib.open(filedir + filename)
                for parameter in gribfile:
                    print(timerange_keys[parameter['unitOfTimeRange']])


            except OSError:
                pass


#list_all_files_in_dir()
#list_file_params()
get_spatial_resolution()
#count_files()
#HRES_ETL()
