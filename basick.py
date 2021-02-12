# 파이썬 기본 개념정리
# https://wikidocs.net/book/1553

# 값 입력
a = int(input())
arr = list(map(int,input().split(' ')))

#줄바꿔 list 출력
arr = ['a', 'b', 'c']
print('\n'.join(arr))

#배열 > 인덱스와 함께 튜플형식으로 저장 (이너멀에이트)
arr = [1, 2, 3, 4]
arr = [(i, idx) for idx, i in enumerate(arr)]
print (arr)


# set와 tuple 개념 잡기

# $ git config --global user.name "jaehan.kim"

# $ git config --global user.email "mju6013@naver.com"


# $ git config --global --list
