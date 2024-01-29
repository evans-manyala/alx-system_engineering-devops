#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * infinite_while - Creates Zombie processes infinitely
 * Return: Zero if successful
*/
int infinite_while(void)
{
	while (1)
		sleep(1);
	return (0);
}
/**
 * main - Program creates the main parent process.
 * Return: Zero if successful
*/
int main(void)
{
	pid_t pid;
	int x;

	for (x = 0; x < 5; x++)
	{
		pid = fork();

		if (pid < 0)
		{
			perror("fork");
			exit(1);
		}
		else if (pid == 0)
		{
			/* Child process */
			printf("Zombie process created, PID: %d\n", pid);
			exit(0); /* Child exits immediately, creating a zombie */
		}
		else
		{
			/* Parent process */
			sleep(1);  /* Sleep for a short time to allow child to become a zombie */
		}
	}
	infinite_while();
	return (0);
}
