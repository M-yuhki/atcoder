#include<iostream>
#include <vector>
#include <cstdlib>
#include <algorithm>

using namespace std; 

template<class T> inline bool chmin(T& a, T b) {
    if (a > b) {
        a = b;
        return true;
    }
    return false;
}
template<class T> inline bool chmax(T& a, T b) {
    if (a < b) {
        a = b;
        return true;
    }
    return false;
}

// 入力
int N;
int W;
long long a[100010][2];
int f;

// DP テーブル
long long dp[100010];

int main() {
    cin >> N >> W;
    for (int i = 0; i < N; ++i) cin >> a[i][0] >> a[i][1];

    // 初期化
    for (int i = 0; i < 100010; ++i) dp[i] = 0;

    // ループ
    for (int i = 1; i < N+1; ++i) {
      chmax(dp[i][0],dp[i-1][1] + a[i-1][0]);
      chmax(dp[i][0],dp[i-1][2] + a[i-1][0]);
      chmax(dp[i][1],dp[i-1][0] + a[i-1][1]);
      chmax(dp[i][1],dp[i-1][2] + a[i-1][1]);
      chmax(dp[i][2],dp[i-1][0] + a[i-1][2]);
      chmax(dp[i][2],dp[i-1][1] + a[i-1][2]);
    
    }

    // 答え
    cout << max({dp[N][0],dp[N][1],dp[N][2]}) << endl;

}
