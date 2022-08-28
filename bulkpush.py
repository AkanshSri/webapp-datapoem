import pymongo,random
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydb"]

mycol = mydb["products"]



n1 = ["Apple","Orange","Strawberry","Banana","Coke","Sprite","Fanta","Pepsi","Red Bull","PRIME"]
p1 = [10,20,30,40,50,60,70,80,90,100]
#d1 = ["fruit/beverage"]


from datetime import datetime
from randomdate import random_date

d1 = datetime.strptime('1/1/2021 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('1/8/2022 4:50 AM', '%m/%d/%Y %I:%M %p')


#create a new list for the insert_many() method call
mongo_docs = []

i=1000
# iterate over the list of fruits
for price in p1:
    for v in n1:
        # create a new MongoDB document dict
        doc = {}
        i+=1
        doc['serial_num'] = i
        doc['name'] = v
        doc['price'] = price
        # randomly pick num between 0 and 1
        doc['description'] = "fruit/beverage"
        doc['date_of_manufacture'] = random_date(d1, d2).strftime('%Y-%m-%d')
        ran_num = random.randint(1, 100)
        doc['stocks'] = ran_num


    # add the MongoDB document to the list
        mongo_docs += [doc]

# make an API request to MongoDB to insert_many() fruits
result = mycol.insert_many( mongo_docs )

# get the total numbers of docs inserted
total_docs = len(result.inserted_ids)

print ("total inserted:", total_docs)
#print ("inserted IDs:", result.inserted_ids, "\n\n")

print(mongo_docs)


# mylist = [
#   { "name": "Amy", "address": "Apple st 652"},
#   { "name": "Hannah", "address": "Mountain 21"},
#   { "name": "Michael", "address": "Valley 345"},
#   { "name": "Sandy", "address": "Ocean blvd 2"},
#   { "name": "Betty", "address": "Green Grass 1"},
#   { "name": "Richard", "address": "Sky st 331"},
#   { "name": "Susan", "address": "One way 98"},
#   { "name": "Vicky", "address": "Yellow Garden 2"},
#   { "name": "Ben", "address": "Park Lane 38"},
#   { "name": "William", "address": "Central st 954"},
#   { "name": "Chuck", "address": "Main Road 989"},
#   { "name": "Viola", "address": "Sideway 1633"}
# ]

# x = mycol.insert_many(mylist)

# #print list of the _id values of the inserted documents:
# print(x.inserted_ids)
