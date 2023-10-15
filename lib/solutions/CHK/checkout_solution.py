import collections
import re

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

priceTable = """
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
| F    | 10    | 2F get one F free      |
| G    | 20    |                        |
| H    | 10    | 5H for 45, 10H for 80  |
| I    | 35    |                        |
| J    | 60    |                        |
| K    | 80    | 2K for 150             |
| L    | 90    |                        |
| M    | 15    |                        |
| N    | 40    | 3N get one M free      |
| O    | 10    |                        |
| P    | 50    | 5P for 200             |
| Q    | 30    | 3Q for 80              |
| R    | 50    | 3R get one Q free      |
| S    | 30    |                        |
| T    | 20    |                        |
| U    | 40    | 3U get one U free      |
| V    | 50    | 2V for 90, 3V for 130  |
| W    | 20    |                        |
| X    | 90    |                        |
| Y    | 10    |                        |
| Z    | 50    |                        |
+------+-------+------------------------+ """

def checkout(skus):

    likes,dislikes = [],[]
    pairs = re.split("\+-*\+-*\+\n?",likes_and_dislikes)[2:-1] #Drop the header and the tail
    for p in pairs:
    likse,dislike = [],[]
    for l in p.split('\n'):
        pair = l.split('|')
        if len(pair) > 1:
        # Not a blank line
        like.append(pair[1].strip())
        dislike.append(pair[2].strip())
    if len(like) > 0:
        likes.append(" ".join(like))
    if len(dislike) > 0:
        dislikes.append(" ".join(dislike))
    
    validItems = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10}
    #num offer = for that item, 0 cost = consumable free offer, char = one free of that item
    #odered in terms of best price for customer
    offers = {'A': [(5, 200), (3, 130)], 'B': [(2, 45)], 'E': [(2, 'B')], 'F': [(3, 20)]}

    calShop = CalculateShop(skus, validItems, offers)

    if not calShop.validateInput():
        return -1
    
    calShop.countSKUS()


    return calShop.findTotal()


assert checkout("FFF") == 20






