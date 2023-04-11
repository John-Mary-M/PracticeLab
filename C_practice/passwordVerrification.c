#include <stdio.h>
#include <string.h>
/**
 * main - validates user password
 * Returns: 0 on success.
 */
int main(void)
{
	char *p_pswd;
	char passwd[100];
	p_pswd = passwd; /*set pointer to refer to a char array*/
	char *actual = {"Fox Track Delta"};
	int result;

	printf("Enter password:\n");
	/*
	 * read in the entire password from user till a newline character is
	 * encountered
	 */
	scanf("%[^\n]s", p_pswd);

	/* check the contents of passwd array*/
	/*printf("%s\n", passwd);*/
	/*compare user input to preset password*/
	result = strcmp(p_pswd, actual);

	/*check if the enter password is correct*/
	if (result == 0)
	{
		printf("Welcome\n");
	}
	else
	{
		printf("Incorrect, Try again Later\n");
	}

	return (0);
}
