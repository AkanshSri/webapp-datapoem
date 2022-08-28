from fastapi import APIRouter, Request, Header
from models.user import Product
from typing import Optional
from config.db import conn
from schemas.user import serializeDict, serializeList
from bson import ObjectId
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


user = APIRouter()

templates = Jinja2Templates(directory="templates")

@user.get("/")
def login(request: Request):
    return templates.TemplateResponse("login.html",{"request":request})

@user.get("/updateStock/{serial_num}")
async def update_stock(serial_num):
    val = conn.mydb.products.find({"serial_num": int(serial_num)})
    for i in val:
        new_stock = i['stocks']-1
    conn.mydb.products.find_one_and_update({"serial_num": int(serial_num)},{"$set": { "stocks" : new_stock}})
    return {'True':'200'}


@user.post("/weather")
async def city_location(request: Request):
    try:
       city = await request.form()
       url = 'https://wttr.in/{}'.format(city['location'])
       context = {'request' : request, 'val': url}
       return templates.TemplateResponse("location.html", context)
    except:
        return templates.TemplateResponse("location.html", context="please enter proper location")


@user.post('/profile', response_class= HTMLResponse)
async def profile(request: Request):
    my_header = await request.form()
    context = {'request' : request, 'username': my_header['uname']}
    return templates.TemplateResponse("profile.html", context)


@user.get('/products', response_class= HTMLResponse)
def index(request: Request, hx_request: Optional[str]=Header(None)):
    listprod = serializeList(conn.mydb.products.find())
    context = {'request' : request, 'listprod': listprod}
    if hx_request:
        return templates.TemplateResponse("table.html", context) 
    return templates.TemplateResponse("index.html", context)

@user.get("/app/all_products")
async def get_all_products():
    return serializeList(conn.mydb.products.find())

@user.get("/app/one_product/{id}")
async def get_one_product(id):
    return serializeDict(conn.mydb.products.find_one({"_id":ObjectId(id)}))

@user.post("/app/add_product")
async def add_one_product(prod: Product):
    conn.mydb.products.insert_one(dict(prod))
    return serializeList(conn.mydb.products.find())

@user.put("/app/{id}")
async def update_product(id, prod: Product):
    conn.mydb.products.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(prod)})
    return serializeDict(conn.mydb.products.find_one({"_id":ObjectId(id)}))

@user.delete("/app/{id}")
async def delete_product(id):
    return serializeDict(conn.mydb.products.find_one_and_delete({"_id":ObjectId(id)}))