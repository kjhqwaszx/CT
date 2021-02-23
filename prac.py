# 3
# 1 0
# 5
# 4 2
# 1 2 3 4
# 6 0
# 1 1 9 1 1 1

# 1
# 2
# 5

#### 1999_bak

def printerQueue():
    testCase = int(input('testCase를 입력해주세요 : '))
    
    result = []
    for i in range(testCase):
        count = 0
        n, index = list(map(int,input().split(' ')))
        queue = list(map(int, input().split(' ')))

        # index와 함께 queue 튜플로 묶어주기
        queue = [(p,idx) for idx, p in enumerate(queue)]
        
        while True:
            if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
                count += 1
                #우선순위가 높은 프린트 요청일 경우
                if queue[0][1] == index:
                    #궁금했던 인쇄 요청인 경우
                    result.append(count)
                    # print(count)
                    break;
                else:
                    queue.pop(0)
            else:
                queue.append(queue.pop(0))
    print(result)

printerQueue()
