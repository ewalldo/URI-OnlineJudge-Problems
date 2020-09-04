#include <stdio.h>
#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <string.h>
   
using namespace std;

int main()
{
   char *v1, *v2, *v3, *v4, value[100];
   int v1_i;
   float v2_f;
   
   cin.get(value, 100);
   v1 = strtok(value," ");
   v2 = strtok(NULL," ");
   v3 = strtok(NULL," ");
   v4 = strtok(NULL,"");
   
   v1_i = atoi(v1);
   v2_f = atof(v2);
   printf("%d%.6f%s%s\n",v1_i, v2_f, v3, v4);
   printf("%d\t%.6f\t%s\t%s\n",v1_i, v2_f, v3, v4);
   printf("%10d%10.6f%10s%10s\n",v1_i, v2_f, v3, v4);
}