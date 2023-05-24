
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
 
'''머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.'''

price = 580000
coin = 0
if price >= 100000 and price < 300000 :
    coin = price * 0.05
elif price >= 300000 and price < 500000:
    coin = price * 0.1
elif price > 300000 and price >= 500000 :
    coin = price * 0.2
return price - coin



