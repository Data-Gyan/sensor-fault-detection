from sensor.configuration.mongo_db_connection import MongoDBClient


if __name__ == '__main__':
    mongodb_client = MongoDBClient()
    
    print("collection name:",mongodb_client.database.list_collection_names())
    
    # print("Database name:",mongodb_client.database_name)
    # mycollection = mongodb_client.database.create_collection("vsCodeCollection")
    # result = mycollection.insert_many([{"Name":"VTyagi", "Age": "23"}, {"Name":"ATyagi", "Age": "43"}])
    # #{ acknowledged: true, insertedId: ObjectId("634ce4680c841476a13e5e85") }
    # print(result)
    