

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        int[] dp = new int[1001];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++)
            dp[i] = (dp[i - 1] + dp[i - 2]) % 10007;

        System.out.println(dp[n]);

    }
}

