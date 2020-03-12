#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < int(n); i++)
#define SENTINEL INT_MAX
#define delimiter " "
using namespace std;

int main() {
  string s;
  while(true) {
    getline(cin, s);
    size_t pos;
    vector<int> vec;
    int temp;
    while((pos = s.find(delimiter)) != string::npos) {
      auto token = s.substr(0, pos);
      try {
        temp = stoi(token);
        vec.push_back(temp);
      }
      catch (const invalid_argument &e) {
        cout << "token" << token << endl;
      }
      // -1 for null-terminated string
      s.erase(0, pos + sizeof(delimiter) -1);
    }
    for(auto &item: vec) {
      cout << item << endl;
    }
    if (cin.bad() || cin.eof()) {
      cout << "endline" << endl;
      break;
    }
  }
  return 0;
}
