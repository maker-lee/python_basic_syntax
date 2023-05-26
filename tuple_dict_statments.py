# # 튜플

# t1 = 1,2,3,[3,3,4]

# print(type(t1[3]))
# print(t1)


# 딕셔너리


# print(dic1)

dic1 = {'이름':'홍길동','나이':25,'직업':'도둑','성별':'남자'}

a = dic1.items()




# keylist = []
# valuelist = []
# for i in dic1.keys():
#     keylist.append(i)
#     valuelist.append(dic1[i])
# print(keylist,valuelist)


# blood = ['A','A','B','O','O','AB','AB']

# dic_b = {}

# # 빠른 방법
# for a in blood :
#     if a not in dic_b.keys() :  # 모든 혈액형을 계속 검사하지 않도록 함
#         dic_b[a] = 1
#     else :
#         dic_b[a] += 1 # 카운트를 사용하지 않아서 조회 속도가 빠름 
# print(dic_b)

# # 두번째로 빠른방법
# for a in blood :
#     if a not in dic_b.keys() : 
#         dic_b[a] = blood.count(a) # count는 조회에 시간이 오래 걸림
# print(dic_b)

# # 짧은 방법 ㅋㅋ 
# for i in blood :
#     dic_b[i] = blood.count(i) 
# print(dic_b)


# # set 
# s1 = {'이름','나이','성별'}
# s2 = set('test')
# print(s1)
# print(s2)

# blood = ['A','A','B','O','O','AB','AB']

# # 반 학생들의 혈액형 종류는 몇개인가?
# print(len(set(blood)))


# s1 = set([1,2,3,4,5])
# s2 = set([4,5,6])
# s1.update(s2)
# print(s1)

# 최대값 구하기 / 최소값 구하기

# lista = [100,20,30,5,90,-10]

# lista.sort()
# listb = []
# for a in (lista[::-1]) :
#     listb.append(a)
# print(listb)


# print(lista[::-1])


# # 단, maxA 사용 안하기, sort 사용 안하기

# # maxA = lista[0]
# # minA =lista[0]
# # for i in lista :
# #     if i > maxA :
# #         maxA = i
# #     elif i < minA :
# #         minA = i
# # print(maxA,minA)
    

# lista.sort()
# print('작은수',lista[0])
# print('큰수',lista[-1])
    

# # if 문
# a = 10
# if (a>5) | (a>100) :
#     print('참')
# if a > 5 or a > 100 :
#     print('참2')

# 비트 연산이란 2진법의 숫자를 or and xor등으로 CPU 내부적으로 계산하는 방식을 말함

# and 는 &와 같고 or는 |ㅇ와 같고 not True는 Flase가 되고 not False는 True


# print(10 | 1) # 11 
# print(10 & 1) # 0   
# print(10 or 1) # 10 이거나 1이니까 ㅇㅋ 맞으니까 10 


# 숫자는 정수(2진수, 10진수, 16진수), 실수와 관계없이 0이면 거짓, 0이 아닌 수는 참입니다.
#문자열은 내용이 있을 때 참, 빈 문자열은 거짓입니다.

# # if문 한줄로 쓰기
# a =10 
# if a > 1 : print('a는 1보다 크다') ; print('두줄쓰기')
# 출력 : a는 1보다 크다 두줄쓰기


# # 조건부 표현식
# # if 문의 실행문을 if 문 앞으로, : 는 쓰지 않는다.
# A=10
# result = 'A는 10보다 크다' if A > 10 else'아니네'
# print(result)




# # 연습문제 
# tax = 10000 
# total = 0
# weight = int(input('짐의 무게는 얼마인가?'))

# total = ( weight // 10 ) * tax if weight // 10 > 0 else 0 

# print('전하의 무게는 %dkg이며 수수료는 %d이옵니다.' %(weight,total))

# # 연습문제2
# ques1 = int(input('가진 돈의 액수를 입력하시오'))
# ques2 = (input('배가 고픈가요? (y/n)'))

# if ques1 >= 10000 and ques2 == 'y' :
#     print('저녁을 사먹으시오')
# else :
#     print('집에 가라')



# print('포매팅을 {}사용해봅니다. {}이건 뭐였져?'.format('1번','2번'))


# a 와 b 가같은지 비교하는 연산자 is 
# 객체 타입은 메모리주소를 비교하고 숫자, 문자, bool 기본 타입의 경우 값을 비교함
# 숫자, 문자, bool은 데이터 pool을 만들어서 재활용하므로, 값을 비교할 때 메모리 주소가 아니라 데이터 pool에서값을 비교한다.

# a = [10,20]
# b = [10,20]
# if a is b : # 객체이므로 메모리주소가달라서 fail
#     print('참입니다.')
# print(id(a))
# print(id(b))

# c = 10
# d = 10
# if c is d :
#     print('참입니다.')
#     print(id(c))
#     print(id(d))


# while 조건식 : 조건식이 참인 경우 아래를 반복 
    # 실행문


# '''머쓱이네 피자가게는 피자를 여섯 조각으로 잘라 줍니다. 피자를 나눠먹을 사람의 수 n이 매개변수로 주어질 때, n명이 주문한 피자를 남기지 않고 모두 같은 수의 피자 조각을 먹어야 한다면 최소 몇 판을 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.'''

# n = 10
# pizza = 6

# def solution(n):
#     i=1
#     while(1): # while 1이 무슨 말이야 
#         if (6*i)%n==0:
#             return i
#         i+=1

# # 1부터1000까지 모두더한값을 출력하라
# n = 0
# sum1 = 0
# while True :
#     if n == 1001 :
#         break
#     sum1 += n    
#     n += 1   

# print(f'더한값은 {sum1}, 평균값은 {sum1/1000}')


# # countinue 다시반복문 조건으로 이동한다.
# # 1부터 1000중에 홀수만 더해서 출력해 
# a = 0
# sum = 0
# while a < 1000 :
#     a += 1  # hello 무한출력
#     if a % 2 == 0 : # 짝수라면 
#         continue
#     sum += a        
# print(sum) 



# 나만의 리스트 만들기

# while True :
#     cnt = int(input('리스트의 요소를 몇개 넣을건가요? (10개 이하): '))
#     if cnt >= 10 :
#         cnt = int(input('10개 이하라구요: '))
#         continue
#     list1 = []
#     while True :
#         q = int(input('리스트를 입력하세요. : '))
#         list1.append(q)
#         if len(list1) > cnt :
#             break 
# print(list1) # 엥ㅇ???
 
# 로또 번호 생성기 

# import random

# lotto = []
# #while len(lotto) < 6 :

# # range() 함수 ()
# for i in range(0,6) :
#     print(i) # 012345 (6개의 숫자, 끝자리는 -1 개임)
#     lotto.append(random.randint(1,45))
# print(lotto)

# v1 = list(range(10,20)) # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# print(v1)

# for a in v1 :
#     print(a)

# for a in range(0,len(v1)) :
#     print(v1[a])

# # for a in 리스트 구문으로는 원본 데이터를 변경할 수 없다.
# lista = [200,100,300]
# for a in lista :
#     a = 100 # 불가능
#     lista[a] = 100  # 가능 (직접 리스트의인덱스로 접근해야함 )


# 리스트로 0~9까지를 담는 방법
# list_1 = list(range(10)) 
# print(list_1)
# list_2 = []
# for i in range(10) :
#     list_2.append(i) 
# print(list_2)

list_3 = [2*j for j in range(10) if j % 2 == 1]
print(list_3)




