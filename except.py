# # 예외처리 구문 try ~ except

# while True :
#     try :
#         first = int(input('분자 쉬먀 :'))
#         second = int(input('분모 쉬먀 :'))
#         print(first/second)
#     except ZeroDivisionError as zd : # except 중에 1개만 걸림 10
#          print(f'{zd}')
#     except ValueError as ve :
#          print(f'{ve}')
#     except Exception as e: 
#          print(f'{e}')

# #    Fianlly :
#        print('결과를 확인해주세요')


# 사용자가 0으로 숫자를 나누게 되면 DIVISION BY ZERO ERROR 발생함
class Bird :
    def fly(self) :
        raise Exception  # 에러 강제

class Eagle(Bird) :
    pass # 무조건 오버라이딩 강제하는 코드/ 안하면 에러남
    def fly(self) : # 이거 해야함 
        print('날아올라')

eagle1 = Eagle()
eagle1.fly()

