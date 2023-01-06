#include "lists.h"

/**
 * is_palindrome - checks if linked list is empty
 * @head: head pointer
 *
 * Return: 1 if empty, 0 if not empty
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;

	if (temp == 0)
		return (1);
	else
		return (0);
}
