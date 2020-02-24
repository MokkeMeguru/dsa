#include <bits/stdc++.h>
#include <boost/format.hpp>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;

int main() {
  int A, B, N;
  cin >> N >> A >> B;
  auto c = 0;
  rep(i, N + 1) {
    auto res = 0;
    res += int(i / 10000) % 10;
    res += int(i / 1000) % 10;
    res += int(i / 100) % 10;
    res += int(i / 10) % 10;
    res += i % 10;
    if (A <= res && res <= B)
      c += i;
  }
  cout << c << endl;
  return 0;
}
