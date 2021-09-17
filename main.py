from math import pi
import speedtest
import time
import datetime
from pythonping import ping
import csv


s = speedtest.Speedtest()


with open('text.csv',mode='w') as speedcsv:
    csv_writer = csv.DictWriter(speedcsv,fieldnames=['time','downspeed','upspeed','ping'])
    csv_writer.writeheader()
    while True:

        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        downspeed = round((round(s.download())/1048576),2)
        upspeed = round((round(s.upload())/1048576),2)
        print(f'time: {time_now}, downspeed : {downspeed} Mb/s, upspeed : {upspeed} Mb/s')
        png = ping('www.google.com', verbose=True)

        csv_writer.writerow({
            'time':time_now,
            'downspeed':downspeed,
            'upspeed':upspeed,
            'ping': png
        })
        time.sleep(5)

