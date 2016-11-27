#include<iostream>
using namespace std;

int gcd(int a, int b){
    return a == 0 ? b : gcd(b % a, a);
}

int main(){
    int nums = 0;
    cin >> nums;
    while (nums --){
        int p, q;
        cin >> p >> q;
        int m = 2 * q;
        while (gcd(p, m) != q){
            m += q;
        }
        cout << m;
    }
    return 1;
}
