#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* main - gets input from user and prints it in reverse
 *
 * Return: 0 on success.
 */
int main(void)
{
	char string[];
	int i, j;

	j = strlen(string);
	gets(string);

	printf("%s\n", strrev(string));
	return (0);
}
