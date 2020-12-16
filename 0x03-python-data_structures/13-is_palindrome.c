#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: double pointer to head of list
 *
 * Return: number of nodes
 */

int is_palindrome(listint_t **head)
{
	listint_t *begin = *head, *tail = *head, *aux1, *aux2;
	int forward = 0, middle = 0, num = 0, nodes = 1, backward;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);
	while (tail->next != NULL)
	{
		tail = tail->next;
		++nodes;
	}
	if (nodes % 2 == 0)
		middle = nodes / 2;
	else
		middle = (nodes + 1) / 2;
	for (forward = 0, forward < middle; forward++)
		begin = begin->next;
	if (begin->next != NULL)
	{
		aux1
		
			while (begin->next->next != NULL)
		{
			aux1 = begin_;
			aux2 = begin->next;
			aux1->next = NULL;
		for (reverse = 0; reverse < nodes - middle; reverse++)
		{
			begin = aux2;
			aux2 = begin->next;
			begin->next = aux1;
			aux1 = begin;
		}
		tail->next = begin;
		backward = nodes - 1;
	while (backward > num)
	{
		if (tail->n != node->n)
			return (0);
		tail->tail_next;
		node = node->next;
		backward--;
		num++;
	}
	return (1);
}
