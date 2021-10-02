nums = list(range(97, 123))

word = input()

for i in nums:
    print(word.find(chr(i)), end=' ')
