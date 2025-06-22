class Solution {
public:
    vector<string> divideString(string s, int k, char fill) {
        vector<string> ans;
        if(k==s.size()){
            ans.push_back(s);
            return ans;
        }
        else if(k>s.size()){
            k=k-s.size();
            while(k--){
                s+=fill;
            }
            ans.push_back(s);
            return ans;
        }
        else{
            vector<string> v;
            string p="";
            for(int i=0;i<s.size();++i){
                if(p.size()==k){
                    v.push_back(p);
                    p="";
                    p+=s[i];
                }
                else{
                    p+=s[i];
                }
            }
            
            if(s.size()%k==0){
                if(p.size()!=0)v.push_back(p);
                return v;
            }
            else{
                int q = s.size()%k;
                k = k-q;
                while(k--){
                    p+=fill;
                }
                v.push_back(p);
                return v;
            }
        }
    }
};