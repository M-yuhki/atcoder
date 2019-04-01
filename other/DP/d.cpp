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
long long w[110];
long long v[110];
int f;

// DP テーブル
long long dp[110][100010] = {0};

int main() {
    cin >> N >> W;
    for (int i = 0; i < N; ++i) cin >> w[i] >> v[i];

    // ループ
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j <= W; ++j){
        if(j - w[i] >= 0){
          chmax(dp[i+1][j],dp[i][j-w[i]] + v[i]);
          }
        chmax(dp[i+1][j],dp[i][j]);
        
      }
    }

    // 答え
    cout << dp[N][W] << endl;

}
