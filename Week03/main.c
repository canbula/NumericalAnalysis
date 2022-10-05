#include <stdio.h>
#include <time.h>

int statement() {
    int i, s=0;
    for (i=0;i<10000;i++) {
        s += i;
    }
    return s;
}

int main() {
    clock_t start = clock(), passed;
    int i;
    for (i=0;i<100;i++) {
        statement();
    }
    passed = clock() - start;
    //printf("%d \n", passed);
    //printf("%lu \n", passed / (long double) CLOCKS_PER_SEC);
    //printf("%Lf seconds \n", passed / (long double) CLOCKS_PER_SEC);
    printf("%Lf seconds", (long double) passed / (long double) CLOCKS_PER_SEC);
    return 0;
}
