#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

/**
 * infinite_while - sleep for life
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - entry point
 * Creates 5 zombie processes
 * Return: 0
 */
int main(void)
{
	int i;

	for (i = 0; i < 5; i++)
	{
		if (fork() == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			return (0);
		}
	}

	infinite_while();
	return (0);
}

