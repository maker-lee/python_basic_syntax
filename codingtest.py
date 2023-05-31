# '''M번 더하기, K번 초과 불가, 배열 크기 N'''

# def maxsum(N,M,K, myarr):
#     myarr = sorted(myarr, reverse=True) # 내림차순 정렬
#     # print(myarr) # 정렬 확인용
#     first_big = myarr[0] #큰 수1
#     second_big = myarr[1] #큰 수2
    
#     count = 0 #계산 횟 수 초기 값 = 0
#     myresult = 0 #계산 값 저장소 초기 값 = 0
#     while M > 0: #M은 음수 불가
#         if count < K : #count=k일 경우 덧셈 중단
#             myresult += first_big
#             count += 1 #덧셈한 수 +1
#         else: #큰 수2 덧셈
#             myresult += second_big
#             count = 0 #큰 수2 덧셈은 1회만 실행
#         M -= 1 #M에서 1씩 감소 -> while문 종료 조건
#     return myresult #결과 값 출력
# print(maxsum(5,8,3, [2, 4, 5, 4, 6]))


# #####################################################################
# # 입력 예시 
# N = 5 # 요소 숫자
# M = 8 # 숫자가 더해지는 횟수
# K = 3  # 연속으로 더할 수 있는 횟수 

# # sorted와 index를 이용한 풀이 

# num_list = [2,4,5,4,6]
# num_list = sorted(num_list)

# cnt = 0
# sum1 = 0
# while cnt < M : # 총 몇번 더해야하나 
#     for _ in range(K) : # 같은 숫자는 몇번 반복할 수 있나
#         sum1 += num_list[-1] # 가장 큰 수를 찾는다 -> 인덱스를
#         cnt += 1 # n번 더함 
#     sum1 += num_list[-2] # 두번째로 작은 수 찾아서 더함 
#     cnt += 1 # n번 더함 
# print(sum1) # 완성 

# 곱하면 더 편한거 아님?

sum1 = num_list[-1]

#####################################################################


# input값 설정
num_list = [2,4,5,4,6]
M = 8
K = 3

# 가장 큰 수 구하기
num_list.sort(reverse = True)
first_num = num_list[0]
second_num = num_list[1]

# 반복문
sum=0
while True: # 무한 반복해라 
    for i in range(K): # 한 번호를 최대한 반복하는 수 (3번)
            if M!= 0: # 만약 8번과 0이 같지 않으면  (탭 왜 두번ㅠ)
                sum+=first_num   # 가장 높은 수를 sum에 더하고  
                M-=1 # 8번에서 1번씩 빼라 
            else:  # 총 8번 했으면 반복을 탈출해 
                break               
    if M != 0: # 8번과 0이 같지 않으면  
        sum+=second_num    # 두번째로 높은 수를 더해
        M-=1 # 8번에서 1개씩 빼라 
    else: # 총 8번 했으면 반복을 탈출해 
        break                    
print(sum)      # 첫번째 반복문과 두번째 반복문의 합



# ######################################################################
# k = 3
# m = 8
# local = [2,4,5,4,6]
# local.sort(reverse = True)

# first = local[0] # 가장 큰 수
# second = local[1] # 두번째로 큰 수
# sum1 = 0 # 가장 큰 수 지정한 횟수 더하기

# for i in range(k):
#     sum1 += first 
# print(sum1) #18


# ########################################################
# # 두번째로 큰 수는 k번 더할 필요가 없다. 큰 수를 k번 더하고 그사이에 양념처럼 1번씩만더해주면 된다.
# ############################################################
# # 두 번째로 큰 수 지정한 횟수 더하기
# sum2 = 0
# for num2 in range(k):
#     sum2 += second 
# print(sum2) # 15




# ##############################################################
# # (1) break를 거는 이유는 가장 큰 수가 K 번 더해진 경우
# # (2) 총 더해야하는 M번 다 더한 경우 
# #############################################################
# # # 지정 횟수 break  # 해석 
# # while True:  # 아래를 무한정 돌려라 
# #     for i in range(k): # 0,1,2를 i에 집어넣어라 
# #         if m == 0: # 만약 (m) 8이 0과 같아지면 
# #             break #멈춰라 
# #         m -= 1 # 8에서 1씩 빼라 -> 결론 3번 밖에 안돌아가서 5되고 무한반복됨 
    
# # # 덧셈의 길이 제한하기
# # while True: # 아래를 무한정 돌려라 
# #     if m == 0: # 만약 (m) 8이 0과 같아지면 
# #         break #멈춰라 
# #     m -= 1  8에서 1씩 빼라 -> 8번쯤 돌아가고 끝 