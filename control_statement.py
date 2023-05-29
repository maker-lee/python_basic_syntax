
# 제어문

# su = 60
# lista = [90,25,67,45,80] # 학생의 번호 순서대로임 
# # 1번은 합격입니다 .... 5번 학생은 합격입니다 이렇게 출력하세용.

# listb = ['합격' for i in lista if i >= su ]
# num=1
# for i in lista :
#     if i >= su :
#         print(f'{num}번째 학생은 합격입니다.')
#     else :
#         print(f'{num}번째 학생은 불합격입니다.')
#     num += 1


# # 혈액형 A형 1명이 급하게 필요한 상황 4번째 지원자가 A형입니다. 
# lista = ['b','b','ab','a','b','a']
# num = [lista.index('a')+1 for i in lista if i == 'a']
# print(f'{num[0]}번째 고객이 지원하게 되었습니다.')
# # 리스트의 길이가 길 수 있으니까 반복문과 break를 쓰는게 더 빠르다. 
    
# for문을 사용한 구구단
# n = int(input('구구단몇단을계산해드릴까용?'))
# for j in range(1,10) :
#     print(f'{n}*{j}={n*j}')

# while True :
#     for j in range(1,10) :
#         print(f'{n}*{j}={n*j}')
#     break

# # 이중 for 문 
# for i in range(5,10) :
#     for j in range(1,10) :
#         print(f'{i}*{j}={n*j}')


# lista = [10,20,30,40]

# # lista의 [0]번째와 [1]번째 바꾸기
# a = lista[0]
# b = lista[1]
# lista[0] = b
# lista[1] = a
# print(lista) # 변경이 되는 값을 keep해둬야함 

# # 파이썬에서 지원하는 문법은 # 여러개도 된다. 
# lista[0], lista[1], lista[2] = lista[1], lista[0], lista[3]
# print(lista) # 변경이 되는 값을 keep해둬야함 


# for문을 이용한 정렬 알고리즘
lista = [93,45,21,30,20,94,66,71,56]
# 오름차순 정렬 lista.sort() 

# 리스트a의 0번째 값은, lista의 가장 작은 값이다. 
# 리스트a의 현재 0번째 값은 lista의 가장 작은 값의 index와 자리를 바꾼다.


# # 선택정렬 : 0번째 인덱스부터 가장 작은 값을 채워나가는 방식
# for i in range(len(lista)-1) : # index 값으로 접근하기 때문에, lista보다 range를사용
#     # 채워나가야할 인덱스 , 가장 작은 수가 들어갈 인덱스다. 0,1,2 이렇게 채워넣을거야
#     # 맨 뒤에 숫자는 비교할 필요가 없으니까 -1 자리까지만 비교하면 된다. 
#     # i 자리는 리스트의 숫자만큼이다. 그러나 맨 뒤는 비교할 필요가 없으니까-1적어도ㅇㅋ
        
#     for j in range(i+1,len(lista))  : # 비교의 대상이 되는 인덱스, 자기 자신과 비교하지 않기 위해서 1자리를 뒤에서 해야하고, i부터 시작하면 되니까 시작을 0부터 아니라 i부터 하면 된다. 포인트는 이미 정렬한 인덱스와는 비교하면 안된다. 
#     # j 자리는 리스트의 숫자만큼인데 이미 맨앞으로 간 애들거 비교할 필요가 없으니까 i+1 

#         if lista[i] > lista[j] : 
#             # 만약에 i 자리가 j 자리보다 크다면 둘의 위치를 바꿔라 
#             lista[i], lista[j] = lista[j], lista[i]
# print(lista)



# # 버블정렬 : 앞자리와 뒷자리를 비교해서 큰 애들을 계속 뒤로 보내기
# lista = [93,45,21,30,20,94,66,71,56]

# # for i in range(len(lista)-1) : # 012345678  # 93 시작
# #     for j in range(len(lista)-i-1) : # n-1부터 7  # 45시작
# #         if lista[j] > lista[j+1] :    # 뒷친구가 앞친구보다 크면
# #             lista[j+1],lista[i] = lista[i],lista[j+1] # 앞뒤친구 자리 바꿔
# # print(lista)
 
# for i in range(len(lista)): # 
#     for j in range(len(lista)-i-1):
#         if (lista[j] > lista[j+1]):
#             temp = lista[j]
#             lista[j] =lista[j+1]
#             lista[j+1] = temp
# print(lista)





# '''행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.'''

# arr1 = [[1,2],[2,3]]
# arr2 = [[3,4],[5,6]]
# answer = []

# answer = [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))]
# print(answer)
# j는 [1,2] 의 길이를 말한다. 0,1  # 1는 리스트 내부에 있는 리스트 숫자를 말한다.

# for i in range(len(arr1)) : # 0,1 # ar1에서맨처음, 2에서 맨처음걸 가져와라
#     temp = []
#     for j in range(len(arr1[0])) :
#         temp.append(arr1[i][j] + arr2[i][j])    
#     answer.append(temp)        
# print(answer)








