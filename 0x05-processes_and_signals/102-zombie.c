#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int infinite_while(void)
{
        while (1)
            sleep(1);
        return (0);
}
