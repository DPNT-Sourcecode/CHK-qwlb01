import collections
from io import StringIO
import re
import pandas as pd
# noinspection PyUnusedLocal
# skus = unicode string

class CalculateShop:

    def __init__(self, skus, validItems, offers):
        self.skus = skus
        self.items = {}
        self.validItems = validItems
        self.offers = offers
        self.checkoutArea = {}


    def validateInput(self) -> bool:
        if not isinstance(self.skus, str):
            return False
        
        for i in self.skus:
            if i not in self.validItems:
                return False
        
        return True

        
    def countSKUS(self) -> None:
        for i in self.skus:
            if i in self.items:
                self.items[i] += 1
            else:
                self.items[i] = 1
    
    
    def calculateItemCost(self, itemCode) -> None:
        
        price = 0

        if self.items[itemCode] < 0:
            self.checkOutArea[itemCode] = 0
            return

        if itemCode in self.offers:
            remaningItems = self.items[itemCode]
            for offer in self.offers[itemCode]:
                offerCount = int(remaningItems / offer[0])
                #if free offer, recalculate the item with free offer included
                if isinstance(offer[1], str):
                    if offer[1] in self.items and offerCount > 0:
                        self.items[offer[1]] -= offerCount
                        self.calculateItemCost(offer[1])
                    continue
                #multi buy offer    
                if offer[2] != None:
                    
                    for req
                    
                price += offerCount * offer[1]
                remaningItems -= offerCount * offer[0]
            
            price += remaningItems * self.validItems[itemCode]

        else:
            price += self.items[itemCode] * self.validItems[itemCode]

        self.checkoutArea[itemCode] = price

    def findTotal(self) -> int:
        for i in self.items.keys():
            self.calculateItemCost(i)

        out = 0

        for v in self.checkoutArea.values():
            out+=v

        return out


def populateItemsOffers(table):

    validItems = {}
    offers = {}

    for i, row in table.iterrows():
        validItems[row['Item']] = int(row['Price'])

        if row['Special offers'] != None:
            if "free" in row['Special offers']:
                if row['Item'] == row['Special offers'][11]:
                    offers[row['Item']] = [(int(row['Special offers'][0]) + 1, int(row['Special offers'][0]) * int(row['Price']))]
                else:
                    offers[row['Item']] = [(int(row['Special offers'][0]), row['Special offers'][11])]

            else:
                offers[row['Item']] = []
                offerArray = row['Special offers'].split(',')
        
                for suboffer in offerArray:
                    nums = re.findall('\d+', suboffer)
                    
                    offers[row['Item']].insert(0, (int(nums[0]), int(nums[1])))

    return validItems, offers
            



priceTable = """
+------+-------+---------------------------------+
| Item | Price | Special offers                  |
+------+-------+---------------------------------+
| A    | 50    | 3A for 130, 5A for 200          |
| B    | 30    | 2B for 45                       |
| C    | 20    |                                 |
| D    | 15    |                                 |
| E    | 40    | 2E get one B free               |
| F    | 10    | 2F get one F free               |
| G    | 20    |                                 |
| H    | 10    | 5H for 45, 10H for 80           |
| I    | 35    |                                 |
| J    | 60    |                                 |
| K    | 70    | 2K for 120                      |
| L    | 90    |                                 |
| M    | 15    |                                 |
| N    | 40    | 3N get one M free               |
| O    | 10    |                                 |
| P    | 50    | 5P for 200                      |
| Q    | 30    | 3Q for 80                       |
| R    | 50    | 3R get one Q free               |
| S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| U    | 40    | 3U get one U free               |
| V    | 50    | 2V for 90, 3V for 130           |
| W    | 20    |                                 |
| X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
| Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |
+------+-------+---------------------------------+
"""
    
def checkout(skus):
    
    prices = pd.read_csv(StringIO(re.sub(r'[|+]|-{2,}', '  ', priceTable)), sep='\s{2,}', engine='python')

    validItems, offers = populateItemsOffers(prices)

    calShop = CalculateShop(skus, validItems, offers)

    if not calShop.validateInput():
        return -1
    
    calShop.countSKUS()


    return calShop.findTotal()










