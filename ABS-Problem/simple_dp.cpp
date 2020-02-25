#include <bits/stdc++.h>
#include <boost/format.hpp>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
vector<string> devides = {"dream", "dreamer", "erase", "eraser"};

bool dp[100010];

int main() {
  string S;
  cin >> S;
  dp[0] = true;
  rep(i, S.size()) {
    if (!dp[i])
      continue;
    else {
      for (auto &item : devides) {
        if (S.substr(i, item.size()) == item) {
          dp[i + item.size()] = true;
        }
      }
    }
  }
  if (dp[S.size()]) {
    cout << "YES" << endl;
  } else {
    cout << "NO" << endl;
  }
  return 0;
}

