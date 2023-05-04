case = int(input())
for _ in range(case):
    sentence = list(input().split())
    for word in sentence:
        word = list(word)
        word.reverse()
        print(''.join(word), end=' ')
    

    # string = list(input().split())
    # for word in string:
    #     print(word[::-1], end=' ')

