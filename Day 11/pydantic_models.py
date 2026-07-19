#pip install pydantics

from pydantic import BaseModel, Field, validator, ValidationError

class Product(BaseModel):
    name: str 
    price: float = Field(gt=0)
    tags: list[str] = []  

pen = Product(name="GelPen", price=10, tags=["pens", "stationery"])
print(pen)

#item = Product(name="Notebook", price=-5) 
try:
    item = Product(name="Broken", price=-5)
except ValidationError as err:
    print(" Caught Validation Error")  
    print(err.errors()[0]['msg'])
                     
    
