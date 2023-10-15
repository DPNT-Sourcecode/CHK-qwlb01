import collections

# noinspection PyUnusedLocal
# skus = unicode string

class CalculateShop:
def validateInput(input) -> bool:
    if not isinstance(input, str):
        return False
    

def countSKUS(skus) -> dict:
    items = collections.defaultdict(int)

    for i in skus:
        items[i]+=1

    return items



def checkout(skus):
    



