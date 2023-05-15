#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

int main(void)
{
	char *command = NULL;
	size_t bufsize = 0;

    while (1)
    {
        printf("Cisfun$ ");
        if (getline(&command, &bufsize, stdin) == -1)
	{
            perror("getline");
            exit(1);
        }

        // Remove newline character from the end of the command
        command[strcspn(command, "\n")] = '\0';

        // Exit the shell if the user enters "exit" command
        if (strcmp(command, "exit") == 0)
            break;

        // Fork a child process to execute the command
        pid_t child_pid = fork();

        if (child_pid == -1)
	{
            perror("fork");
            exit(1);
        }
        else if (child_pid == 0)
	{
            // Child process
            char *args[] = {command, NULL};
            if (execve(command, args, NULL) == -1)
	    {
                perror("execve");
                exit(1);
            }
        }
        else {
            // Parent process
            int status;
            waitpid(child_pid, &status, 0);
        }
    }
    free(command);
    return 0;
}
