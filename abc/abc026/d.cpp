#include <bits/stdc++.h>
#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
#include <string>
#include <regex>
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)
#define ARRAY_LEN(ARR) (sizeof(ARR) / sizeof((ARR)[0]))
using namespace std;

double f(int a,int b,int c,int t){
  return a*t + b * sin(c * 3.14159265358979323846264 *t);
}

int main(void){
  int a;
  int b;
  int c;
  cin >> a >> b >> c;
  double l;
  double r;
  double t;
  l = 0.0;
  r = (100+b)/a + 10.0;
  
  while(true){
    double fl;
    double ft;
    double fr;
    fl = f(a,b,c,l);
    ft = f(a,b,c,t); 
    fr = f(a,b,c,r);
    
    if( fabs(ft - 100.0) < 0.0000001 ) break;

    else if(100.0 < fl && ft < 100.0 ) r = t;
    else l = t;
 
  }

  printf("%.10lf\n", t);  

}

