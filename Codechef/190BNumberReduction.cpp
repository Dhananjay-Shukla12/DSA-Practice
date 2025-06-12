#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int target;
	cin>>target;
	while(target--){
	    int x;
	    cin>>x;
	    if(x>3){
	        while(x>3)x=x-3;
	        if(x%2==0)x=x/2;
	        cout<<x<<endl;
	    }
	    else if(x%2==0)cout<<x/2<<endl;
	    else cout<<x<<endl;
	}
	return 0;
}
