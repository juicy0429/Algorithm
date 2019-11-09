// import java.io.*;
// import java.util.*;
// ​
// public class back1620 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         int N = sc.nextInt();
//         int M = sc.nextInt();
// ​
//         HashMap<String, Integer> maps = new HashMap<>();
//         String Arr[] = new String[N];
// ​
//         for (int i = 0; i < N; i++){
//             String s = sc.next();
//             Arr[i] = s;
//             maps.put(s, i + 1);
//         }
// ​
//         for (int i = 0; i < M; i++){
//             if(sc.hasNextInt()){
//                 System.out.println(Arr[sc.nextInt() - 1]);
//             } else {
//                 System.out.println(maps.get(sc.next()));
//             }
//         }
//     }
// }

​
"""
백준 - 1620번(나는야 포켓몬 마스터)
https://www.acmicpc.net/problem/1620
​
입력
첫째 줄에는 도감에 수록되어 있는 포켓몬의 개수 N이랑 내가 맞춰야 하는 문제의 개수 M이 주어져. N과 M은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수인데, 자연수가 뭔지는 알지? 모르면 물어봐도 괜찮아. 나는 언제든지 질문에 답해줄 준비가 되어있어.
둘째 줄부터 N개의 줄에 포켓몬의 번호가 1번인 포켓몬부터 N번에 해당하는 포켓몬까지 한 줄에 하나씩 입력으로 들어와. 포켓몬의 이름은 모두 영어로만 이루어져있고, 또, 음... 첫 글자만 대문자이고, 나머지 문자는 소문자로만 이루어져 있어. 포켓몬 이름의 최대 길이는 20이야. 그 다음 줄부터 총 M개의 줄에 내가 맞춰야하는 문제가 입력으로 들어와. 문제가 알파벳으로만 들어오면 포켓몬 번호를 말해야 하고, 숫자로만 들어오면, 포켓몬 번호에 해당하는 문자를 출력해야해. 입력으로 들어오는 숫자는 반드시 1보다 크거나 같고, N보다 작거나 같고, 입력으로 들어오는 문자는 반드시 도감에 있는 포켓몬의 이름만 주어져. 그럼 화이팅
​
출력
첫째 줄부터 차례대로 M개의 줄에 각각의 문제에 대한 답을 말해줬으면 좋겠어!!!. 입력으로 숫자가 들어왔다면 그 숫자에 해당하는 포켓몬의 이름을, 문자가 들어왔으면 그 포켓몬의 이름에 해당하는 번호를 출력하면 돼. 그럼 땡큐~
"""
​
N, M = map(int, input().split())
​
item_list = list()
item_Dict = dict()
num = 1
for _ in range(N):
    item = input()
    item_list.append(item)
    item_Dict[item] = num        
    num += 1
for _ in range(M):
    question = input()
    if question.isdigit():
        print(item_list[int(question)-1])
    else:
        print(item_Dict[question])