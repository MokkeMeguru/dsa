#include <bits/stdc++.h>
#include <boost/format.hpp>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;

int main() {
  int N, Y;
  cin >> N >> Y;
  rep(i, N + 1) {
    if(i * 10000 > Y) break;
    rep(j, N - i + 1) {
      if (i * 10000 + j * 5000 + (N - i - j) * 1000 == Y) {
        cout << (boost::format("%d %d %d") % i % j % (N - i - j)).str() << endl;
        goto ext;
      }
    }
  }
  cout << "-1 -1 -1\n";
   ext:
  return 0;
}
