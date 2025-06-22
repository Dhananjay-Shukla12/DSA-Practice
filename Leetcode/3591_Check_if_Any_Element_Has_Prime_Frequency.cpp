class Solution {
public:

bool isprime(int n){
    if(n<=1)return false;
    if(n==2)return true;
    for(int i=2;i<=sqrt(n);++i){
        if(n%i==0)return false;
    }
    return true;
}
    bool checkPrimeFrequency(vector<int>& nums) {
        map<int,int>m;
        for(auto x:nums){
            m[x]++;
        }
        for(auto x:m){
            if(isprime(x.second))return true;
        }
        return false;
    }
};