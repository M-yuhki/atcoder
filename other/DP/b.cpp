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

const long long INF = 1LL << 60;

// 入力
int N;
int K;
long long h[100010];

// DP テーブル
long long dp[100010];

int main() {
    cin >> N >> K;
    for (int i = 0; i < N; ++i) cin >> h[i];

    // 初期化 (最小化問題なので INF に初期化)
    for (int i = 0; i < 100010; ++i) dp[i] = INF;

    // 初期条件
    dp[0] = 0;

    // ループ
    for (int i = 1; i < N; ++i) {
      for(int j = max(0,i-K); j<i;j++){
        chmin(dp[i],dp[j]+abs(h[j]-h[i]));
      }
    }

    // 答え
    cout << dp[N-1] << endl;
}
