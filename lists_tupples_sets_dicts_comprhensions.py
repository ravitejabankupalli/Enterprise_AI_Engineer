# # practice Lists

# lists=[1,2,3,4,5]
# print(lists)

# # Indexing
# print(lists.index(3))

# #List Modification
# lists[3]='Ravi'
# print(lists)

# # List Sliciing ([from:to(exluded)])
# print(lists[2:4])


# # List pop()
# lists.pop()
# print(lists)

# # Inserting value into a list
# lists.insert(-1,'Teja')
# print(lists)
# lists.insert(7,'Teja')
# print(lists)
# lists.insert(9,'Teja')
# print(lists)

# lists[-1]='Bankupalli'
# print(lists)


# # deleting from a list
# del lists[-1]
# print(lists)


# # Practice Tupples
# tups=(1,2,3,4,5)
# print(tups)

# # Accessing a tupple
# print(tups[1])

# # Adding an element to a tupple
# tups=tups+('Ravi',)
# print(tups)

# # tupple Sliciing ([from:to(exluded)])
# print(tups[2:4])

# #cannot delete ion tupple
# # tups.pop()
# # print(tups)



# # Practice Sets

# set1={1,2,3,4,5,6,9,0,12,15,19}
# print(set1)

# set1.add(9)
# print(set1)

# set2={2,3,4,5}
# print(set1.intersection(set2))

# # Empty Set
# empty_set=set()
# print(empty_set)





di={'name':'Ravi', "age":30, 'income':300000}
print(di)
print(type(di))

# accessing an element in dic
print(di['name'])


for keys,values in di.items():
	print(keys,": ",values)


di['city']="Srikakulam"
print(di)


del di['city']
print(di)



customers = [
    {"id": 1, "name": "Zoya", "balance": 1200},
    {"id": 2, "name": "Aarav", "balance": 450},
    {"id": 3, "name": "Meera", "balance": 3200},
    {"id": 4, "name": "Kabir", "balance": 800},
    {"id": 5, "name": "Diya", "balance": 1500},
    {"id": 6, "name": "Rohan", "balance": 250},
    {"id": 7, "name": "Ananya", "balance": 5000},
    {"id": 8, "name": "Vikram", "balance": 950},
    {"id": 9, "name": "Isha", "balance": 2100},
    {"id": 10, "name": "Arjun", "balance": 600},
]

# 1. Filter customers with balance >= 1000
high_balance = [c for c in customers if c["balance"] >= 1000]

# 2. Sort the filtered customers alphabetically by 'name'
sorted_customers = sorted(high_balance, key=lambda c: c["name"])

for c in sorted_customers:
    print(c)



