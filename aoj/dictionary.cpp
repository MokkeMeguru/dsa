#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;

#define dictsize int(pow(5.0, 12.0))
int dict[dictsize] = {};

map<char, int> dict_to_key = {
    {'A', 1},
    {'C', 2},
    {'G', 3},
    {'T', 4},
};

int name_to_key(string &str) {
  auto res = 0;
  for(auto &item : str) {
    res = res * 4 + dict_to_key[item];
  }
  return res;
}

int main() {
  int N;
  cin >> N;
  string operate;
  string name;
  rep (i, N) {
    cin >> operate >> name;
    if (operate == "insert"){
      dict [name_to_key(name)] = 1;
    } else {
      if (dict [name_to_key(name)])
        cout << "yes" << endl;
      else
        cout << "no" << endl;
    }
  }
}
