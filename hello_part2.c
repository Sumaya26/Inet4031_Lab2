#include <stdio.h>

int main() {
    char *user_list[] = {"User1", "User2", "User3"};
    int i;

    for (i = 0; i < 3; i++) {
        printf("%s\n", user_list[i]);
    }

    return 0;
}

