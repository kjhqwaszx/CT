#1966_프린터 큐
def printerQueue():
    test_case = int(input())
    
    for i in range(test_case):
        n, index = list(map(int,input().split(' ')))
        queue = list(map(int,input().split(' ')))
        # 인덱스와 함께 list에 저장
        queue = [(j,idx) for idx, j in enumerate(queue)]
        count = 0

        while True:
            # Printer 에서 우선순위가 가장 높은 문서인지
            if queue[0][0] == max(queue,key=lambda x:x[0]) [0]:
                count += 1
                #우리가 뽑고자하는 문서인지
                max()
                if queue[0][1] == index:
                    print(count)
                    break
                else:
                    queue.pop(0)
            else:
                queue.append(queue.pop(0))

printerQueue()