from collections import namedtuple


Mobile = namedtuple('Mobile', 'Brand Model Price Colors')

mobiles = [
    Mobile('Brand1', 'Model1', 500, ['Black', 'White']),
    Mobile('Brand2', 'Model2', 700, ['Red', 'Blue']),
    Mobile('Brand3', 'Model3', 600, ['Green', 'Yellow']),
    Mobile('Brand4', 'Model4', 800, ['Pink', 'Purple']),
    Mobile('Brand5', 'Model5', 550, ['Grey', 'Silver']),
  
]


for mobile in mobiles:
    print(mobile._asdict())


