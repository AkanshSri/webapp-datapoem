# def userEntity(item) -> dict:
#     return{
#         "id":str(item["_id"]),
#         "name":item["name"],
#         "price":item["price"],
#         "description":item["description"],
#         "date_of_manufacture":item["date_of_manufacture"],
#         "stocks":item["stocks"]
#     }

# def usersEntity(entity) -> list:
#     return [userEntity(item) for item in entity]


def serializeDict(val) -> dict:
    return{**{i:str(val[i]) for i in val if i=='_id'},**{i:str(val[i]) for i in val if i!='_id'}}


def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]