import collections

# noinspection PyUnusedLocal
# skus = unicode string
def validateInput(input) -> bool:
    if not isinstance(input, str)

def countSKUS(skus) -> dict:
    items = collections.defaultdict(int)

    for i in skus:
        items[i]+=1

    return items

def checkout(skus):
    


