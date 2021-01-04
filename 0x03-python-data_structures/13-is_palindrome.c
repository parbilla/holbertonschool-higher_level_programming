#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: double pointer to head of list
 *
 * Return: number of nodes
 */

int is_palindrome(listint_t **head)
{
	listint_t *beg = *head, *nod = *head, *tail = *head, *rev, *aux1, *aux2;
	int forward = 0, middle = 0, num = 0, nodes = 1, back;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);
	while (tail->next != NULL)
	{
		tail = tail->next;
		++nodes;
	}
	rev = tail;
	if (nodes % 2 == 0)
		middle = nodes / 2;
	else
		middle = (nodes + 1) / 2;
	for (forward = 0; forward < middle; forward++)
		beg = beg->next;
	if (beg->next != NULL)
	{
		aux1 = beg;
		aux2 = beg->next;
		while (aux2->next != NULL)
		{
			beg = aux2;
			aux2 = beg->next;
			beg->next = aux1;
			aux1 = beg;
		}
		tail->next = beg;
		beg = beg->next;
	}
	else
		tail->next = *head;
	for (num = 0; num < nodes / 2; num++)
	{
		if (tail->n != nod->n)
			return (0);
		tail = tail->next;
		nod = nod->next;
	}
	aux1 = rev;
	aux2 = rev->next;
	aux1->next = NULL;
	for (back = 0; back < num - 1; back++)
	{
		rev = aux2;
		aux2 = rev->next;
		rev->next = aux1;
		aux1 = rev;
	}
	return (1);
}
