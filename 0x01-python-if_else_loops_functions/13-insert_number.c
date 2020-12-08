#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: list to check
 *
 * Return: 0 (no cycle)
 */

listint_t *insert_node(listint_t **head, int number)
{
	/* pointers to linked list, one moves one place, two moves two */
	listint_t *insert, *temp;

	temp = *head;
	insert = malloc(sizeof(listint_t));
	if (insert == NULL)
		return (NULL);

	insert->n = number;
	insert->next = NULL;

	if (*head == NULL)
		*head = insert;
	else
	{
		if (insert->n < temp->n)
		{
			insert->next = *head;
			*head = insert;
		}
		else
		{
			while (temp->next != NULL)
			{
				insert->next = temp->next;
				temp->next = insert;
				temp = insert-next:




			return (1);
	}
	return (0);
}
