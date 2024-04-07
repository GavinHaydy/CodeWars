def beeramid(bonus, price):
    levels = 0
    beers = bonus // price
    if bonus < price:
        return 0
    while beers >= levels ** 2:
        beers -= levels ** 2
        levels += 1
    return levels -1


""" best
def beeramid(bonus, price):
    beers  = bonus // price
    levels = 0
    
    while beers >= (levels + 1) ** 2:
        levels += 1
        beers  -= levels ** 2
    
    return levels
 """
