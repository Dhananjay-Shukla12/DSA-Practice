class Solution {
public:
    int minMaxDifference(int num) {
        string t = to_string(num);
        string piku = to_string(num);
        int j = 0;
        for(int i=0;i<t.size();++i){
            if(t[i]!='9'){
                j=i;
                break;
            }
        }
        char samy = t[j];
        for(int i=j;i<t.size();++i){
            if(t[i]==samy){
                t[i]='9';
            }
        }
        int p = stoi(t);
        char dj = piku[0];
        for(int i=0;i<piku.size();++i){
            if(dj==piku[i])piku[i]='0';
        }

        int q = stoi(piku);
        return p-q;
    }
};