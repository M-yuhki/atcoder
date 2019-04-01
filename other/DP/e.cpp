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
//long long dp[110][100010];

int main() {
    cin >> N >> W;
    for (int i = 0; i < N; ++i) cin >> w[i] >> v[i];
    
    int wmax = 10;
    int vmax = 0;
    for (int i = 0; i < N; ++i){
      wmax = wmax + w[i];
      vmax = vmax + v[i];
    }

    long long dp[110][vmax];

    for (int i= 0; i < N;++i){
      for (int j=0; j <vmax ; ++ j) dp[i][j] = wmax + 100;  
    }

    cout << dp[1][1] << endl;

    // ループ
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j <= vmax; ++j){
        if(j - v[i] >= 0){
          chmin(dp[i+1][j],dp[i][j-v[i]] + w[i]);
          }
        chmin(dp[i+1][j],dp[i][j]);
        
      }
    }

    // 最適値の出力
    long long res = 0;
    for (int sum_v = 0; sum_v < vmax; ++sum_v) {
        if (dp[N][sum_v] <= W) res = sum_v;
    }
    cout << res << endl;


}
