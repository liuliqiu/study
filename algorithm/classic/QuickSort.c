#include <stdio.h>
#define NUMBER 10000

int quick_sort(int* array, int n){
    if(n<=1){
        return 0;
    }
    int pivot;
    int i, j;
    int temp;
    int middle = (n-1)/2;
    int pivot_index;
    if((array[0] - array[middle]) * (array[0] - array[n-1]) <= 0){
        pivot_index = 0;
    }else if((array[middle] - array[0])*(array[middle] - array[n-1]) <= 0){
        pivot_index = middle;
    }else{
        pivot_index = n - 1;
    }
    //pivot = array[0];
    pivot = array[pivot_index];
    array[pivot_index] = array[0];
    array[0] = pivot;
    i = j = 1;
    while(j < n){
        if(array[j] < pivot){
            temp = array[j];
            array[j] = array[i];
            array[i] = temp;
            i ++;
        }
        j ++;
    }
    array[0] = array[i - 1];
    array[i - 1] = pivot;
    int x, y;
    x = quick_sort(array, i - 1);
    y = quick_sort(array + i, n - i);
    return n - 1 + x + y;
}

show(int* array, int n){
    int i;
    for(i=0;i<n;i++){
        printf("%d ", array[i]);
    }
    printf("\n");
}

main(){
    int array[NUMBER];
    int i;
    for(i=0;i<NUMBER;i++) {
        scanf("%d", array + i);
    }
    int result;
    result = quick_sort(array, NUMBER);
    printf("%d\n", result);
    printf("%d %d\n", array[0], array[NUMBER - 1]);
}
