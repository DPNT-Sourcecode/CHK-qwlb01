import collections

# noinspection PyUnusedLocal
# skus = unicode string

class CalculateShop:

    def __init__(self, skus):
        self.skus = skus
        self.items = None



    def validateInput(self, input) -> bool:
        if not isinstance(input, str):
            return False
        

    def countSKUS(self) -> None:
        self.items = collections.defaultdict(int)

        for i in self.skus:
            self.items[i]+=1



def checkout(skus):
    




