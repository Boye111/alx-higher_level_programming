#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: The singly linked list to check
 * Return: 1 if has a cycle in it or 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *r = list, *p = list;
	int found = 0;

	while ((r && p) && p->next)
	{
		r = r->next;
		if (p->next || p->next->next)
			p = p->next->next;
		else
			break;
		if (r == p)
		{
			found = 1;
			break;
		}
	}
	return (found);
}
