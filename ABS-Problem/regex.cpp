#include <bits/stdc++.h>
#include <boost/format.hpp>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;

int main() {
  string S;
  cin >> S;
  auto result = regex_match(S, regex("(dream(er)?|erase(r)?)*"));
  if (result) {
    cout << "YES" <<endl;
  } else {
    cout << "NO" << endl;
  }
  return 0;
}

