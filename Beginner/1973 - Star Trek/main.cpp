#include <stdio.h>
#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <string>
   
using namespace std;
 
int main() {
 
    long long int value, n_atacados = 0, n_roubados = 0, now = 0, total_c = 0, atual = 0;
    
    cin >> value;
    
    int carneiro[value];
    int atacados[value] = {0};
    for (int i = 0; i < value; i++)
    {
        cin >> carneiro[i];
        total_c += carneiro[i];
    }
    
    while(true)
    {
        atual = carneiro[now];
        if (carneiro[now] > 0)
        {
            n_roubados += 1;
            if (atacados[now] == 0)
            {
                atacados[now] = 1;
                n_atacados += 1;
            }
            carneiro[now] -= 1;
        }
        if (atual % 2 == 0)
        {
            now -= 1;
        }
        else
        {
            now += 1;
        }
        if (now < 0 || now >= value)
        {
            break;
        }
    }
    
    cout << n_atacados << " " << (total_c - n_roubados) << endl;
    return 0;
}