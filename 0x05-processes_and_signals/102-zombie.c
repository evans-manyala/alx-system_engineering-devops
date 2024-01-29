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

int main(void)
{
	pid_t pid;
   int i;

   for (i = 0; i < 5; i++) {
       pid = fork();

       if (pid < 0) {
           perror("fork");
           exit(1);
       } else if (pid == 0) {
           /* Child process */
           exit(0); /* Child exits immediately, creating a zombie */
       } else {
           /* Parent process */
           printf("Zombie process created, PID: %d\n", pid);
       }
   }
}