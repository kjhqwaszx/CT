< python >
print함수
 * 방법 1
  -  print() 에서 '+'연결 시 정수형은 문자열 처리를 주어야 한다.  str(변수명)
  -   ' , ' 로 연결할 경우 상관없다. 대신 공백이 추가됨 ( sep="" 추가시 공백 x )
 * 방법 2
  - print("나는 %d살입니다." % 20)
  - print("나는 %s을 좋아해요." % "파이썬")
  - print(" Apple은 %c 로 시작해요." % "A")
  - print("나는 %s 색과 %s색을 좋아해요" %("빨강", "파랑")
 * 방법3
  - print("나는 {}살입니다." .format(20))
  - print("나는 {}색과 {}색을 좋아해요.".format("파랑","빨강")
  - print("나는 {0}색과 {1}색을 좋아해요.".format("파랑","빨강")  ### 주로 많이 사용
  - print("나는 {age}살이며, {color}색을 좋아해요".format(age=20, color="파랑")

 * 방법4 ( python v3.6이상)
    age = 20
    color = "빨강"
    print(f"나는 {age}살이며, {color}색을 좋아해요")

슬라이싱
id="012345-789abcd"
print("id : " + id[0:2]) # index 2 전까지 갖고온다 ( 0, 1 출력)
-> id[ 0:2 ] = id[ :2 ] # 처음부터 시작할 경우 0 생략가능
(01 출력)
-> id[ 7:14 ] = id[ 7: ]  # 맨 마지막까지 출력할경우 생략가능
= id[ -7: ] #뒤에서부터 카운트해서 가져오는경우 d= -13, c=-12 ... 7 = -7 
 ( 모두 789abcd 출력된다 ) 

문자열함수
  - 문자열.lower() : 전체 소문자
  - 문자열.upper() : 전체 대문자
  - 문자열[0].isupper() : 문자열 인덱스가 대문자?
  - len(문자열) : 문자열 길이
  - 문자열.repalce("변경할 단어", "단어") : 대치
  - 문자열.index("단어") : 해당 단어(문자) 위치, 문자가 없으면 에러
     -> = find로도 가능, find 는 찾을 문자가 없으면 return -1
index = name.index("n") # String에서 n 위치
print(index)
index = name.index("n",index+1) #String에서 두번째 n위치
print(index)
  - 문자열.count("n") # 문자열 속  n의 개수


배열( list )
subway = [10, 20, 30]
addList = ["a","b","c"]
  - subway.append(40)  : 배열 끝에 추가   ( 10, 20, 30, 40)
  - subway.insert(1,15) : index에 값 추가 ( 10, 15, 20 ,30 ,40)
  - subway.pop() : 배열 끝에서 제거 (10, 15, 20, 30)
  - subway.count(10) : 배열속 10 의 갯수
  - subway.sort() : 오름차순 정렬
  - subway.revesr() : 배열 뒤집기 ( 내림차순 정렬 아님 )
  - subway.clear() : 배열 초기화
  - subway.extend(addList) : addList 배열을 뒤에 붙인다

객체
cabinet={
  1: "유재석",
  2: "김태호"
  "A-1" : 하하
}
  - print( cabinet[1] ) : 유재석     #키 값이 없을 경우 에러
  - print( cabinet["A-1"] ) : 하하    #키 값이 없을 경우 에러
  - print( cabinet.get(1) ) : 유재석  # 키값이 없을경우 None 출력
  - cabinet.get(1,"사용가능") : 키값이 없을경우 사용가능 출력
  - print( 3 in cabinet ) : 키값 3이 존재하는지 ( True 출력 )
  - cabinet["A-10"]="정형돈" : A-10 키값으로 정형돈 추가, 이미 키값이 있으면 업데이트
  - del cabinet["A-1"] : key , val 삭제
  - print( cabinet.keys()) : 객체 키값 출력
  - print( cabinet.values()) : 객체 값 출력
  - print( cabinet.items()) : 객체 키, 값 출력
  - cabinet.clear() : 객체 초기화

튜플 (tuple) : 객체처럼 변경이 불가능하다.   
menu = ("돈까스", "치즈까스")
(name, age, hobby) = ("유재석", 25, "코딩")  : 튜플 만들기

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



