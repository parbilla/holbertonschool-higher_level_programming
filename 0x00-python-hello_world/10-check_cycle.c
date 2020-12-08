#include "lists.h"

/**
* check_cycle - Checks if a singly linked list has a cycle in it.
* @list: list to check
*
* Return: 0 (no cycle)
*/

int check_cycle(listint_t *list)
{
	/* pointers to linked list, one moves one place, two moves two */
	listint_t *one, *two;

	/* point pointers to head*/
	one = two = list;

	/* move pointers */
	while (one != NULL && two != NULL && two->next != NULL)
	{
		two = two->next->next;
		one = one->next;
		/* if there is a cycle, in sometime two will be equal to one*/
		if (two == one)
			return (1);
	}
	return (0);
}
