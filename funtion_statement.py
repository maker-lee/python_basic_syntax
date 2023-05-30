
# # 로직의 연산을 재사용하기 위해 만드는 함수 
# # 리턴값 , input값은 있어도, 없어도 상관없다. 
# # 함수를 호출할 때는 함수명(input)으로 한다. 

# def myFunc(myInput) :
#     calc = 20 * (myInput + 10) ** 2
#     return calc

# def myPlusFunc(num) :
#     answer = 0
#     for i in range(1,num+1) :
#         answer += i 
#     return answer 

# #print(myPlusFunc(100))


# def plusTwo(num1,num2) :
#     return ((num1 + num2) + 2 )* 2
# result = plusTwo(1,2)


# num_list = [1,4,6,9,4]

# def my_index2(list1,num1)  :
#     result = 0
#     for a in range(len(list1)) :
#         if list1[a] == num1 :
#             result = a
#             break 
#     print(result)
    
# my_index2(num_list,9) 
# r1 = my_index2(num_list,9) 
# print(r1) # 내부에 print()가있으면 none값이출력된다.

# import math
# # 원의 넓이를 구하는 함수 만들기
# radius = int(input('반지름의 길이를 입력하세요'))  
# def area(radius) :      
#     return round(radius ** 2 * math.pi,3)
# print(area(radius))


# def hello1() :
#     print('hello1 python!')

# def hello2() :
#     return 'hello2 python!'

# hello1()
# print(hello2())

#args는 arguments의 약자로 '인수'(파라미터)

# def sum(*args) : # 매개변수의 개수를 정하고 싶지 않을때 
#     result = 0
#     for i in args :
#         result += i
#     return result
# print(sum(1,2,3,4,5))

# def cla(a,b,c='plus') : # 리턴값이 여러개 있는 경우 튜플타입으로 생긴다.
#     if c  == 'plus' :
#         result = a+b
#     elif c  == 'minus' :
#         result = a-b 
#     elif c  == 'multiply' :
#         result = a*b
#     return result

# # calvalue =cla(1,2)
# # print(f'계산한 첫번째 값은 {calvalue[0]} 두번째 값은 {calvalue[1]} 세번째 값은 {calvalue[2]}')

# print(cla(1,2,'plus'))
# print(cla(1,2,'minus'))
# print(cla(1,2,'multiply'))
# print(cla(1,2)) # 매개변수를 주지않아도 돌아간다, 기본값을 주었기때문

# # 매개변수의 순서를 안맞추고도 원하는 매개변수의 자리에 값을 넣어 함수를 호출하는 방법
# def whoareyou(name,age,gender) :
#     print(f'제이름은 {name}이고 나이는 {age},이고 성별은 {gender}')
# whoareyou(age=12,gender='man',name='david')

# print('hello ',end='')
# print('world')

# # 지역변수(함수 내)와 전역변수(함수 밖) 
# c = 0
# a = 100
# def sum(a,b) : # 함수 안에서 사용되는 변수명으로, 함수 내에서만 유효하다
#     # 함수 내에서 함수 밖의 전역 변수를 사용하려면 global 키워드를 사용한다. 
#     global c
#     result = a + b + c
#     return result 
# result = sum(a,10)
# print(result)

# # print(a)
# 저장되는 메모리 위치가 달라서, 함수안의 변수는 밖에 영향을 끼치지 못한다.

# result = 0
# def sum(a) :
#     global result
#     result += a
#     return result 
# print(sum(10))

# num_list = [10,20,30,40]
# for a in range(len(num_list)) :
#     print(a)
# for a in range(len(num_list)) :
#     print(a)
# print(a)



# 저장 메모리와 객체 복사

# 객체는 힙 메모리 영역에저장되는데, 함수 내에서도 접근하여 추가/수정이 가능하다
# 스택 영역에 있는 지역변수는 함수가 끝나면휘발되지만, 힙메모리는 휘발되지않는다.
# list1 에 list2 를 담으면 객체의 주소가 복사 되므로 동일한 데이터를 가지게 된다.
# id() 함수를 쓰면 주소를 알 수 있다. 

# list1 = [1]
# list2 = list1
# list3 = list1[:]
# list4 = list1.copy() # import copy 의 copy.copy와 같다. 
# print(id(list1)) # 2800320891968 같
# print(id(list2)) # 2800320891968 같
# print(id(list3)) # 2975228342528 달
# print(id(list4)) # 2395836937088 달

# import copy
# list5 = copy.copy(list1) # 얕은복사로 객체안의 객체의값은 메모리 주소로 복사된다. 
# print(id(list5)) #2097480209856 달

# list6 = copy.deepcopy(list1)
# print(id(list6)) # 1219324331392 (주소가 완전 달라짐)

# # 깊은 복사는 copy.deepcopy를 사용하여 객체의 객체도 모두 value로 복사된다.
# list1.append(2)

# print(list1)
# print(list2)
# print(list3)
# print(list4)
# print(list5)


# def mySort(num_list) : # 객체는 원본 메모리에 접근해서 원본을 바꿈
#     for i in range(len(num_list)-1) :
#         for j in range(i+1,len(num_list))  :
#             if num_list[i] > num_list[j] : 
#                 num_list[i], num_list[j] = num_list[j], num_list[i]
#     #return num_list

# lista = [5,1,2,3,6]
# mySort(lista)
# print(lista)


# 람다함수 : (1) 함수를 간편하게 표현 (2)함수를 변수에 담기 위함

# lambda 매개변수 : 실행문

# # 예시 
# def add(a,b) :
#     return a+b
# print(add(1,2))

# add_lambda = lambda a,b : a+b
# print(add_lambda(1,2))

# mul = lambda a : a*a
# print(mul(5))

# cal_list = [lambda a,b : a+b,lambda a,b : a-b,lambda a,b : a*b,lambda a,b : a/b]
# print(cal_list[1](1,2))

# # lambda로 입력한 매개변수가 짝수면 True 홀수라면 False
# oddOrNot = lambda x : True if x % 2 == 0 else False 


# # map 함수 : 이터러블 자료를 하나씩 꺼내어 함수가 수행한 결과 값을 객체로 리턴한다. 
# print(list(map(mul,[1,2,3,4])))
# print(tuple(map(lambda x : x **2,[1,2,3,4])))

# # filter() 함수 참/거짓 조건으로 참인 값을 걸러내는것
# def toN(x) :
#     if x < 0 :
#         return True 
#     else :
#         return False

# lista = [1,2,-1,-3,-4]
# print(list(filter(toN,[1,2,3,0,0,-1,-3,-4])))

# # 삼항연산자 
# a = [i for i in lista if i < 0] # [-1, -3, -4]
# a = list(filter(lambda x : True if x < 0 else False,lista)) # [-1, -3, -4]
# a = list(map(lambda x : True if x < 0 else False,lista)) # [False, False, True, True, True]



# lista = [4,7,1,2,5,6,8]
# answer = list(filter(lambda x : True if x % 2 != 0 else False,lista))
# print(sum(answer))

# # 문자를 아스키코드로 변환
# print(ord('a')) #97
# print(chr(97)) # 아스키코드를 문자로 변환


# # 절대값 abs()
# answer =list(map(abs,[1,-32,-32,-21,-5]))
# print(answer)



# 재귀함수
# factorial 예제 10! 

# 예제 , 변수 n을 넣었을 때 n!가 나오도록

# n = 4

# def fac(n) :
#     sumF = 1
#     for i in range(1,n+1) :
#         sumF *= i
#     return sumF
# print(fac(4))

# # 재귀함수란, 함수 내에서 함수를 호출하는 것.
# # 반드시 종료 조건이 들어가야 한다 안그러면 무한루프됨 
# def test1(n) :
#     return n + test(n-1) # 무한루프

# def test(n) :
#     if n == 1 : 
#         return 1 # 1을 돌려줌 
#     return n + test(n-1) # 10+9+8+7+6+5+4+3+2 #1은 if문으로 더해줘 
# print(test(10))

# def fact(n) :
#     if n == 1 :
#         return 1
#     return n * fact(n-1)
# print(fact(4))


# # 예제
# lista = [10,20,30,40,50]
# # 다섯개중에 2개씩 숫자를 추출하는 경우의 수

# # 정답 
# import math
# print(math.comb(5,2))

# # for문 정답 
# list = [] 
# for i in range(len(lista)) :
#     for j in range(i+1,len(lista)) :
#         list.append([lista[i],lista[j]])
# print(list)

# # 재귀함수 정답 ?????
# def fac_C(lista) :
#     list = []
#     if :
#         for i in range(len(lista)) :
#             for j in range(i+1,len(lista)) :
#                 list.append([lista[i],lista[j]])
#     return list 

# def fact(n) :
#     if n == 1 :
#         return 1
#     return n * fact(n-1)
# print(fact(4))


# 카운트 재귀함수 
def counter(n) :
    if n == 1 :
        return 1 # 종료 조건
    else :
        return str(counter(n-1)) + " " +str(n)
print(counter(5))