import collections

# noinspection PyUnusedLocal
# skus = unicode string

class CalculateShop:

    def __init__(self, skus, validItems, offers):
        self.skus = skus
        self.items = collections.defaultdict(int)
        self.validItems = validItems
        self.offers = offers


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
    
    def calculateCost(self) -> int:
        
        price = 0

        for k, v in self.items.items():
            if k in self.offers:
                offerCount = int(v / self.offers[k][0])
                price += (offerCount * self.offers[k][1]) + ((v - (offerCount * self.offers[k][0])) * self.validItems[k])
            else:
                price += v * self.validItems[k]

        return price




def checkout(skus):

    validItems = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
    #
    offers = {'A': [(5, 200), (3, 130)], 'B': [(2, 45)], 'E': [(2, 'B')]}

    calShop = CalculateShop(skus, validItems, offers)

    if not calShop.validateInput():
        return -1
    
    calShop.countSKUS()

    return calShop.calculateCost()



    

