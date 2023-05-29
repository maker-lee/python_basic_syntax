# # ctrl + F5 터미널 됨  
# print('hello world')

# a = 1
# b = '1'
# c = 2.4
# d = -1.5468786854315486877965312
# print(a,'는',type(a))
# print(b,'는',type(b))
# print(c,'는',type(c))
# print(d,'는',type(d))

# a = 3
# b = 4

# # 사칙연산 연습

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b) # 몫 
# print(a % b)  # 나머지 

# print('문자 형 변환',str(a)+str(b))

# # 자료의 형변환

# c = 2.33333
# print(int(c))

# x ='a'
# print(ord(x)) 
# # 아스키코드(문자를 숫자로 매핑시키는 코드) 변환하는 함수 ord
# # 문자에 매핑되는 숫자를 사전에 저장되어, 메모리에 97을 이진법으로 바꿔서 저장된다.



# # 이스케이프문을 활용한 줄바꿈
# # 이스케이프문이란 \n(줄바꿈), \t(탭)등의 특수기호를 말한다.
# qq = '줄바꿈\n'+'아이구\n힘들어'
# print(qq)

# print("python's eazy")
# print("쌍따옴표(\")는 파이썬에서 문자를 의미한다.") #\는 특수문자를 있는 그대로 표현해준다
# print('쌍따옴표(")는 파이썬에서 문자를 의미한다.') # 아니면 ",'를 번갈아 쓰자
# print("홑따옴표(')는 파이썬에서 문자를 의미한다.")
# print('\\n은 파이썬에서 한 줄 바꿔쓰기를 의미한다.') 



# 문자열의 덧셈과 곱셈

# a = 'python '
# b = 'is fun'
# c = a+ b
# print(c)
# print(a+b)
# print(a,b)

# c = a*4+b
# print(c)


# 인덱싱 = 위치값 
# 찾을 대상[찾는 것의 숫자값] 인덱스의 사용방법 0 부터 커지거나 -1로 뒤에서부터 찾는다.
#a = 'python\'s fun. but python is a little bit difficult. however i am not horack horack, so i\'ll masterd it'
# print(a[5])
# print(a[-1])

# # 문자열의 길이를 출력한다.
# print(len(a))
# print(a[len(a)-1])

# 슬라이싱  시작~끝까지 잘라낸다. 찾을대상[시작(이상):끝(미만):간격(n칸)]
#print(a[0:20:2])
# 2이상 ~ 미만 문자를 n개씩 건녀띄고 b에 담아 출력

# d = 'python is fun'
# print(d[6:])
# print(d[::-1]) # 역순으로 출력하기


# a = '20220505CHILDRENS\'_DAY'

# day = a[:8]
# date = a[8:]
# print(day)
# print(date)

# aaa = [1,2,3,4]
# print(aaa[::-1])


# # 문자열 formating
# age = 10
# weight = 40
# print('my age is %d and weight is %fkg'%(age,weight))
# print('%s는 %s입니다'%(date,day))
# # print('%s는 %s입니다'%(int(date),day))
# input으로 받을 때 편하다. +를 사용하지 않아 덜 번거롭다

# lan = input('언어:')
# times = int(input('몇번?'))

# # print('how many times study? and languges? i studied %s, %d timees' %(lan,times))

# age = int(input('나이가 몇살이신가요?'))
# weight = float(input('몸무게가몇키로인가요?'))
# print('my age is %d, and weight is %f kg' %(age,weight))



# # 대상 문자열에 지정한 문자가 몇개 있는지 개수 세기 변수.count('갯수 세야 하는 단어') 
# a = 'python'
# b = a.count('g')

# # 위치(index) 찾기 변수.find(찾을내용) 
# c = a.find('m')

# print(b,c)

# # 대소문자 변경 .upper(), .lower()
# a = 'heLLo'
# print(a.upper())
# b = "HELLo"
# print(b.lower())

# # 양쪽 공백 제거 .strip()  
# c = "   HELLo   "
# print(c.strip())

# # 문자열 대체하기 replace(찾는문자,대체문자) 
# d = 'i studied python'
# # d1 = d.replace('python','java')
# # print(d1)
# # print(d)

# # 문자열 나누기 split()
# e = d.split() # 공백을 기준으로 나눈다 ['i', 'studed', 'python']
# # print(e)

# dd = 'i studied  python   ' # 스페이스바1칸, 중간에 2칸, 뒤에 3칸인 경우
# e1 = dd.split(" ") #공백 한 칸당 하나씩으로 나뉜다 ['i', 'studied', '', 'python', '', '', '']
# # 스플릿 중간에 " "가 사라지고 맨뒤에 " "는 나뉘는게 없어서 살아남는다. 
# print(e1)
# print(dd.split()) # 공백이 여러개여도 하나로 체크된다. 
# print(dd.split('ed')) # ['i studi', '  python   ']


# sep 이란 separate(구분자) 의 줄임말 입니다. 즉, 다중 출력 문자열에서 "각 문자열 객체 사이를 무엇으로 구분 할 것인가" 
# sep 이 지정되지 않거나 None 이면, 다른 분할 알고리즘이 적용됩니다: 연속된 공백 문자는 단일한 구분자로 간주하고, 문자열이 선행이나 후행 공백을 포함해도 결과는 시작과 끝에 빈 문자열을 포함하지 않습니다.

# # 연습문제
# x = int(input('x='))
# y = 2.5 * x**2 + 3.3 *x + 6 # y = 2.5 * pow(x,2)+ 3.3 *x + 6 # 제곱은 pow로 한다.
# print('2차 방정식 결과 =',y)

# # 연습문제2
# # 3개의단어를 키보드로 입력 받아 각단어의 첫글자를 추출 후 단어의 약자를 출력하라
# a = input('입력1 : ')
# b = input('입력2 : ')
# c = input('입력3 : ')
# print('='*30)
# abbr = a[0]+b[0]+c[0]
# print(abbr)



# print('value=',10+20+30)
# print('010','2243','9321',sep='-')
# print('나는','배가','고프다')

# a = 'abcdefghijklmnopqrstu'
# # print(a[0:20:2])

# # d = 'python is fun'
# # print(d[5:])

# for i in a :
#     print(i)


# numer1 = 1
# denom1 = 2
# numer2 = 3
# denom2 = 4
 
# # a = (numer1 * denom2) + (numer2 * denom1)
# # b = (denom1 * denom2)
# # c = a/b

# # for i in range(min(a, b), 0, -1):
# #     if a % i == 0 and b % i == 0:
# #         c = i
# # print(a/c,b/c)


# # 최대공약수 구하는 방법
# # 제가이걸어떻게아나요...(초5산수임)
# # 아래가 정답인데 
# def gcd(x,y):
#     if x % y == 0:
#         return y
#     else:
#         return gcd(y,x%y)

# e,f = numer1*denom2+denom1*numer2,denom1*denom2
# g = gcd(e,f)
# if g != 1:
#     e//=g
#     f//=g
# print(e,f)




# # 기약 분수 구하기 
# def solution(numer1, denom1, numer2, denom2): 
#     a = (numer1 * denom2) + (numer2 * denom1)
#     b = (denom1 * denom2) 
#     for i in range(min(a, b), 0, -1):
#         if a % i == 0 and b % i == 0:
#             c = i
#     return [a/c,b/c]




