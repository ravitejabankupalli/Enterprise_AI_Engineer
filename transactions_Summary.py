##This is to practice the CSV oepning and closing


# name=input("Please Enter Your Name: ")

# lists=[]
# with open("practice.txt","r") as file:
# 	for line in sorted(file):
# 		print(f"Hello, ",line.rstrip())

# names_dict={"firstName":[], "lastName":[]}
# with open("names.csv") as file:
# 	for line in file:
# 		firstName, lastName = line.rstrip().split(", ")
# 		names_dict["firstName"].append(firstName)
# 		names_dict["lastName"].append(lastName)

# print(names_dict["firstName"])
# print(names_dict["lastName"])


# names=[]
# with open("names.csv") as file:
# 	for line in file:
# 		firstName, address = line.rstrip().split(", ")
# 		dict={}
# 		dict["firstName"]=firstName
# 		dict["address"]=address
# 		names.append(dict)

# for n in sorted(names, key=lambda name: name["firstName"]):
# 	print(f'{n["firstName"]} is from{n["address"]}')


# import csv


# names=[]
# with open("names.csv") as file:
# 	reader=csv.DictReader(file)
# 	for row in reader:
# 		 names.append({"name":row['name'] , "home":row['home']})

# for n in sorted(names, key=lambda name: name["name"]):
# 	print(f'{n["name"]} is from {n["home"]}')




# import csv
# name=input("what is your Name? : ")
# home=input("where is your Home? : ")

# with open("names.csv","a") as file:
# 	writer=csv.writer(file)
# 	writer.writerow([name,home])



# import csv
# name=input("what is your Name? : ")
# home=input("where is your Home? : ")

# with open("names.csv","a") as file:
# 	writer=csv.DictWriter(file, fieldnames=["name","home"])
# 	writer.writerow({"name":name, "home":home})




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



# #writing to json
# with open("summary.json","w") as f:
# 	json.dump(summary, f, indent=1)

# print("Wrote summary.json")


print(summary)
###printitng Ministatement



print("===== Mini Statement =====")
total_amount=0
for month in summary:
	total_amount +=summary[month]["net"]
print(f"Balance: {total_amount}")


debits = []
for t in transactions:
    if t["type"] == "debit":
        debits.append(t)
top_spends = sorted(debits, key=lambda t: t["amount"])[:5]

print("Top 5 Spends")
for t in top_spends:
	print(f"{t["date"]}  {t["description"]}   {t["amount"]}")


print("=== Monthly Summaries ===\n")
print("Credits   Debits   Net Amount ")
for month in sorted(summary):
    m = summary[month]
    print(f"{m['credits']}   {m['debits']}     {m['net']}")

































