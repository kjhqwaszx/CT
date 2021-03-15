# 파이썬 기본 개념정리
# https://wikidocs.net/book/1553
# https://wikidocs.net/2

#파이썬 유용한 코드
# https://velog.io/@johnque/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9C%A0%EC%9A%A9%ED%95%9C-%EC%BD%94%EB%93%9C%EB%93%A4
# https: // dailyheumsi.tistory.com/67

# Scalar Type
int, float, bool, None

#print 함수
print("나는 {0}색과 {1}색을 좋아해요.".format("파랑","빨강")  ### 주로 많이 사용


# while
while c != 0:
      실행문

#  **** String ****                                                   *********

# 문자열.lower() : 전체 소문자

# 문자열.upper() : 전체 대문자

# 문자열[0].isupper() : 문자열 인덱스가 대문자?

# len(문자열) : 문자열 길이

# 문자열.repalce("변경할 단어", "단어") : 대치

# 문자열.index("단어") : 해당 단어(문자) 위치, 문자가 없으면 에러
#   -> = find로도 가능, find 는 찾을 문자가 없으면 return -1

# index = name.index("n") # String에서 n 위치
# index = name.index("n",index+1) #String에서 두번째 n위치

# 문자열.count("n") : 문자열 속  n의 개수

# join : 문자열을 합치는데 사용한다. 구분자가 앞에 붙음
# ','.join(['a','b','cd']) => a,b,cd

# split : 문자열을 구분자로 나누어 list로 반환한다.
# 'a,b,cd'.split(',') => ['a','b','cd']

# partition : 구분자로 나누어 튜플 형식으로 반환한다.
# departure, _, arrival = "Seattle-Seoul".partition('-')
# (departure,'Seattle'), (_,'-'), (arrival,'Seoul')

# List :순서가 있는 수정가능한 객체의 집합 

# **** List 함수 ****                                                 **********

# copy : list를 복사한다.
# arr_c = arr.copy()

# arr.index(val) : 리스트 안에서 해당 아이템이 index를 출력한다.
# a = ['서울','인천','제주','대전']
# a.index('인천') => 1

# arr.count(val) : 리스트 안에서 매칭되는 갯수를 출력한다.
# a = [1,2,3,3,4,5,6]
# a.count(3) => 2

# a.pop() : 배열 끝에서 제거 (10, 15, 20, 30)
# a.pop(index) : 배열의 index를 return하고 삭제 

# a.clear() : 배열 초기화

# a.extend(addList) : addList 배열을 뒤에 붙인다

# val in arr : 리스트안에 포함되어있는지 확인가능 (bool)
# a= [1,10,100]
# 1 in a => True  ,  30 in a => False

# append(val) : 원소를 리스트 마지막에 추가
# a = [1,2,3]
# a.append(4) = > a= [1,2,3,4]

# insert(index,val) : 원하는 index에 원소를 추가
# a = [1,3,4,5]
# a.insert(1,2) # [1,2,3,4,5]

#  del a[1] : a의 index 1 원소를 삭제

# a.remove(val) : a의 첫번쨰 val을 삭제

# a.reverse() : 리스트를 거꾸로 뒤집는다.

# a.sort() : 오름차순 정렬

# a.sort(reverse=True) : 내림차순 정렬
# a.sort(key=len) : 정렬 기준을 정할 수 있다.(오름차순)
# => ["일", "일이", "일이삼"]



# Dictionary : key : value 로 구성된 집합
# **** Dictionary ****                                                  ***********
#   dic = {
#           name:'jaehan'
#         }

# dic[key] : 해당 key 값의 value 출력 ( key가 없으면 오류)

# dic[key]=val -> key : value 추가

# dic.get(key) : 해당 key 값의 value 출력 ( key가 없으면  None)
# dic.get(key,val) : 해당 key값이 없으면 val값으로 출력 ( val추가는 아니다. )



# del dic[key] : key 삭제 

# keys = list(dic.keys()) : 딕션어리의 key들을 list로 출력한다.
# values = list(dic.values())
# key_val = list(dic.items())

# key in dic : 딕션어리 안에 key값이 있는지 ( bool )


# 튜플 : List와 비슷하지만 값을 변경할 수 없다. ( ) 로 감싸져있다.

#  ***** Tuple *****                                                                *********

# t1 = (1,)  : 하나의 요소를 갖는 경우에는 마지막에 , 를 붙여주어야 한다.

# 요소를 삭제하거나 변경 시 에러 발생 ( del[0], t1[0] = 1 불가능 )

# t1 = (1,2,'a',b')
# t2 =('c','d')
# t[0] ->1     t[2] -> 'a'

# t1+t1 -> (1,2,'a','b',c','d')  #### 튜플 요소 추가는 가능

# (name,age,addr) = ('jaehan', 25, 'seoul')
# print(name) -> 'jaehan', print(age) -> 25, print(addr) ->'seoul'


# ***** set *****                                                                                     ****************
#  중복된 요소를 갖지않는다. 순서가 없다.

#s1=set('hello')
#print(s1) -> {'e','h','l',o}     ## l 중복 X

# set : 순서가 없고, 중복


세트 (set) : 중복x, 순서 없음
my_set = { 1,2,3,3,3 }
your_set = {2,4,5}            ==    your_set = set( [2,4,5 ] )
  - print(my_set) : 1,2,3 으로 출력됨
  - print(my_set& your_set) : 교집합
  - print(my_set | your_set) : 합집합
  - print(my_set - your_set) : 차집합
  - my_set.add( 4 ) : 세트에 추가
  - my_set.remove( 4 ) 세트에서 삭제

조건문( if )

if 조건1-1 or 조건1-2 :
    작업내용
elif 조건2 :
    작업내용
else:
    작업내용
( ** 0< temp <= 10 -> and 조건 없이 이렇게 가능 )
( 조건이 변수 in 리스트 가능하다. ) -> if temp in [10,20,30] : 

반복문(for)
  for 변수 in range(5):      == for 변수 in [0,1,2,3,4] :
    print(변수)     # 0,1,2,3,4

  - 한줄 for
    students = [1,2,3,4,5]
    students = [i+100 for i in students]   # [101, 102, 103, 104, 105]

    name_len = ["a", "ab", "abc"]
    name_len =  [len(i) for i in name_len] #[1, 2, 3]

함수
  - 함수선언
def 함수명 ():
  내용

  - 기본값
def profile(name , age=24, main_lang="python"):
    내용 
=> age와 main_lang을 받지 않으면 기본값으로 세팅

 - 가변인자

1)
 def profile(name, age, lang1, lang2, lang3, lang4, lang5):
     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") #end =""는 줄바꿈 x
     print(lang1, lang2, lang3, lang4, lang5)
2) language 를 가변인자로 설정 
def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "python", "java", "c", "c++","c#")
profile("김태호", 20, "python", "java") ## 1번 함수의 경우 에러발생

  - 전역변수 사용
gun =10

def checkpoint(soldiers):
    global gun  # global 로 전역변수 접근 
    gun = gun-soldiers

checkpoint(2)
print("남은 총 : {0}".format(gun)) 

표준입출력
  - 출력 
1) .ljust(num), .rjust(num)
for subject, score in scores.items():
     print(subject.ljust(8), str(score).rjust(4),sep=":")    # ljust(8) : 8공간을 확보하고 왼쪽 정렬 

2) .zfill(num)
for num in range(1,21):
     print("대기번호 : " + str(num.zfill(3)) # zfill(3) : 3자리이고 자리가 남으면 앞부터 0으로 채운다. 001 002 003 ...

# 총 10자리 공간을 확보 한 후 빈 자리는 공백으로 두고 오른쪽정렬
print("{0: >10}".format(500))

# 양수일 경우 +, 음수일경우 - 로 표시
print("{0: >+10}".format(-500))

# 왼쪽 정렬하고, 빈칸은 _로 채움
print("{0:_<+10}".format(500))

# 3자리 마다 콤마를 찍기
print("{0:,}".format(1000000000))

# 3자리 마다 콤마를 찍기 ( 부호 포함)
print("{0:+,}".format(1000000000))

#소수점 출력 ( 둘째자리까지 표현)
print("{0:.2f}".format(5/3))

- 파일 입출력 : 파일을 open 하면 반드시 close 해주어야한다.
score_file = open ("score.txt", "w", encoding="utf8") # 쓰기모드

print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8")  # append 모드 ( 이어서 쓰기 )
score_file.write("과학: 80")
score_file.write("\n코딩: 80")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")  # append 모드 ( 이어서 쓰기 )
print(score_file.read())
score_file.close()



