#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi; 
typedef pair<int,int> pi;
#define PB push_back
int main(){
ios::sync_with_stdio(0);
cin.tie(0);
ll t;
cin>>t;
while(t--){
    ll n,x;
    cin>>n>>x;
    ll a[n];
    for(ll i=0;i<n;++i)cin>>a[i];
    ll first =0;
    ll last = 0;
    for(ll i=0;i<n;++i){
        if(a[i]==1){
            first = i;
            break;
        }
    }
    for(ll i=0;i<n;++i){
        if(a[i]==1)last=i;
    }
    if((last-first)+1<=x)cout<<"YES"<<endl;
    else cout<<"NO"<<endl;
}
return 0;
}

