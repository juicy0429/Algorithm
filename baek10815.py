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

## 소스트리 커밋 테스트


# def binary_search(num):
#     left = 0
#     right = n-1
#     while left <= right :
#         mid = (left+right)//2
#         if intCard[mid] == num :
#             return 1
#         elif intCard[mid] > num :
#             right = mid - 1
#             # 반 줄여주기 1
#         else:
#             left = mid + 1
#             # 반 줄여주기 2
#     return 0
# ​
# n = int(input())
# intCard = list(map(int, input().split()))
# intCard.sort()
# ​
# input() #M
# for num in list(map(int, input().split())):
#     print(binary_search(num), end = ' ')


# import java.util.HashSet;
# import java.util.Scanner;
# public class B10815 {
#   public static void main(String[] args) {
#      System.out.print("ÀÔ·Â");
#      Scanner scanner = new Scanner(System.in);
#      HashSet<Integer> set1 = new HashSet<Integer>();
#      int l1 = scanner.nextInt();
#      for (int i=0; i<l1; i++) {
#         set1.add(scanner.nextInt());
#      }
#      int l2 = scanner.nextInt();
#      int [] check = new int [l2];
#      for (int i=0; i<l2; i++) {
#         int num = scanner.nextInt();
#         check[i]= num;
#      }
     
#      for(int j=0; j<l2; j++) {
#         if(set1.contains(check[j])){
#            System.out.print(1);
#         } else {
#            System.out.print(0);
#         }System.out.print(" ");
#      }
#      scanner.close();
#   }
# }