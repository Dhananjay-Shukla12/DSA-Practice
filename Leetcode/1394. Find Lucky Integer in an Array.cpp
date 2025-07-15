class Solution {
public:
    int findLucky(vector<int>& arr) {
        map<int,int> m;
        for(auto x:arr)m[x]++;
        int maxn = -1;
        for(auto y:m){
            if(y.first==y.second)maxn = max(maxn,y.first);
        }
        return maxn;
    }
};