#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
vector<string> devides = {"dream", "dreamer", "erase", "eraser"};

int main() {
  int N = 0;
  cin >> N;
  int tp = 0, xp = 0, yp = 0;
  int tc, xc, yc;
  bool reachable = true;
  rep(i, N) {
    cin >> tc >> xc >> yc;
    auto diffd = abs(xc - xp) + abs(yc - yp);
    auto difft = tc - tp;
    if (!reachable) continue;
    if (diffd > difft) {
      reachable = false;
    }
    if ((diffd - difft) % 2 != 0) {
      reachable = false;
    }
    tp = tc;
    xp = xc;

    yp = yc;
  }
  if (reachable) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }
  


  return 0;
}

