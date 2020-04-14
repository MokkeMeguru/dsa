#include <bits/stdc++.h>
#include <iostream>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int count(string s, char c) {
  auto res = 0;
  for(auto item: s) {
    if (item == c) res++;
  }
  return res;
}

vector<string> solve(int K, string S, int acc, int C) {
  vector<string> result;
  if (K == 0) {
    result.push_back(S);
  } else if (acc + C > S.size()) {

  } else if (K > count(string(S.begin() + acc + C, S.end()), 'o')) {
  } else {
    for (int i = acc + C; i < S.size(); ++i) {
      if(S.at(i) == 'o') {
        auto temp = string(S.begin(), S.end());
        temp[i] = 'c';
        auto _result = solve(K - 1, temp, i + 1, C);
        copy(_result.begin(), _result.end(), back_inserter(result));
      }
    }
  }
  return result;
}


int main(void) {
  int N, K, C;
  cin >> N >> K >> C;
  vector<string> results;
  string S;
  cin >> S;
  auto result = solve(K, S, 0 - C, C);
  vector<int> temp = vector<int>(N, 0);
  rep(i, N) {
    for(auto res: result) {
      if (res[i] == 'c') {
        temp.at(i) += 1;
      }
    }
  }

  rep(i, temp.size()){
    if (temp[i] == result.size())
      cout << i + 1 << endl;
  }
  

  return 0;
}
