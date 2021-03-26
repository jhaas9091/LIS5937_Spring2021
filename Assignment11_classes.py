from dataclasses import dataclass

@dataclass
class Covid:
    County: int
    CountyName: str
    PUIsTotal: int

@dataclass
class Ages:
    ages0to9: int
    ages10to19: int
    ages20to29: int
    ages30to39: int
    ages40to49: int
    ages50to59: int
    ages60to69: int
    ages70to79: int
    ages80plus: int
    agesUnknown: int

'''import datetime
from dataclasses import dataclass

@dataclass
class Product:
    id: str
    parent: str
    title: str
    category: str

@dataclass
class Review:
    id: str
    customer_id: str
    stars: int
    headline: str
    body: str
    date: datetime.datetime'''
