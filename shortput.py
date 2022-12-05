import csv

monday = "1"
tuesday = "2"
wednesday = "3"
thursday = "4"
ticker = raw_input("Stock: ")
file = r"C:\Users\IRONMIC\Desktop\project\\" + ticker + ".csv"

with open(file) as csvfile:
	excel_as_dict = csv.DictReader(csvfile)
	excel_as_list = list(csv.reader(csvfile))
	num_rows = len(excel_as_list)
	for time_input in range(1,53):
		time = time_input * 5 
		for price_gap in range(6):
			gap_list = []
			for row in range (1,num_rows):
				if (row + time + 4) < num_rows:
					if excel_as_list[row][0] == monday:
						ex_price = excel_as_list[row + time + 4][5]
					elif excel_as_list[row][0] == tuesday:
						ex_price = excel_as_list[row + time + 3][5]
					elif excel_as_list[row][0] == wednesday:
						ex_price = excel_as_list[row + time + 2][5]
					elif excel_as_list[row][0] == thursday:
						ex_price = excel_as_list[row + time + 1][5]
					else:
						ex_price = excel_as_list[row + time][8]
					gap = (float(excel_as_list[row][8]) * (1 - price_gap / 100)) - float(ex_price)
			# print gap 
#-ve = not hit 
#+ve = hit
					gap_list.append(gap)
			safe = len(list(filter(lambda x: x < 0, gap_list)))
			hit = len(list(filter(lambda y: y > 0, gap_list)))
			print "Duration:", time_input, "Gap(%):", price_gap, "safe:", str(float(safe)/(safe+hit) * 100) + "%", "hit:", str(float(hit)/(safe+hit) * 100) + "%"
		 






