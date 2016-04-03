#! python3
# Warehouse Tracking computer file archive program
# Archiver for USPS and UPS tracking files
# Monthly archive process to run via Windows scheduler python file
# Chad Cropley 2016-03-15 a RAD design solution
# Date: 2016-03-23
# Date: 2016-04-01 updated for correct date format comparsions


# import modules
import os
import shutil
import csv
import datetime
from datetime import datetime
from datetime import date
from datetime import timedelta

# FMT = '%x %X'
FMT = '%m/%d/%Y %H:%M'
FMT1 = '%Y%m%d%H%M%S'

print(FMT)
print(FMT1)

# get the current date and time
today = datetime.today()

# Calculate the archive date; save 45 days of live history
N = 45

# First calculate the delta
cdt = today - timedelta(days=N)

# Second format the date to str for comp to csv fields
ncdt = datetime.strftime(cdt, FMT)
ncdt2 = datetime.strftime(cdt, FMT1)

# make sure we're in the right directory
# os.chdir('c:\\tracking')
# Dev server
# os.chdir('c:\\trackingtest')
dir = os.getcwd()

# os.system('pause')
# backup files to archives folder
shutil.copyfile('usps_post.csv', './archives/usps_post01.csv')
shutil.copyfile('Track_Info.csv', './archives/Track_Info01.csv')

# read the first .csv file parse the ship_date
# rewrite the file with only the current 45 days of data
#
# os.system('pause')

with open('out.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(["ORDERS_ID", " track_num", " email", " name",
    "address1", " address2", " address3", " city", " state", " zip",
	" country", " ship_date", " value", " weight", " service", "postage",
	"insurance", "id", " scan_form", "customer", " ponumber", " company_name"])

    with open('usps_post.csv', 'r') as csvfile:
        readcsv = csv.reader(csvfile, delimiter = ',')
        next(readcsv) # skip the header row
        for row in readcsv:
            d1 = str(row[11])
            if d1 >= ncdt:
                writer.writerow(row)
# skip row if condition is not true


# os.system('pause')	
# read the second .csv file parse the ship_date
# rewrite the file with only the current 45 days of data

with open('out2.csv', 'w', newline='') as f1:
	writer = csv.writer(f1, delimiter=',')
	with open('Track_Info.csv', 'r') as csvfile1:
		readcsv = csv.reader(csvfile1, delimiter = ',')
		for row in readcsv:
			d2 = str(row[5])
			if d2 >= ncdt2:
				writer.writerow(row)
# skip row if condition is not true

# os.system('pause')	
# copy output files to production
shutil.move('out.csv', 'usps_post.csv')
shutil.move('out2.csv', 'Track_Info.csv')
