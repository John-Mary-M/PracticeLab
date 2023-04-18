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
	char srch[25];
	FILE *Fp;

	Fp = fopen("Student_data.txt", "r");
	if (Fp == NULL)
		return (-1);
	char buf[255];
	while (fgets(buf, sizeof(buf), Fp) != NULL)
	{
		if (strstr(buf, srch) != NULL)/*search for srch in the buf*/
		{
			printf("%s\n", buf);
		}
		i++;
	 
	

	/* check what user would like to do*/
	printf("Welcome!\nTo access student records enter 1.\nTo access teacher
	       records, enter 2\n");
        scanf("%d", &stdt_rec); /*take users choice*/
	if (stdt_rec == 1)
	{
		printf("to enter student press 3: or search existing student\n");
		switch (3)
		default:{
			printf("Enter student to search records\n");
			scanf("%s", srch);
			
	}

}
