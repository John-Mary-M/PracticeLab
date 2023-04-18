#include "main.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * main - asks if you want to accsess student or teacher data and grants access
 *
 * Return: always 0.
 */
int main(void)
{
	int stdt_rec;

	/* check what user would like to do*/
	printf("Welcome!\nTo access student records enter 1.\nTo access teacher
	       records, enter 2\n");
        scanf("%d", &stdt_rec); /*take users choice*/
	if (stdt_rec == 1)
	{
		

}
