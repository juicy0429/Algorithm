# import java.io.BufferedReader;
# import java.io.InputStreamReader;
# import java.util.Arrays;
# // 백준 1300번 자바
# public class One300 {
#    public static void main(String[] args)throws Exception{
#        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
#        int a = Integer.parseInt(br.readLine());
#        int[] Karma = new int[a*a];
#        int n =1;
#        for(int i=0;i<a;i++){
#            Karma[i] = i+1;
#        }
#        while(n<a){
#        for(int j=n*a;j<(n+1)*a;j++){
#            Karma[j] = (j+1-(n*a))*(n+1);
#          }
#        n++;
#        }
#        Arrays.sort(Karma);
#        BufferedReader brr = new BufferedReader(new InputStreamReader(System.in));
#        int aa = Integer.parseInt(brr.readLine());
#        System.out.println(Karma[aa-1]);
#        BufferedReader brrr = new BufferedReader(new InputStreamReader(System.in));
#        int aaa = Integer.parseInt(brrr.readLine());
#        int l = Integer.parseInt(brrr.readLine());
#        sol sl = new sol(aaa,l);
#        System.out.println(sl.koala(aaa,l));
#    }
# }
# class sol {
#    int a;
#    int l;
#    public sol(int a, int l){
#        this.a = a;
#        this.l = l;
#    }
#    public int koala(int a, int l){
#        int high = l;
#        int low = 1;
#        int mid = 0;
#        int sum = 0;
#        int answer = 0;
#        while(low <= high) {
#            mid = (high + low) / 2;
#            sum = 0;
#            for(int i = 1; i <= a; i++)
#                sum += Math.min(mid / i, a);
#              System.out.println("sum"+sum);
#            if(sum >= l) {
#                high = mid - 1;
#                System.out.println("high"+high);
#                answer = mid;
#            }else{
#                low = mid + 1;
#            }
#        }
#        return answer;
#    }
# }

# while(low <= high) {
#            mid = (high + low) / 2;
#            sum = 0;
#            for(int i = 1; i <= a; i++)
#                sum += Math.min(mid / i, a);
#              System.out.println("sum"+sum);
#            if(sum >= l) {
#                high = mid - 1;
#                System.out.println("high"+high);
#                answer = mid;
#            }else{
#                low = mid + 1;
#                System.out.println("low"+low);
#            }
#        }
#        return answer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
​
public class back1300 {
​
    static int N;
    static long K;
​
    public static void main(String[] args) throws IOException {
        // TODO Auto-generated method stub
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken()); //문제에선 3에 해당
        st = new StringTokenizer(br.readLine());
        K = Long.parseLong(st.nextToken()); // 문제에선 7에 해당
​
        //일차원 배열에 오름 차순으로 정렬할 때 k번째 수 구하기
​
        long s = 1, e = K, mid = 0, ans = 0;
        //s = 시작지점, e = 끝위치
        while (s <= e) // parametric search
        {
            //mid값을 설정
            mid = (s + e) / 2;
            //갯수 = cnt
            long cnt = 0;
​
            for (int i = 1; i <= N; i++) {
                // 몫이 N보다 큰 경우에는 그 개수가 N개인 것과 동일하므로..
                // e보다 작은 숫자의 갯수 구하기
                cnt += min(N, mid / i);
            }
            if (cnt < K) s = mid + 1;
            else {
                e = mid - 1;
                ans = mid;
            }
​
        }
        System.out.println(ans);
    }
​
    public static long min(long a, long b) {
        return a > b ? b : a;
    }
}