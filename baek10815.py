# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 
# 상근이는 숫자 카드 N개를 가지고 있다. 
# 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.


input_number = int(input()) 
input_data = input() 

input_data = input_data.split(' ') 
input_data = list(map(int,input_data)) 
input_data.sort() 

check_number = int(input()) 
check_data = input() 

check_data = check_data.split(' ') 
check_data = list(map(int,check_data)) 

for i in range(check_number): 
    answer = 0 
    left = 0 
    right = input_number - 1 
    mid = (left + right) // 2 
    
    while(left <= right): 
        if input_data[mid] == check_data[i]: 
            answer = 1 
            break 
        elif input_data[mid] < check_data[i]: 
            left = mid + 1 
        else: 
            right = mid - 1 
        mid = (left + right) // 2 
        
    print(answer,end = ' ')

