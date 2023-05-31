# 파일 만들기

'''open()은 w,r,a 모드를 가지고 있다. 
open을 했을 때 파일이 없으면 자동생성을 해줌

'''
# f = open('test.txt','w',encoding='UTF-8') # F는 객체 
# for i in range(1,11) :
#     data = '%d번째 줄입니다 \n'%i
#     f.write(data)

# f = open('test.txt','r',encoding='UTF-8')
# line = f.readline()
# while line :
#     print(line)
#     line = f.readline()
#     if not line :
#         break    

# lines = f.read()
# print(lines)# read는 한번에 데이터 형태로 담아온다.

# f = open('test.txt','a',encoding='UTF-8')
# for i in range(10,20) :
#     data = '%d번째 줄입니다 \n'%i
#     f.write(data)
# f.close() # 파일시스템은 사용빈도가 낮은 데이터를 자동으로 삭제하지 못하니까 직접 닫아줘야 메모리 낭비가 없다(gc = garbage collector)


import os 
# os 라이브러리를 활용한 디렉터리 내에 파일 검색.
searchDir = r'C:\Users\User\Desktop\이지선'

# # .py를 찾으리라
# dirList = os.listdir(searchDir) # 파일 디렉토리 목록을 뽑아냄
# #print(dirList) # ['python_basic_syntax', 'test.txt']  # python_basic_syntax

# # for dir in dirList :
# #     dir_tuple = os.path.split(dir)
# #     #print(dir_tuple) # ('', 'python_basic_syntax') ('', 'test.txt')
# #     if(dir_tuple[1]=='.py') :
# #         #print(dir) # 안나옴. 당연함 없음. 현재폴더에서만 검색함
# #         fullPath = os.path.join(searchDir,dir) 

#         # 하위 폴더 검색
# for dir in dirList :
#     # 폴더인지 아닌지 확인해라 
#     filename = os.path.join(searchDir,dir) 
#     if os.path.isdir(filename) :# 폴더라면 isdir(폴더 확인함수) 
#         for dir2 in os.listdir(filename) :
#             dir_tuple2 = os.path.split(dir)
#             if(dir_tuple2[1]=='.py') :
#                 fullPath = os.path.join(searchDir,dir2) 

#     # py인지 아닌지 확인해라 
#     dir_tuple = os.path.split(dir)
#     if(dir_tuple[1]=='.py') :
#         fullPath = os.path.join(searchDir,dir) 
        
        
#         print(fullPath)


import os

def search(dirname):
    try:
        filenames = os.listdir(dirname) # 파이썬의 os.listdir() 함수는 지정 경로의 디렉토리 내의 모든 파일 이름을 리스트로 반환한다
        for filename in filenames:
            full_filename = os.path.join(dirname, filename) #os.path.join('a','b') 는 a\b 이렇게 경로가듯 만들어줌
            if os.path.isdir(full_filename): # 지정경로의 디렉토리 내 모든 파일이름을 리스트로 반환
                search(full_filename) # 재귀함수 다시 처음으로가 
            else:
                ext = os.path.splitext(full_filename)[-1] #\를 기준으로 나뉨
                if ext == '.py': # 더이상 폴더가 없는데, 파일명이 py인 경우 
                    print(full_filename)
    except PermissionError: # Python 코드 중 특정 파일을 열 때 PermissionError가 생기는 이유는 대다수 파일의 권한 자체가 문제이거나 파일 경로가 잘못됐을 때가 많다.
        pass

search(r'C:\Users\User\Desktop\이지선')

