def points(games):
    result = 0
    for i in games:
        if i[0] > i[2]:
            result += 3
        elif i == i[2]:
            result += 1
    return result 
