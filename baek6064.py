"""
백준 - 6064번(카잉 달력)
https://www.acmicpc.net/problem/6064
​
문제
최근에 ICPC 탐사대는 남아메리카의 잉카 제국이 놀라운 문명을 지닌 카잉 제국을 토대로 하여 세워졌다는 사실을 발견했다. 카잉 제국의 백성들은 특이한 달력을 사용한 것으로 알려져 있다. 그들은 M과 N보다 작거나 같은 두 개의 자연수 x, y를 가지고 각 년도를 <x:y>와 같은 형식으로 표현하였다. 그들은 이 세상의 시초에 해당하는 첫 번째 해를 <1:1>로 표현하고, 두 번째 해를 <2:2>로 표현하였다. <x:y>의 다음 해를 표현한 것을 <x':y'>이라고 하자. 만일 x < M 이면 x' = x + 1이고, 그렇지 않으면 x' = 1이다. 같은 방식으로 만일 y < N이면 y' = y + 1이고, 그렇지 않으면 y' = 1이다. <M:N>은 그들 달력의 마지막 해로서, 이 해에 세상의 종말이 도래한다는 예언이 전해 온다. 
예를 들어, M = 10 이고 N = 12라고 하자. 첫 번째 해는 <1:1>로 표현되고, 11번째 해는 <1:11>로 표현된다. <3:1>은 13번째 해를 나타내고, <10:12>는 마지막인 60번째 해를 나타낸다. 
네 개의 정수 M, N, x와 y가 주어질 때, <M:N>이 카잉 달력의 마지막 해라고 하면 <x:y>는 몇 번째 해를 나타내는지 구하는 프로그램을 작성하라. 
​
입력
입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 구성된다. 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 각 테스트 데이터는 한 줄로 구성된다. 각 줄에는 네 개의 정수 M, N, x와 y가 주어진다. (1 ≤ M, N ≤ 40,000, 1 ≤ x ≤ M, 1 ≤ y ≤ N) 여기서 <M:N>은 카잉 달력의 마지막 해를 나타낸다.
​
출력
출력은 표준 출력을 사용한다. 각 테스트 데이터에 대해, 정수 k를 한 줄에 출력한다. 여기서 k는 <x:y>가 k번째 해를 나타내는 것을 의미한다. 만일 <x:y>에 의해 표현되는 해가 없다면, 즉, <x:y>가 유효하지 않은 표현이면, -1을 출력한다.
"""
​
"""
Solution: 이 문제는 Brute Force 유형으로, 무식하게 하면 풀립니다. 근데 시간 초과 뜨는건 함정.ㅎㅎ
하지만 모든 숫자를 다 확인하기엔 숫자 범위가 크므로 규칙을 파악하여 계산함으로 시간을 줄일 수 있습니다.
1. 각 (x, y)의 값을 1씩 빼준 후 규칙을 찾기.
2 ex) M, N = 5, 7 일때
    -> 0: (0, 0)    7: (2, 0)     
    -> 1: (1, 1)    8: (3, 1)
    -> 2: (2, 2)    9: (4, 2)
    -> 3: (3, 3)    10: (0, 3)
    -> 4: (4, 4)    11: (1, 4)
    -> 5: (0, 5)    12: (2, 5)
    -> 6: (1, 6)    13: (3, 6) ...
3. 여기서 x의 자리를 보면 동일한 숫자가 올 주기가 5임을 알 수 있다.
    -> ex) 3: (3,3) -> 8: (3,1) -> 13: (3,4)
4. 이를 도식화하면 (i x M)이므로 이 경우만 확인하면 끝.
"""
​
N = int(input())
​
for _ in range(N):
    m, n, x, y = map(int ,input().split())
​
    x -= 1
    y -= 1
    k = x
    while k < n*m:
        if k % n == y:
            print(k+1)
            break
        k += m
    else:
        print(-1)