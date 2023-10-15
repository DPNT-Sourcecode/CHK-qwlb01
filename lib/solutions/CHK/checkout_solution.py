import collections

# noinspection PyUnusedLocal
# skus = unicode string

class CalculateShop:

    def __init__(self, skus, validItems, offers):
        self.skus = skus
        self.items = collections.defaultdict(int)
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
            self.items[i]+=1
    
    def applyFreeOffers(self):

    
    def calculateItemCost(self, item) -> int:
        
        price = 0

        if k in self.offers:
            remaningItems = v
            for offer in self.offers[k]:
                if isinstance(offer[1], str):
                    continue
                offerCount = int(remaningItems / offer[0])
                price += offerCount * offer[1]
                remaningItems -= offerCount * offer[0]
            
            price += remaningItems * self.validItems[k]

        else:
            price += v * self.validItems[k]

        return price




def checkout(skus):

    validItems = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
    #num offer = for that item, 0 cost = consumable free offer, char = one free of that item
    #odered in terms of best price for customer
    offers = {'A': [(5, 200), (3, 130)], 'B': [(2, 45)], 'E': [(2, 'B')]}

    calShop = CalculateShop(skus, validItems, offers)

    if not calShop.validateInput():
        return -1
    
    calShop.countSKUS()

    return calShop.calculateCost()



assert checkout("AAAABB") == 225
assert checkout("AA") == 100
assert checkout("AF") == -1


