#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: a pointer
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *copy = list, *copytemp = list;

	while(copytemp != NULL && copy->next != NULL && copy->next->next != NULL)
	{
		copy = copy->next->next;
		copytemp = copytemp->next;

		if (copy == copytemp)
				return (1);
	}
	return (0);
}