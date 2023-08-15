#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of linked list
 *
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *second_half = NULL;
	int is_palindrome = 1;
	/* Find the middle node of the linked list */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	/* Handle the case when the length of the linked list is odd */
	if (fast != NULL)
	{
		second_half = reverse_list(slow->next);
	}
	else
	{
		second_half = reverse_list(slow);
	}
	/* Compare the first half with the reversed second half */
	while (second_half != NULL)
	{
		if ((*head)->n != second_half->n)
		{
			is_palindrome = 0;
			break;
		}
		*head = (*head)->next;
		second_half = second_half->next;
	}
	/* Restore the original linked list by reversing the second half again */
	if (fast != NULL)
	{
		slow->next = reverse_list(second_half);
	}
	else
	{
		*head = reverse_list(second_half);
	}
	return (is_palindrome);
}

/**
 * reverse_list - reverses a singly linked list
 * @head: pointer to head of linked list
 *
 * Return: pointer to new head of reversed linked list
 */

listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (head != NULL)
	{
		next = head->next;
		head->next = prev;
		prev = head;
		head = next;
	}
	return (prev);
}
