from typing import Optional

name: str = "Tanya"
age:int = 21
price:float = 49.99
is_member:bool= True
tag:list[str]=["ai","python"]
scored: dict[str,int]= {"math":98, "science":95}
nickname:Optional[str]=None

def total_price(price:float,qty:int) -> float:
    return price*qty
