#include <iostream>
 
using namespace std;

int main(int argc, char** argv)
{
    int X, Y, M;
    int A, B;

    while(scanf("%d %d %d", &X, &Y, &M)!=EOF)
    {
        while(M-- > 0)
        {
            scanf("%d %d", &A, &B);

            if ( A<=X && B<=Y)
                cout << "Sim" << endl;
            else if(A<=Y && B<=X)
                cout << "Sim" << endl;
            else
                cout << "Nao" << endl;
        }
    }
    return 0;
}