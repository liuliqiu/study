#include <stdio.h>
#include <math.h>

#define square(x) (x)*(x)

void slove(float (*cord)[2], int n){
    float dist[n][n];
    int i, j;
    for(i=0;i<n;i++)
        for(j=0;j<n;j++)
            dist[i][j] = sqrt(square(cord[i][0]-cord[j][0]) + square(cord[i][1] - cord[j][1]));
    
    
    }

void main(){
    int n, i;
    scanf("%d", &n);
    float cord[n][2];
    for (i=0; i<n; i++){
        scanf("%f %f", &cord[i][0], &cord[i][1]);
    }
    slove(cord, n);
}
