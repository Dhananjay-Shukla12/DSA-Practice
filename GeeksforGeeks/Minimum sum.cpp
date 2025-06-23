class Solution {
  public:
  
  string strAdd(string a, string b){
      reverse(a.begin(),a.end());
      reverse(b.begin(),b.end());
      int carry = 0;
      string answer = "";
      int i=0; int j=0;
      while(i<a.size() && j<b.size()){
          int rem = (a[i]-'0')+(b[j]-'0')+carry;
          carry = rem/10;
          answer.push_back((char)((rem%10)+'0'));
          i++;
          j++;
      }
      while(i<a.size()){
          int rem = (a[i]-'0')+carry;
          carry = rem/10;
          answer.push_back((char)((rem%10)+'0'));
          i++;
      }
      
       while(j<b.size()){
          int rem = (b[j]-'0')+carry;
          carry = rem/10;
          answer.push_back((char)((rem%10)+'0'));
          j++;
      }
      while(carry){
          int rem = carry;
          carry = rem/10;
          answer.push_back((char)((rem%10)+'0'));
      }
      return answer;
  }
    string minSum(vector<int> &arr) {
        // code here
        sort(arr.begin(),arr.end());
        
        string p = "";
        string q = "";
        for(int i=0;i<arr.size();++i){
            if(i%2==0)p+=to_string(arr[i]);
            else q+=to_string(arr[i]);
        }
        
        string ans  = strAdd(p,q);
        
        while(!ans.empty() and ans.back()=='0')ans.pop_back();
        reverse(ans.begin(),ans.end());
        if(ans.empty())return "0";
        return ans;
    }
};