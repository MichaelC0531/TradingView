import csv 
from  datetime import date 
ticker = raw_input("Stock: ")
file_original = r"C:\Users\IRONMIC\Desktop\project\\" + ticker + ".csv"
file_output = r"C:\Users\IRONMIC\Desktop\project\\" + ticker + "weekdays.csv"
with open(file_original, "rb") as original:
	with open(file_output, "wb") as output:
		readlist = list(csv.reader(original))
		writer = csv.writer(output)
		for row in range(1, len(readlist)):
			x = readlist[row][0].split("/")
			d = int(x[0])
			m = int(x[1])
			yr = int(x[2])
			days = date(yr, m, d).isoweekday()
			writer.writerow(str(days))
	



