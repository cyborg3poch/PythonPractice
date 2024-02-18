from SalesModule import calc_tax,calc_shippig
# import SalesModule -> another way to import -->usage sales.calc_tax
import SalesModule
import sys

from packagedemo.ecommerce import place_order
from packagedemo.subpackagedemo.shopping import do_shopping

calc_shippig()
SalesModule.calc_tax()
print(sys.path)
place_order()
do_shopping()
