
N = int(input("길이를 입력해주세요: "))
A = input("정수 배열 A를 입력하세요: ")
B = input("정수 배열 B를 입력하세요: ")
A = A.split()
B = B.split()

A = [int(A[i]) for i in range(N)]
B = [int(B[i]) for i in range(N)]

print(A)
max_B = int(B.index(max(B)))
min_A = int(A.index(min(A)))
print("B의 가장 큰 값의 인덱스 : ",max_B)
print("A의 가장 작은 값의 인덱스 : ",min_A)

# 




for __ in range(N):
    A[max_B],A[min_A] = A[min_A], A[max_B]

print(A)


