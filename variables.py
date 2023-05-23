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


# '''
# 여기에주석을그냥쓰면됩니다.
# 괜히 고민했네 ; 
# 스페이스바 내가 이래서 키보드만 두번 바꿨는데
# 여기 또 이러고 앉아있네
# '''
 

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


a = '20220505CHILDRENS\'_DAY'

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

# strlist = ["We", "are", "the", "world!"]
# print(strlist[1:3])
# answer = []
# for i in strlist :
#     answer.append(len(i))
# print(answer)


# 예제1) 리스트의 값을 정수 타입으로 변환 map(변환 타입 int,len 등등, [리스트])
# 단 map은 객체이므로 다시 튜플, 리스트 타입으로 변환해야한다.

result1 = list(map(int, [1.1, 2.2, 3.3, 4.4, 5.5]))
print(result1)

numbers = [1,2,3,4,5]
answer = []
for i in numbers :
    i = i * 2
    answer.append(i)
print(answer)

def solution(numbers):
    answer = [i *2 for i in numbers]
    return answer

# 이렇게표현할수도있다.