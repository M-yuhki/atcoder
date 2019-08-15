#include <bits/stdc++.h>
#include <iostream>
#include <algorithm>
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)
using namespace std;
int main(void){
    int a;
    int b;
    cin >> a >> b;
    cout << max({a+b,a-b,a*b}) << endl;
}
