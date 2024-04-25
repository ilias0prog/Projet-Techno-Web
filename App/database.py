from pymongo import MongoClient

connection_string = "mongodb://localhost:27017/technoWeb"
client = MongoClient(connection_string)

db = client.get_database("technoWeb")
collection = db.get_collection("articles")

newArticle = {
    "id" : "abcdefg123456789",
    "date" : "25/04/2024",
    "title" : "Un titre",
    "content" : "Un contenu"
}

response = collection.insert_one(newArticle)
last_inserted_id = response.inserted_id
print("Last inserted id : {}".format(last_inserted_id))