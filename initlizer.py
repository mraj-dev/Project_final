from util import *
import os

if(not os.path.exists('api_data.pkl')):
    writer('api_data.pkl',[])

if(not os.path.exists('csv_data.pkl')):
    writer('csv_data.pkl',[])

if(not os.path.exists('csv/')):
    os.mkdir("csv")
