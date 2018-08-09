#include<bits/stdc++.h>
using namespace std;

int main(){
printf("Enter prime number and primitive root and public key");
int q,g,y;
cin>>q>>g>>y;
printf("Enter the message and c1");
long k,m,c1;
cin>>m>>c1;
long pk=q-2;
int i;
for(i=0;;i++){
int f= pow(g,i);
if((f%q)==c1)
break;
}
int c2=m*pow(y,i);
cout<<c2%q<<endl;
return 0;
}
