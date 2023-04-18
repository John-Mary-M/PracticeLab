#ifndef _main_h_
#define _main_h_

/**
 * struct student - type to store student details.
 * @name: stores students name.
 * @email: stores email.
 * @phone: srores phone number.
 * @age: stores age.
 * @address: stores address.
 * @nextOfKin: stores student's next of kin.
 * @emergencyContact: stores emergency contact.
 */

struct student
{
	char *name;
	char *email;
	int phone;
	int age;
	char *address;
	char *nextOfKin;
	int emergencyContact;
};
void init_dog(struct dog *d, char *name, float age, char *owner);
#endif /* MAIN_H */
