#include <stdio.h>

int max(int a, int b){
    return a>b?a:b;
}
int min(int a, int b){
    return a<b?a:b;
}
int print_array(int A[], int A_len){
    int i;
    for(i=0;i<A_len;i++){
        printf("%d ", *(A+i));
    }
    printf("\n");
}

int max_contiguous_subsequence_sum(int A[], int A_len){
    // ex6.1
    int i, c = 0, m = 0;
    // c max contiguous subsequence sum contain A[i]
    // m max contiguous subsequence sum
    for(i=0;i<A_len;i++){
        c = max(c, 0) + A[i];
        m = max(c, m);
    }
    return m;
};

int trip_penalty(int A[], int A_len){
    // ex6.2
    int B[A_len+1];
    int C[A_len+1];
    int i, j, tmp;
    B[0] = 0;
    C[0] = 0;
    for(i=0;i<A_len;i++){
        B[i+1] = A[i];
        C[i+1] = -1;
    }

    for(i=1;i<A_len+1;i++){
        for(j=i-1;(j>=0)&&(B[i]-B[j]<=200);j--){
            tmp = C[j] + (200 - B[i] + B[j]) * (200 - B[i] + B[j]);
            if(C[i] < 0)
                C[i] = tmp;
            else
                C[i] = min(tmp, C[i]);
        }
    }

    return C[A_len];
}

main(){
    int result;

    int a[] = {5, 15, -30, 10, -5, 40, 10, -10};
    result = max_contiguous_subsequence_sum(a, 8);
    printf("ex6.1: %d\n", result);

    int a2[] = {50, 150, 180, 230, 250, 310, 390, 460};
    //int a2[] = {50, 150, 200, 250, 250, 310, 390, 400};
    result = trip_penalty(a2, 8);
    printf("ex6.2: %d\n", result);


}
