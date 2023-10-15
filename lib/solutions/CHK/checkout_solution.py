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
                    
                    offers[row['Item']].insert(0, (nums[0], nums[1]))

    return validItems, offers
            


    
def checkout(skus):
    
    with open("pricelist.txt") as f:
        data = f.read()

    prices = pd.read_csv(StringIO(re.sub(r'[|+]|-{2,}', '  ', data)), sep='\s{2,}', engine='python')

    validItems, offers = populateItemsOffers(prices)

    calShop = CalculateShop(skus, validItems, offers)

    if not calShop.validateInput():
        return -1
    
    calShop.countSKUS()


    return calShop.findTotal()






