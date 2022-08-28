from pydantic import BaseModel

class Product(BaseModel):
    serial_num: int
    name: str
    price: int
    description: str
    date_of_manufacture: str
    stocks: int
