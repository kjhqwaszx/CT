def isSorted():
    arr = list(map(int, input().split(' ')))

    if arr == sorted(arr):
        print('acending')
    elif arr == sorted(arr, reverse=True):
        print('decending')
    else:
        print('mixed')
isSorted()