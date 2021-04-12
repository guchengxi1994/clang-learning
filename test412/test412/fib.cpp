#include<iostream>

using namespace std;

int fib(int n){
    //cout<<"test"<<endl;
    if(n<=2){
        return 1;
    }else{
        //cout<<fib(n-2)<<endl;
        return fib(n-2) + fib(n-1);
    }
}
