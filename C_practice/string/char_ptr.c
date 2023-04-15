#include <stdio.h>
#include <string.h>

/**
 * main - more string operations
 *
 * Return: 0 on success.
 */
int main(void)
{
	char *hero = "Dumbledore";
	int res;

	printf("address pointed to by hero: %p\n", hero);
	printf("the contents in the hero address: %s\n", hero);

	/* assigning new value in memory pointed to by hero*/
	hero = "sirius";
	printf("contents of hero again: %s\n", hero);
	res = puts(hero);  /* prototype of puts is int puts(char *s); */
	printf("res: %d\n", res);  /* res is the length of hero plus a newline
				    * character
				    * if puts() fails then it returns -1
				    */

	/*
	 * whenever we use the strcpy we need to be certain there is enough
	 * space
	 */
	/*strcpy(hero, "abcdef ghijk lmno pqrst uvwx yz");*/
	/*printf("new contents if space is enough: %s\n", hero);*/
	/* this causes a seg fault because the program runs out memory*/


	return (0);
}
