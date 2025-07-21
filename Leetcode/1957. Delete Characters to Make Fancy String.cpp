class Solution {
public:
    string makeFancyString(string s) {
        int n = s.size();
        string ans = "";
        ans.push_back(s[0]);
        int k = 1;
        char prev =s[0];
        for(int i=1;i<n;++i){
            if(s[i]==prev){
                k++;
            }
            else{
                prev = s[i];
                k=1;

            }
            if(k<3)ans.push_back(s[i]);
        }
        return ans;
    }
};