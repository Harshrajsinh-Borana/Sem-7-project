#include <iconv.h>
#include <stdio.h>

int main() {
    iconv_t conv = iconv_open("UTF-8", "ISO-8859-1");
    if (conv == (iconv_t)-1) {
        perror("iconv_open failed");
        return 1;
    }
    printf("libiconv is working correctly.\n");
    iconv_close(conv);
    return 0;
}
