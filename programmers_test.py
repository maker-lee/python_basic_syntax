
'''어떤 문자열 A가 다른 문자열 B안에 속하면 A를 B의 부분 문자열이라고 합니다. 예를 들어 문자열 "abc"는 문자열 "aabcc"의 부분 문자열입니다.
문자열 str1과 str2가 주어질 때, str1이 str2의 부분 문자열이라면 1을 부분 문자열이 아니라면 0을 return하도록 solution 함수를 완성해주세요.
'''


# str1 = "abcc"
# str2 = "aabcc"

# str1_num = len(str1)
# answer = 0
# for i in range(len(str2)) :
#     if (str2[i:i+str1_num]) == str1 :
#         answer = 1
# if answer >= 1 :
#     answer = 1
# else :
#     answer = 0
# print(answer)


# def solution(str1, str2):
#     if str1 in str2: return 1
#     return 0


# def solution(n):       
#     if n <= 7 :
#         answer = 1
#     elif n % 7 == 0 :
#         answer = n // 7
#     else  :
#         answer = (n // 7) + 1
#     return answer


# def solution(n):
#     return (n - 1) // 7 + 1



# # 특정 문자 제거하기
# my_string = "abfffcdefffe"
# letter = "f"

# my_string = my_string.replace(letter,"")
# print(my_string)

# my_string = list(my_string)
# for i in my_string :
#     # print(i)
#     if i == letter :
#         my_string.remove(letter)
#         # print(my_string)
# answer = ''.join(my_string)
# print(answer)


# array = [149, 180, 192, 170]
# height = 167

# answer = 0

# array.sort(reverse=True)
# while True :
#     for i in array :
#         if i > height :
#             answer += 1
#     break
# print(answer)
 


# # 최대 공약수 구하기

# num1 = 10
# num2 = 3

# for i in range(1, num1 + 1):
#   if (num1 % i == 0) & (num2 % i == 0):
#     gcd = i 
  
# print("%d와 %d의 최대공약수는 %d"%(num1, num2, gcd))

# numer1= 1
# denom1 =2
# numer2=3
# denom2=4

# # 분수의 덧셈 
# num1 = (numer1 * denom2) + (numer2 * denom1)
# num2 = denom1 * denom2


# # 최대공약수 구하기 
# for i in range(1, num1 + 1): # 1부터 분자든 분모든 그 숫자만큼 반복한다.
#     if (num1 % i == 0) & (num2 % i == 0): 
#         # 만약 i가 (분자보다 작은 수) 나눴을 때 나머지가 없고, 분모도 없으면
#         gcd = i # 이것은 약수다. 그런데 작은데서 커질거라서 약수가 계속 덮어씌워진다.

# print(num1/gcd,num2/gcd) # 최대공약수로 분자와 분모를 나눠서 알려줘라 


# array = [1,1,1,1,1,1, 2, 3, 3, 3, 4,5,5,5,5,5,5]

# if len(array) == 1 :
#     print(array[0])

# print(max(array))


'''
원소가 어떤 것들이 있는가
그 원소는 array에서 몇 개 있는가
가장 갯수가 많은건뭔가
갯수가 많은걸 리턴해라 
원소가 1개면 어쩌지 
'''



'''
마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.
'''

# participant=["marina", "josipa", "nikola", "vinko", "filipa"]
# completion=["josipa", "filipa", "marina", "nikola"]


# # # 단어 빈도수 구하기
# array = [1, 2, 3, 3, 3, 4] # 데이터셋
# wc = {} # 빈셋
# # get 함수 이용 : key이용 value 가져오기
# for key in array: 
#     wc[key] = wc.get(key,0) +1
# print(wc)

# for v in wc.keys() :
#     print(v)



# p1 = {}
# c1 = {}
# for key in participant :
#     p1[key] = p1.get(key,0) + 1 # get으로 키를 가져온다. 키가 없으면 초기값은 0이다. 
# for key2 in completion :
#     c1[key2] = c1.get(key2,0) + 1 
# for i in p1.keys() : # 이러면 동명이인에서는 실패, 효율성은 통과함 
#     if p1[i] == c1[i] :
#             pass
#     else :
#         print(i)


# 요소 검사와 반복
# dict 생성방법
#  part = dict(key1 = 100, key2 = 200)
# print(part['key1'])
# print('key1' in part)

# for i in part.items() : #(key,value)를 넘긴다
#     print(i)



# 리스트로 짠 경우 , 단 효율성에서 시간 초과가 됨 ()
# for i in completion :
#     try :
#         participant.remove(i)
#     except :
#         pass
# print(''.join(participant))



# # 최빈값 구하기 

# # 나의 풀이 

# array = [1, 2, 3, 3, 3, 4]
# array = ['a','a','pizza','pizza']

# p1 = {}
# for key in array :
#     p1[key] = p1.get(key,0) + 1 # get으로 키를 가져온다. 키가 없으면 초기값은 0이다.
# print(p1) # {1: 1, 2: 1, 3: 3, 4: 1}


# listA = list(p1.values()) #1,1,3,1
# listA_num = len(list(p1.values()))
# maxA = max(listA)
# print(maxA)

# for i in range(0,listA_num) :
#     try :
#         listA.remove(maxA)
#     except :
#         pass
# if listA_num - len(listA) > 1 :
#     print(-1)
    
    
# a = []
# pizza = []
# for k, v in p1.items() :
#     a.append(k)
#     pizza.append(v)
# c = max(pizza)
# print(a[pizza.index(c)]) # 최빈수 

# # 배우신분들의 풀이 

# def solution(array):
#     while len(array) != 0:
#         for i, a in enumerate(set(array)):
#             array.remove(a)
#         if i == 0: return a
#     return -1

# def solution(array):
#     keys = set(array)
#     dict = {}
#     max_freq = []
#     for key in keys:
#         dict[key] = array.count(key)
#     for key in keys:
#         if dict[key] == max(dict.values()):
#             max_freq.append(key)
#     if len(max_freq) > 1:
#         answer = -1
#     else:
#         answer = max_freq[0]
#     return answer

# 최소 공배수 구하기

# 소수 구하기  + 공약수 구하기

# n = 10
# pizza = 6
# divs = 0
# divs2 = 0

# # 최대공약수 def lcm(a, pizza):
# for i in range(max(n, pizza), (n * pizza) + 1):
#     if i % n == 0 and i % pizza == 0:
#         print(i)
#         break


# def gcd(a, pizza):  # 최대공약수
#     while pizza > 0:
#         a, pizza = pizza, a % pizza
#     return a

# def lcm(a, pizza):
#     return a * pizza / gcd(a, pizza)



# '''머쓱이네 피자가게는 피자를 여섯 조각으로 잘라 줍니다. 피자를 나눠먹을 사람의 수 n이 매개변수로 주어질 때, n명이 주문한 피자를 남기지 않고 모두 같은 수의 피자 조각을 먹어야 한다면 최소 몇 판을 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.'''

# # 나의 풀이 
# n = 10
# pizza = 6
# list_p = list()
# for i in range(1,n*pizza+1) :
#     if i % pizza == 0 :
#         list_p.append(i)
# for j in list_p :
#     if j % n == 0 :
#         print(j/pizza)
#         break

# # 다른풀이 

# def solution(n):
#     i=1
#     while(1): # while 1이 무슨 말이야 
#         if (6*i)%n==0:
#             return i
#         i+=1


'''영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다. 문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.
# '''

# my_string = "nice to meet you"
# answer = ''
# my_string = list(my_string)
# mo = ['a','e','i','o','u']

# for i in mo :
#     while i in my_string :
#         my_string.remove(i) 
# answer = "".join(my_string)
# print(answer)


# # 다른 풀이 
# def solution(my_string):
#     return "".join([i for i in my_string if not(i in "aeiou")])

# # 상남자식 풀이 replace는 다 골라내서 바꾸니까!!!!

# def solution(my_string):
#     my_string = my_string.replace("a","")
#     my_string = my_string.replace("e","")
#     my_string = my_string.replace("i","")
#     my_string = my_string.replace("o","")
#     my_string = my_string.replace("u","")
#     return my_string


'''입출력 예 3,6,9가 잇는 만큼 박수 몇번 치기
29423은 3이 1개, 9가 1개 있으므로 2를 출력합니다.'''
order = 29423

# order = str(order)
# cnt = 0
# for i in range(3,10,3) :    
#     cnt += order.count(str(i))
# print(cnt)

# order = str(order)
# print(order.count('3'))

# str에서도 카운트를 사용할 수 있다. 비슷한 문제 
'''정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요'''

# cnt = 0
# for i in str(930211) :
#     print(i)
#     cnt += i


# # 다른사람의 풀이
# def solution(order):
#     order = str(order)
#     return order.count('3') + order.count('6') + order.count('9')

'''개미 군단이 사냥을 나가려고 합니다. 개미군단은 사냥감의 체력에 딱 맞는 병력을 데리고 나가려고 합니다. 장군개미는 5의 공격력을, 병정개미는 3의 공격력을 일개미는 1의 공격력을 가지고 있습니다. 예를 들어 체력 23의 여치를 사냥하려고 할 때, 일개미 23마리를 데리고 가도 되지만, 장군개미 네 마리와 병정개미 한 마리를 데리고 간다면 더 적은 병력으로 사냥할 수 있습니다. 사냥감의 체력 hp가 매개변수로 주어질 때, 사냥감의 체력에 딱 맞게 최소한의 병력을 구성하려면 몇 마리의 개미가 필요한지를 return하도록 solution 함수를 완성해주세요.'''
# hp = 24

# ant5 = 5
# ant3 = 3
# ant1 = 1

# num_ant5 = hp // ant5 
# print(num_ant5) # 4
# num_ant3 = (hp % ant5) // ant3 # 남은 개미를 3으로 나눔
# print(num_ant3)
# num_ant1 = (hp % ant5) % ant3
# print(num_ant1)
# # print(num_ant5+num_ant3+num_ant1)

# # 다른 사람의 풀이

# def solution(hp):    
#     return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)

'''군 전략가 머쓱이는 전쟁 중 적군이 다음과 같은 암호 체계를 사용한다는 것을 알아냈습니다.

암호화된 문자열 cipher를 주고받습니다.
그 문자열에서 code의 배수 번째 글자만 진짜 암호입니다.
문자열 cipher와 정수 code가 매개변수로 주어질 때 해독된 암호 문자열을 return하도록 solution 함수를 완성해주세요.

'''
cipher = "dfjardstddetckdaccccdegk "	
code = 4
cipher = list(cipher) 
n = 0
me = []
while n < len(list(cipher)) : 
    n += code 
    try :
        me.append(cipher[n-1])
    except :
        pass
# return "".join(me)


# 다른 사람풀이

def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer