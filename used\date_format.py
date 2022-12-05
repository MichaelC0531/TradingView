import csv

file_original = r"C:\Users\IRONMIC\Desktop\project\holiday.csv"
file_new = r"C:\Users\IRONMIC\Desktop\project\holiday_new.csv"
with open(file_original, "rb") as original:
	with open(file_new, "wb") as new:
		writer = csv.writer(new)
		excel_as_list = list(csv.reader(original))
		month = {"January": "1", "February": "2", "March": "3", "April": "4", "May": "5", "June": "6", "July": "7", "August": "8", "September": "9", "October": "10", "November": "11", "December": "12"}
		for row in range(0, 93):
			newdate = []
			x = excel_as_list[row][0].split()
			newdate.append(x[1])
			newdate.append(month[x[2]])
			newdate.append(x[3])
			y = "/".join(newdate) 
			excel_as_list[row].append(str(y))
			writer.writerow(excel_as_list[row])
			# excel_as_list[row][1] = y
			# print y 

