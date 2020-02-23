#include <bits/stdc++.h>
using namespace std;

int main()
{
  int N;
  cin >> N;
  vector<int> A(N, 0);
  for(auto &item: A) {
    cin >> item;
  }
  map<int, int> vals;
 for(auto &item: A) {
   if (!vals.count(item)) {
     vals[item] = 1;
   }
   else {
     vals.at(item)++;
   }
 }
 int count = 0;
 int k = 0;
 for(auto &item: vals) {
   if (count < item.second){
     count = item.second;
     k = item.first;
   }
 }
 cout << k << " " << count << endl;
}
