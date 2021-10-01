from collections import Counter

words = input()
words = words.upper()
words = list(words)
words = Counter(words)

countValue = words.most_common()
# print(countValue)
originalValue = countValue[0][1]
if len(countValue) > 1:
    duplicateValue = countValue[1][1]
    if originalValue == duplicateValue:
        print('?')
    else:
        print(countValue[0][0])
else:
    print(countValue[0][0])
#    max()
