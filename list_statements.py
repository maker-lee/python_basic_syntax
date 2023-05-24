# 리스트

list1 = ['a','b','c','d','e','f','g']

# print(list1[0])
# print(list1[:5])
# print(type(list1[:5]))
# print(type(list1[-1]))

# # list 내에 list 값을 조회하는 방법
# list_ex1 = ['a','b','c',[1,2,3]]
# number = list_ex1[3]
# print(number) # 변수 number에 [1,2,3]을 담아출력하기
# print(number[number.index(1)]+number[number.index(3)]) # number에 담은 값중 1과 3을 더하기
# print(list_ex1[3][0] + list_ex1[3][2] )


# # 리스트 더하기
# list2 = ['피카츄','라이츄','파이리','꼬부기']
# list3 = list1 + list2
# list4 = list2 * 2
# print(list4)

# print(len(list2))

# 리스트 값 수정하기

# # 1개의값을바꿀떄
# list1[0] = 'A'
# print(list1)

# # .count
# print(list1.count('A'))

# 특정 요소 삭제하기 (del / remove)

a = [1,3,9,3,5,6,9,9]
# del a[2]
# print(a) # [1, 2, 4, 5, 6, 7]
# del a[2:6]
# print(a) # [1, 2]

# for i in range(len(a)) :# 요소만큼반복해
#     if 9 in a :  # 만약 리스트안에 9가있으면 
#         a.remove(9) # 9를지워 
# print(a)
  

# del 을 사용하여 풀어보기 

'''
0부터 n까지 불러온다
숫자가 9이면 삭제한다. 
만약 9가 아니면 다음걸 불러온다. 
'''
a = [1,3,9,3,5,6,9,9]
# print(a.count(9))

# while True :
#     a.remove(9)
#     if 9 not in a :
#         break

# print(a)


# 리스트 값 추가하기

# append 무조건 맨 뒤로 값이 추가된다.
# isert 중간에 추가시킬 수 있다.

poke = ['피카츄','라이츄','파이리','꼬부기','야도란']

# a = '야도란'
# b = ['피존투','또가스'] 
# c = '파이리'

# poke.insert(3,c) # ['피카츄', '라이츄', '파이리', '파이리', '꼬부기', '야도란']
# print(poke)
# poke.append(a) # ['피카츄', '라이츄', '파이리', '파이리', '꼬부기', '야도란', '야도란']
# print(poke)

# # extend, iterable 객체를 list에추가할 떄 사용함. 각 요소를 꺼내어 맨 뒤에 추가함 
# # iterable 

# poke.extend(b)
# print(poke)

#num1 = [5,4,6,3,1,2]
# print(num1)

# chlist = ['a','b','d','c','e','g','f']
# chlist.reverse()
# print(chlist)

# 리스트중 '라이츄'는 몇번째에 위치해있는가?
# print(poke.index('라이츄'))

# num1.pop()
# last_value = num1.pop()
# print(last_value)
# print(num1)


# 뮨자 list를 문자열로 바꾸기 <-> 문자열을 list로 바꾸기

# list_str = ['hello','world','python']
# str1 = 'hello world python'

# print(list(str1)) #['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', ' ', 'p', 'y', 't', 'h', 'o', 'n']
# print(str1.split()) #['hello', 'world', 'python']
# print(','.join(list_str)) #helloworldpython


# dot = (1,1) # 
# # [-1] 이면 뒤에서부터고, [0] 이면 앞에서부터다. 
# # dot[0] 이 음수는 2,3 분면 , 양수는 1,4분면이다. 
# quad = [(3,2),(4,1)]
# print(quad[dot[0] > 0][dot[1] > 0])
array = [9, -1, 0]
array.sort()
answer = array[len(array) // 2]   
print(answer)