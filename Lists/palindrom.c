#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool isPalindrome(const char *str) {
    int length = strlen(str);
    for (int i = 0; i < length / 2; i++) {
        if (str[i] != str[length - i - 1]) {
            return false; // Not a palindrome
        }
    }
    return true; // It's a palindrome
}

int main() {
    const char *example1 = "level";
    const char *example2 = "hello";

    if (isPalindrome(example1)) {
        printf("%s is a palindrome.\n", example1);
    } else {
        printf("%s is not a palindrome.\n", example1);
    }

    if (isPalindrome(example2)) {
        printf("%s is a palindrome.\n", example2);
    } else {
        printf("%s is not a palindrome.\n", example2);
    }

    return 0;
}

