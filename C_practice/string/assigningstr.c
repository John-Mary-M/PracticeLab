#include <stdio.h>
#include <string.h>

/**
 * main - checking string contents at different points
 * working with strcpy and strcat functions to manipulate
 * string arrays
 *
 * return: 0 on success.
 */
int main(void)
{
	char protagonist[20] = "got";

	printf("orignal content of protagonist: %s\n", protagonist);

	/*
	 * we cant assign to such an array like this
	 * protagonist = "Gandalf"
	 * simply because protagonist itself is a pointer to the
	 * first element in the array even if its not yet initialized.
	 * we cant change that.
	 * BUT we can do this
	 */
	strcpy(protagonist, "Gandalf");   /*
					   * this will replace the contents of
					   * the array with "Gandalf"
					   */
	printf("Contents of protagonist: %s\n", protagonist);
	/*
	 * what if we dont want to replace contents of protagonist
	 * but add to it?
	 */
	strcat (protagonist, " something new");
	printf("updated contents of protagonist: %s\n", protagonist);

	return (0);
}
