print('DZ21')


def popular_words (text, words):
    tempList = text.lower().split()
    tempRes = {}
    for value in words:
        tempRes[value] = tempRes.get(value, 0)
        for word in tempList:
            if word == value:
                tempRes[value] = tempRes.get(value, 0) + 1
    return tempRes


print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']))
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')

print('Thank you for using')