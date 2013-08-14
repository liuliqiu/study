#include <stdio.h>

int max(int a, int b){
    return a>b?a:b;
}

int max_contiguous_subsequence_sum(int A[], int A_len){
    int i, c = 0, m = 0;
    for(i==0;i<A_len;i++){
        c = max(c, 0) + A[i];
        m = max(c, m);
    }
    return m;
};

main(){
    int a[] = {5, 15, -30, 10, -5, 40, 10, -10};
    int result;
    result = max_contiguous_subsequence_sum(a, 8);
    printf("%d\n", result);
}
