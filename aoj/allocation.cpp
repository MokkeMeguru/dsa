#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;

bool check_split(int &k, int &mid, vector<int> ws) {
  auto cars = 0;
  auto weights = 0;
  for (auto &item : ws) {
    if (weights + item > mid) {
      cars++;
      weights = 0;
    }
    weights += item;
  }
  return cars < k;
}

int main() {
  int n, k;
  cin >> n >> k;
  vector<int> ws;
  int wi;
  rep(i, n) {
    cin >> wi;
    ws.push_back(wi);
  }
  auto left = *max_element(ws.begin(), ws.end());
  auto right = accumulate(ws.begin(), ws.end(), 0);
  auto mid = 0;
  while (right - left > 1) {
    mid = (left + right) / 2;
    if(check_split(k, mid, ws))
      right = mid;
    else
      left = mid;
  }
  if (check_split(k, left, ws))
    cout << left <<endl;
  else
    cout << right << endl;
}
