# # 튜플

# t1 = 1,2,3,[3,3,4]

# print(type(t1[3]))
# print(t1)


# 딕셔너리

dic1 = {'이름':'홍길동','나이':25,'직업':'도둑','성별':'남자',2:52}
# print(dic1.get(''))
# print(dic1)
# print(dic1['이름'])



# keylist = []
# valuelist = []
# for i in dic1.keys():
#     keylist.append(i)
#     valuelist.append(dic1[i])
# print(keylist,valuelist)


blood = ['A','A','B','O','O','AB','AB']

dic_b = {}

# 빠른 방법
for a in blood :
    if a not in dic_b.keys() :  # 모든 혈액형을 계속 검사하지 않도록 함
        dic_b[a] = 1
    else :
        dic_b[a] += 1 # 카운트를 사용하지 않아서 조회 속도가 빠름 
print(dic_b)

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


s1 = set([1,2,3,4,5])
s2 = set([4,5,6])
s1.update(s2)
print(s1)

