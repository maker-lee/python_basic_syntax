
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

participant=["marina", "josipa", "nikola", "vinko", "filipa"]
completion=["josipa", "filipa", "marina", "nikola"]


# 단어 빈도수 구하기

p1 = {}
c1 = {}
for key in participant :
    p1[key] = p1.get(key,0) + 1 # get으로 키를 가져온다. 키가 없으면 초기값은 0이다. 
for key2 in completion :
    c1[key2] = c1.get(key2,0) + 1 
for i in p1.keys() : # 이러면 동명이인에서는 실패, 효율성은 통과함 
    if p1[i] == c1[i] :
            pass
    else :
        print(i)


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
