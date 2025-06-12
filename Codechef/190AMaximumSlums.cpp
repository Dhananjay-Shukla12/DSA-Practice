#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int target;
	cin>>target;
	int goal = 25;
	float remain = goal-target;
	if(remain<=0)cout<<0<<endl;
	else {int ans = ceil(float(remain/4));
	    cout<<ans<<endl;
	}
	return 0;
}
