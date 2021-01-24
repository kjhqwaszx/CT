#1874_스택수열
def isStack():
    n = int(input())
    
    stack = []
    result = []
    count = 1

    for i in range(1, n+1):
        data = int(input())

        while count <= data:
            result.append('+')
            stack.append(count)
            count += 1
            
        if stack[-1] == data:
            result.append('-')
            stack.pop()
        else:
            print('NO')
            exit(0)
    print('\n'.join(result))

isStack()