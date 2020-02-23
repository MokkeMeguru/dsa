#include <bits/stdc++.h>
using namespace std;

int main() {
  int N, M;
  cin >> N >> M;
  vector<int> A(M), B(M);
  for (int i = 0; i < M; i++) {
    cin >> A.at(i) >> B.at(i);
  }
  vector<vector<int>> table(N, vector<int>(N, 0));
  for (int i = 0; i < M; ++i) {
    table.at(A.at(i) - 1).at(B.at(i) - 1)++;
    table.at(B.at(i) - 1).at(A.at(i) - 1)--;
  }
  for (auto row : table) {
    for (int i = 0; i < int(row.size()); ++i) {
      int item = row.at(i);
      if (item > 0) {
        cout << 'o';
      } else if (item < 0) {
        cout << 'x';
      } else {
        cout << '-';
      }
      if (i != int(row.size()) - 1) {
        cout << " ";
      }
    }
    cout << endl;
  }
  // ここにプログラムを追記
  // (ここで"試合結果の表"の2次元配列を宣言)
}
