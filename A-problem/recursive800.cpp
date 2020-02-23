#include <bits/stdc++.h>
using namespace std;

// 木の構築をする (再帰関数)
int dps(vector<vector<int>> &winners, int N, int i) {
  // 葉 つまり一回戦負けの場合は、深さはないので 0
    if (winners[i].size() == 0) {
    return 0;
  }
    // i の 敗者 それぞれがどれくらいの深さの木を構築しているのかをチェックする
  vector<int> depth;
  for (auto v : winners[i]) {
    depth.push_back(dps(winners, N, v));
  }
  // 敗者の木の深さを大きい順にソートする
  sort(depth.begin(), depth.end(), greater<int>());

  // 木を浅くするには、早い段階で小さい木に当たる
  // => 深い段階で大きい木に当たる
  // 現在の木の深さは (敗者の木の長さに +  当たった深さ)
  // e.g. 一回戦 : 1, 二回戦: 2
  int j = 1;
  for (auto &item : depth) {
    // ここで 敗者それぞれの深さ -> i から見た深さに変える
    item += j;
    j++;
  }
  // i から見て  一番深かったときの深さを返す。
  return *max_element(depth.begin(), depth.end());
}

int main() {
  int N;
  cin >> N;
  vector<vector<int>> winners(N + 1);
  for (int i = 2; i < N + 1; ++i) {
    int winner;
    cin >> winner;
    winners[winner].push_back(i);
  }
  cout << dps(winners, N, 1) << endl;
}
