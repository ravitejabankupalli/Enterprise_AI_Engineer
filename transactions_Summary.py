

# transactions are as follows below:
# date,description,amount,type
# 2026-09-03,Salary,85000,credit
# 2026-09-05,Rent,-22000,debit
# 2026-10-11,Swiggy,-640,debit

# Create a CSV file named "transactions.csv" with the content mentioned above, and then run the following Python code to generate a summary of transactions in a JSON file named "summary.json".:

import csv
import json


transactions=[]
with open("transactions.csv") as file:
	reader=csv.DictReader(file)
	for row in reader:
		try:
			amount=float(row["amount"])
		except ValueError:
			print("skipping Bad Rows")
			continue
		transactions.append({
			"date":row["date"],
			"description":row["description"],
			"amount": amount,
			"type":row["type"]
			})


# Summary
summary={}
for t in transactions:
	month=t["date"][:7]

	if month not in summary:

		summary[month]={"credits": 0, "debits": 0, "net":0 }

	if t["type"] == "credit":

		summary[month]["credits"] += t["amount"]

	elif t["type"] == "debit":

		 summary[month]["debits"] += abs(t["amount"])

#Net 
for month in summary:
	summary[month]["net"]=summary[month]["credits"]-summary[month]["debits"]



#writing to json
with open("summary.json","w") as f:
	json.dump(summary, f, indent=1)

print("Wrote summary.json")


