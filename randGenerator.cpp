#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>

void print_bits(int number) {
    for (int i = 31; i >= 0; i--) {
        printf("%d", (number >> i) & 1);
    }
    printf("\n");
}

void read(){
    FILE *file = fopen("rand_numbers.bin", "rb");
    int random_number;
    while (fread(&random_number, sizeof(int), 1, file) == 1) {
        printf("%d\n", random_number);
    }
    fclose(file);
}

int main() {
    int num_random_numbers = 5000000;

    FILE *file = fopen("rand_numbers.bin", "wb");
    for (int i = 0; i < num_random_numbers; i++) {
        int random_number = rand();
        fwrite(&random_number, sizeof(int), 1, file);
    }

    fclose(file);
    return 0;
}
