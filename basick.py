# 값 입력
a = int(input())

#줄바꿔 list 출력
arr = ['a', 'b', 'c']
print('\n'.join(arr))

#배열 > 인덱스와 함께 튜플형식으로 저장 (이너멀에이드)
arr = [1, 2, 3, 4]
arr = [(i, idx) for idx, i in enumerate(arr)]
print (arr)
