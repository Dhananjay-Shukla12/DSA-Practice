#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int target;
	cin>>target;
	while(target--){
	    int x,y;
	    cin>>x>>y;
	    int disleft = 50-x;
	    int ans = 0;
	    for(int i=y;i<y+6;++i)
	    {for(int j=y;j<y+6;++j)
	        if((i+j)==disleft){
	            ans=1;
	            break;
	        }
	    }
	    if(ans==1)cout<<"Yes"<<endl;
	    else cout<<"No"<<endl;
	}
	return 0;
}
