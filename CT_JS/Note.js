// DFS
// 재귀호출 방식으로 DFS 함수는 if, else 로 구성한다.
// if문에는 break point, else에는 조건에 따라 재귀 호출

//else에 작성되는 내용은 하나의 노드에서 뻗어나가는 경우들이다.

// 부분집합을 이용해서 문제를 풀 경우는 else 에서 재귀 두번호출 ( 포함할지, 포함하지 않을지)
// if의 break 조건은 모든 노드를 갔다온 경우 -> 포함관계(부분집합) 형성 후 계산

// 수열을 이용해서 문제를 풀 경우에는 else for문을 통해 노드갯수만큼 재귀호출 .
// if의 break 조건은 문제에 따라.

function DFS(v){ // 부분집합구하기
    if(v === n+1){
        let tmp = ""
        for(let i=1; i<=n; i++){
            if(ch[i]===1) tmp+= i +' '
        }
        if(tmp.length > 0) answer.push(tmp.trim())
    }else{
        ch[v]=1
        DFS(v+1)
        ch[v]=0
        DFS(v+1)
    }
}
function DFS(i,sum){ // 합이같은 부분집합
    if(flag) return
    if(i===arr.length){
        if(sum===total-sum){
            answer="Yes"
            flag=1
            return
        }
    }else{
        DFS(i+1,sum+arr[i])
        DFS(i+1,sum)
    }
}
function DFS(i,sum) { // 배열의 합중 c에 가장 가까운 합 ...
    if(sum > c) return
    
    if(i===arr.length){
        if(answer<sum){
            answer=sum
            return
        }
    }else{
        DFS(i+1,sum+arr[i])
        DFS(i+1,sum)
    } 
}
function DFS(x,y){ //미로탐색
    if(x===6 && y===6){
        answer++
    }else{
        for(let k=0; k<4; k++){
            let nx = x+dx[k]
            let ny = y+dy[k]

            if(nx>=0 && nx<=6 && ny>=0 && ny<=6 && board[nx][ny]===0){
                board[nx][ny]=1
                DFS(nx,ny)
                board[nx][ny]=0
            }
        }
    }
} 

//BFS
// queue를 사용하고 while(queue.length)을 사용한다.
// while 안에서는 let v = queue.shift() 를 통해 연결된 값을 조건에 맞게 넣어준다.
while(queue.length !== 0){//이진트리탐색
    let v = queue.shift()
    answer += (v+" ")
    for(let nv of [v*2, v*2+1]){ // nv는 v*2 와 v*2+1 두번 돈다.
        if(nv>7){
            continue; // 값을 넣지 않겠다.
        }
        queue.push(nv) // 연결된 값들을 넣는다.
    }
}
while(queue.length){ //송아지찾기
    let x = queue.shift()
    for(let nx of [x-1, x+1, x+5]){
        if(nx===e) return dis[x]+1  // 도착지점 도달. return 이전 좌표 방문횟수+1 
        if(nx>0 && nx<10000 && ch[nx]===0){
            queue.push(nx)
            ch[nx]= 1;
            dis[nx] = dis[x]+1
        }
    }
}

// for of 구문 ( 문자열의 경우 문자 하나하나)
    arr = [1,2,3] 
    for(let  x of arr ){
        console.log(x) // 1,2,3이 찍힌다.
    }
    str = "abcd"
    for(let x of str){
        console.log(x) // a,b,c,d
    }

// 최대, 최솟값 내장함수
 - Math.max(1,2,3,4,5), Math.min(1,2,3,4,5)
    
    arr = [1,2,3,4,5]
    Math.min(...arr)  // ... 를 붙여주면 arr[0], arr[1], arr[2] 이런식으로 펼쳐 들어간다.
    Math.max(...arr)
    
// #### String ####

//replace( word|type, newWord )
str="abcda"
str.replace('a','A') // Abcda
str.replace(/a/g,'A') // AbcdA
str.replace(/a/i, 'A') // Abcda
str.replace(/[^a-z]/g,'') // 알파벳 소문자가 아니면 뺀다.

//toUpperCase , toLoserCase()
str = "abcd"
str.toUpperCase()
str.toLowerCase()

//trim 양 끝 공백을 제거
str = " abc "
str.trim() // abc

//substr(startIndex, length) , substring(startIndex,endIndex)
//자른 문자열을 return 한다.
//length가 없으면 start부터 전체 다 출력
//start가 음수면 뒤에서부터 count
str = "abcdef"
str.substr(2) // cdef 
str.substr(-2) // ef
str.substr(1,3) // bcd
str.substring(1,3) // bc ( 3 전까지)


//charCodeAt() , Char를 아스키코드 값으로
//대문자 : 65 ~ 90
//소문자 : 97 ~ 122
for(let x of str){
    x.charCodeAt
}

//isNaN
answer=""
str = 'a10db'
for(let x of str){
    //숫자만 answer에 저장
    if(!isNaN(x)) answer+=x
}

// #### Array ####

//배열 초기화
let n = 5
let arr = Array.from( {length:n},()=>1 ) // 1,1,1,1,1
let queue = Array.from({ length: n }, (v, i) => i + 1) // 1,2,3,4,5

//forEach(el => {func})
let arr = [1,2,3,4]
arr.forEach(el=>console.log(el)) // 1,2,3,4,5

//arr.slice()  얕은 복사로 메모리 주소가 아닌 값만 복사해온다.
let arr = [1,2,3,4]
let arr_cpy = arr.slice() // [1,2,3,4]

// push, pop, shift, unshift
arr = []
arr.push(1) // 1
arr.push(2) // 1,2
arr.push(3) // 1, 2, 3
arr.pop() // 1,2
arr.shift() // 2
arr.unshift(0,1) // 0,1,2

//splice(start,[deleteCount],[value])
arr = [1, 2, 3, 4, 5]
arr.splice(0, 1) // 2,3,4
arr.splice(4, 0, 4.5) // 1,2,3,4,4.5,6

//filter(v => 조건 )
str = ["good", "time", "good", "time", "student"];
// 1. 문자 길이
answer = str.filter(v => v.length > 6)
// 2.중복단어 제거
answer = str.filter((v, i) => {
    //처음 발견된 문자의 index가 자신의 index면 push
    if (str.indexOf(v) === i) return v
})

//회문구조 파악 ( 내부함수 사용)
//split, reverse, join
// * reverse (reverse는 배열에서만 가능하다 ( 문자열 x))

let str = "abcd"
str=str.split('') // char 배열로 저장된다.
str.split('').reverse() // 배열 뒤집기
str.split('').reverse().join('') // 다시 스트링으로 만든다.

//reduce((accumulator,currnetValue) => func, initValue )  **accumulator : 누적
// func의 결과를 accumulator에 저장
// 각 배열의 원소들에대해 callback을 실행하며 하나의 출력결과를 만든다.

// 1. 각 배열의 합
let arr =[1,2,3,4,5]
let sum = arr.reduce((acc,cur)=>acc+cur,0)

//2. 최대값 구하기
let arr = [1,2,3,4,5]
let answer = arr.reduce((max,cur)=>Math.max(max,cur),0)

//findIndex 
let arr = [1,2,3,4,5]
index = arr.findIndex(el=>el==3) // 2

//sort
let arr = [1,4,2,3]
arr.sort()// 오름차순
arr.sort((a,b)=>b-a) // 내림차순

//includes(value[, fromindex])
arr = [1,2,3,4]
arr.includes(3) // true
arr.includes(5) // false
arr.includes(3,1) // false
arr.includes(4,-1) //true



// #### Set ####
// set 구조체는 중복값을 담지 않는다.

let tmp = new Set()
tmp.add(card[i] + card[j] + card[k]) // 중복값이 있을경우 넣지 않는다.
let arr = Array.from(tmp).sort((a,b)=>b-a) // 배열로 만든 후 내림차순 정렬

tmp.add(3) 
tmp.delete(3) // 3제거
tmp.clear() // 초기화

// #### Map ####
// [key,value] 형식으로 저장되는 객체
// set(key,value), get(key), has(key)
let sH= new Map()
sH.has('a') // false
sH.set('a',1)
sH.set('a',sH.get('a')+1) 
sH.get('a') // 1
sH.has('a') //true



// #### Tip ####

//1. 숫자 뒤집기
arr=[23,32,55,123,100]
re_arr=[]
for(let x of arr){
    re_arr.push(Number(x.toString().split('').reverse().join('')))
}
//2, 배열에서 중복 숫자 제거
str = [1,2,3,3,4,5];
answer = str.filter((v, i) => {
    //처음 발견된 문자의 index가 자신의 index면 push
    if (str.indexOf(v) === i) return v
})



///  #### 자바스크립트 상속과 프로토타입 ( https://shlee1353.github.io/2019/07/05/js-prototype-inheritance/ )

// 자바스크립트는 클래스라는 개념대신 기존의 객체를 복사하여 새로운 객체를 생성하는 프로토타입 언어이다.
// prototype은 자신을 원형으로 만들어질 새로운 객체들에게 줄 속성
// proto는 prototype에 대한 정보이다.
// 함수를 정의하면 함수와 연결되는 prototye Object도 함께 생긴다.
// 즉, Prototype Object는 자기 자신의 분신이며 다른 객체가 참조할 프로토 타입이 된다.

function Person(){}
var joon = new Person();
var jisoo = new Person();

Person.prototype.getType=function(){
    return "사람"
}
console.log(joon.getType()) // 사람
console.log(jisoo.getType()) // 사람



