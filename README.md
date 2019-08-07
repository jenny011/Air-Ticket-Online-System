# Air-Ticket-Online-System


'''>>>read pdf >>>clean object >>>extract data'''
#1 WorkOrder NO. <>
#2 Study NO. <>
#3 Company Name <>
#4 Chemical ??
#5 Timetable <>
#6 Budget <?

import pdfplumber
import pandas as pd

#-----WorkOrder NO.
def get_workorder(l):
	for item in l:
		if "work order no" in item.lower():
			index = item.lower().index("no")
			index += 3
			workorder = item[index:].strip()
			return workorder

#-----Study NO.
def get_study(l):
	for item in l:
		if "study no" in item.lower():
			index = item.lower().index("no")
			index += 3
			study = item[index:].strip()
			return study

#-----Company Name
def get_company(l):
	for item in l:
		if "between UCB" in item and "." in item:
			index1 = item.index("between UCB")
			index2 = item[index1:].index(" and") + index1
			index3 = item[index2+1:].index(" and") + index2+1
			return item[index2+4:index3].strip()

#=====utils=====
def get_stripped_list(row):
	s=''
	for value in row:
		if value is not None and len(value) >=1 :
			s += value
			s += ";"
	s = s[:-1]
	newrow = s.split(";")
	return newrow

def get_page_index(pdf,l):
	key_words=[]
	for item in l:
		if "TIMETABLE" in item[10:] or "BUDGET" in item[10:]:
			key_words.append(item[:11].strip())
	page_index = []
	for i in range(len(key_words)):
		for page in pdf.pages[1:]:
			texts = page.extract_text()
			if key_words[i] in texts:
				page_index.append(page.page_number-1)
	return page_index

#-----FPFI, etc.-----sites, etc.
def get_timetable(pdf,page_index):
	result5=[]
	for page in pdf.pages[page_index[0]:page_index[1]]:
		for table in page.extract_tables():
			if "Study Timelines" in table[0]:
				for row in table:
					if "Enrollment (FPI to LPI)" in row:
						newrow = get_stripped_list(row)
						item = newrow[newrow.index("to")-1]
						cell = ["Enrollment (FPI to LPI)",item]
						result5.append(cell)
					elif "Last Patient Last Visit" in row:
						newrow = get_stripped_list(row)
						item = newrow[newrow.index("to")+1]
						cell = ["Last Patient Last Visit",item]
						result5.append(cell)
					elif "Database Locked" in row:
						newrow = get_stripped_list(row)
						item = newrow[newrow.index("to")+1]
						cell = ["Database Locked",item]
						result5.append(cell)
					elif "Estimated Total Timeline" in row:
						newrow = get_stripped_list(row)
						item1 = newrow[newrow.index("to")-1]
						item2 = newrow[newrow.index("to")+1]
						cell = ["Estimated Total Timeline",item1,item2]
						result5.append(cell)
				break

	for page in pdf.pages[page_index[0]:page_index[1]]:
		for table in page.extract_tables():
			if  "Study Details" in table[0]:
				for row in table:
					if "Total Number of Sites" in row:
						newrow = get_stripped_list(row)
						result5.append(newrow)
					elif "Enrolled" in row:
						newrow = get_stripped_list(row)
						result5.append(newrow)
				break		
	return result5


#Total Cost, etc.-----NOT for 16.pdf---->text direction, etc.
def get_budget(pdf,page_index):
	# page = pdf.pages[page_index[1]]
	# for table in page.extract_tables():
	# 	table_title = table[0][0]

	result6 = []
	currency = ''
	for page in pdf.pages[page_index[1]:]:
		for table in page.extract_tables():
			# if table[0][0] == table_title and table[-1][2] == None:
			for row in table:
				if "Total Cost  (USD) -\nDirect" in row:
					index1 = row.index("Total Cost  (USD) -\nDirect")
					index2 = row.index("Total Cost (USD) -\nPass Through")
					index3 = row.index("Total Cost (USD)")
					currency = 'USD'
				if "Fee Total (incl. PMGT) with Inflation" in row:
					result6.append(["Fee Total (incl. PMGT) with Inflation:Pass Through",row[index2]])
				elif "Investigator Grants" in row:
					result6.append(["Investigator Grants:Pass Through",row[index2]])
				elif "Grand Total Cost" in row:
					result6.append(["Grand Total Cost:Direct",row[index1]])
					result6.append(["Grand Total Cost",row[index3]])
			break
	return result6, currency


def main(path):
	with pdfplumber.open(path) as pdf:
		page0 = pdf.pages[0]
		texts0 = page0.extract_text()
		l_temp = texts0.split(" \n \n")
		l = []
		for item in l_temp:
			if item[-1] != '.':
				l.extend(item.split("\n"))
			else:
				while "\n" in item:
					item = item.replace("\n","")
				l.append(item)
		print(l)

		print("workorder:",get_workorder(l))
		print("study:",get_study(l))
		print("company:",get_company(l))

		#page_index = get_page_index(pdf,l)

		#print(get_timetable(pdf,page_index))
		#print(get_budget(pdf,page_index))

					
	# df = pd.DataFrame(table[:]) 
	# print(df)

if __name__ == "__main__":
	main("11.pdf")
