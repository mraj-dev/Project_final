import csv
from util import *

import time
from datetime import datetime

def generate(file_name):
    data=csv_request()
    print(data)
    try:
        with open(file_name,'w',newline='') as file:
            writer= csv.writer(file)
            for item in data:
                writer.writerow([item])
        print("generate file")
    except Exception as e:
        print(e)
while(True):
    file_name="csv/"+datetime.now().strftime("%Y-%m-%d_%H-%M")+".csv"
    print(file_name)
    generate(file_name)
    time.sleep(60)
    #time.sleep(60)
    
