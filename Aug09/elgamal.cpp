#include<bits/stdc++.h>
using namespace std;

int main(){
printf("Enter prime number and primitive root and public key");
int q,g,y;
cin>>q>>g>>y;
printf("Enter the random number and message");
long k,m;
cin>>k>>m;
long pk=q-2;
long c1=pow(g,k);
long c2=m*pow(y,k);
cout<<c1%q<<" "<<c2%q<<endl;

return 0;
}
