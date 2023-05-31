
# 클래스의 사용
# 같은 기능의 함수의 집합
# 객체를 만들기 위해 사용된다.



# 예시
# 사칙연산함수가 있을 때 같은 기능을 하므로 calculator라는 클래스에 모아둘 수있다.

'''명명규칙 
(1) 클래스는 대문자 알파벳으로 시작한다. (낙타표기법) 
(2) 변수명, 함수명은 소문자로 시작한다. 
'''

# # 함수의 집합으로서의 클래스 (일반적이지 않은 형태임)
# class Calculator : 
#     def plus(a,b) :
#         return a+b
#     def minus(a,b) :
#         return a-b
#     def multiply(a,b) :
#         return a*b
#     def divide(a,b) :
#         return a/+b
    
# print(Calculator.plus(10,20)) # 누적된 값을 가지고 있지않은 계산 클래스
    

# 함수의 집합으로서의 클래스 (일반적이지 않은 형태임)

# class Calculator : 
#     result = 0
#     # 클래스 내에서 변수에 접근하는 방법
#     #(1) 클래스명.변수를 쓰면 클래스 변수에 접근 가능하다.
#     #(2) 클래스메소드 데코레이터 사용
#     @classmethod #클래스 약어로 불러오기 
#     def plus(cal,a) :
#         cal.result += a
#     def minus(a) :
#         Calculator.result -= a
#     def multiply(a) :
#         Calculator.result *= a
#     def divide(a) :
#         Calculator.result /= a

# print(Calculator.result) 
# Calculator.plus(10) # 누적된 값을 가지고 있지않은 계산 클래스
# print(Calculator.result) 

# 객체란 클래스의 복제본 / 인스턴스라고도 한다. 
# 객체의 사용 이유
# 클래스의 중복제거 / 변수와 함수의 재활용의 어려움 해결
# 객체는 aCompany 

class Calculator :
    # 객체가 생성될때 init은 가장먼저 실행된다.
    def __init__(self) : # init은 생성자(constructor) / result는 지역변수다
        self.result = 0  # self.result는 객체의 변수라서 위의 result와 달라
        # result는 사용자(객체)에게 받는다. 
    # 클래스 내의 함수의 매개변수가 2개 이상일 때
    # 첫번째 매개변수(self)는 객체를 의미한다. 
    # 힙메모리에 저장되기 때문에 객체.result로 비휘발성으로 저장되어 리턴하지 않아도댐 
    def plus(self,a) : 
        self.result += a
    def minus(self,a) :
        self.result -= a
    def multiply(self,a) :
        self.result *= a
    def divide(self,a) :
        self.result /= a


if __name__ == "__main__": # 여기 함수 돌아갈때만 돌려라 (외부에서 임포트할때는 X)



    # 객체 만들기
    aCompany = Calculator() # self 자리에 aCompany가 들어감 / self는 객체 그 자신
    aCompany.plus(100000) 
    print('1번객체',aCompany.result)

    # 객체 만들기2 
    nCompany = Calculator()
    nCompany.minus(3)
    nCompany.minus(4)
    print('2번객체',nCompany.result)


# 초기값은 클래스 생성 시 매개변수를 통해 초기값 세팅가능 


# import datetime 

# # 
# class Person :
#     def __init__(self,name,age,gender,email) :
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.email = email
#         self.today = str(datetime.datetime.now()) # 안 받고도 들어가게 할수 있다
        
#     def register(self) :
#         self.myInfo = self.name,str(self.age),self.gender,self.email,self.today

# p1 = Person('David',18,'male','david@google.com')
# p2 = Person('Linda',20,'female','Linda@google.com')
# p1.register()
# print(p1.myInfo)
# p2.register()
# print(p2.myInfo)

# 클래스의 상속
# 부모클래스에서의 기능을 자식 클래스에서 물려받는것
# class 자식 클래스명(부모클래스명) 형식으로 선언된다. 

class Cal1 :
    def __init__(self) :
        self.result = 0  
    def plus(self,a) : 
        self.result += a
    def minus(self,a) :
        self.result -= a
    def multiply(self,a) :
        self.result *= a
    

class Cal2(Cal1) : # 자식클래스(부모클래스)
    # def __init__(self):
    #     super().__init__(self,)
    def divide(self,a) :
        self.result /= a
    def multiply(self,a) : # 부모의 기능을 재선언하게 되면 자식이 우선이고 이를 오버라이딩이라고 한다.
        self.result **= a       
if __name__ == "__main__": # 여기 함수 돌아갈때만 돌려라 (외부에서 임포트할때는 X)
    # 현재 실행하는 주체가 자기 자신 파일이면 이 코드가 실행되는데,
    # 다른 파일이면 main이 아니라 if문을 타지 않아서 아래가 실행되지 않는다.

    cc1 = Cal2()
    cc1.plus(100)
    cc1.divide(10)
    print('class_statment의 실행',cc1.result)
    # print(cc1) # print 함수는 object 클래스를 상속받고 있다. list,dict 같은 파이썬 객체값을 value 형식으로 출력해주는 함수가 내장되어 있다.

print('건물 사이에 피어난 장미')