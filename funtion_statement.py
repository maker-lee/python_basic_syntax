
# 로직의 연산을 재사용하기 위해 만드는 함수 
# 리턴값 , input값은 있어도, 없어도 상관없다. 
# 함수를 호출할 때는 함수명(input)으로 한다. 

def myFunc(myInput) :
    calc = 20 * (myInput + 10) ** 2
    return calc

def myPlusFunc(num) :
    answer = 0
    for i in range(1,num+1) :
        answer += i 
    return answer 

#print(myPlusFunc(100))


def plusTwo(num1,num2) :
    return ((num1 + num2) + 2 )* 2
result = plusTwo(1,2)


lista = [1,4,6,9,4]

def my_index2(list1,num1)  :
    result = 0
    for a in range(len(list1)) :
        if list1[a] == num1 :
            result = a
            break 
    print(result)
    
my_index2(lista,9) 
r1 = my_index2(lista,9) 
print(r1) # 내부에 print()가있으면 none값이출력된다.
