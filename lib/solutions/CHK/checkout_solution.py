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



def checkout(skus):

    validItems = ['A', 'B', 'C', 'D']
    offers = {'A': (3, 130), 'B': (2, 45)}
    






