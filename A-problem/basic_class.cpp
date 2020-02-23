#include <bits/stdc++.h>
#include <boost/format.hpp>
using namespace std;

class Clock {
  int hour;
  int minute;
  int second;
  int day = 24 * 60 * 60;
    public : void set(int h, int m, int s) {
    this->hour = h;
    this->minute = m;
    this->second = s;
  }
  string to_str() {
    string str = (boost::format("%02d:%02d:%02d") % this->hour %
                  this->minute % this->second)
                           .str();
    return str;
  }
  void shift(int diff_second) {
    auto now = this->hour * 60 * 60 + this->minute * 60 + this->second;
    now += diff_second;
    if (now < 0) {
      now += this->day;
    } else if (now >= this->day ) {
      now -= this->day;
    }
      auto hour = now / (60 * 60);
    auto minute = now / 60 % 60;
    auto second = now %  60;
    this->hour = hour;
    this->minute = minute;
    this->second = second;
  }
};

// -------------------
// ここから先は変更しない
// -------------------

int main() {
  // 入力を受け取る
  int hour, minute, second;
  cin >> hour >> minute >> second;
  int diff_second;
  cin >> diff_second;

  // Clock構造体のオブジェクトを宣言
  Clock clock;

  // set関数を呼び出して時刻を設定する
  clock.set(hour, minute, second);

  // 時刻を出力
  cout << clock.to_str() << endl;

  // 時計を進める(戻す)
  clock.shift(diff_second);

  // 変更後の時刻を出力
  cout << clock.to_str() << endl;
}
