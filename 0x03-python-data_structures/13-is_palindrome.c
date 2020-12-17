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
	listint_t *begin = *head, *node = *head, *tail = *head, *aux1, *aux2;
	int forward = 0, middle = 0, num = 0, nodes = 1;

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
	for (forward = 0; forward < middle; forward++)
		begin = begin->next;
	if (begin->next != NULL)
	{
		aux1 = begin;
		aux2 = begin->next;
		while (aux2->next != NULL)
		{
			begin = aux2;
			aux2 = begin->next;
			begin->next = aux1;
			aux1 = begin;
		}
		printf("salgo del while\n");
		tail->next = begin;
		printf("cambio el rumbo\n");
	}
	else
		tail->next = *head;
	printf("tail to head\n");
	for (num = 0; num < nodes / 2; num++)
	{
		printf("num = %i\n", num);
		if (tail->n != node->n)
			return (0);
		tail = tail->next;
		node = node->next;
	}
	return (1);
}
