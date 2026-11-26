# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        def suma_con_acarreo(l1: ListNode | None, l2: ListNode | None, acr: int) -> ListNode | None:
            if l1 is None and l2 is None:
                return ListNode(1, None) if acr == 1 else None

            if l1 is None:
                suma = l2.val + acr
                if suma >= 10:
                    return ListNode(suma - 10, suma_con_acarreo(l1, l2.next, 1))
                return ListNode(suma, suma_con_acarreo(l1, l2.next, 0))

            if l2 is None:
                suma = l1.val + acr
                if suma >= 10:
                    return ListNode(suma - 10, suma_con_acarreo(l1.next, l2, 1))
                return ListNode(suma, suma_con_acarreo(l1.next, l2, 0))

            suma = l1.val + l2.val + acr
            if suma >= 10:
                return ListNode(suma - 10, suma_con_acarreo(l1.next, l2.next, 1))
            return ListNode(suma, suma_con_acarreo(l1.next, l2.next, 0))

        return suma_con_acarreo(l1, l2, 0)
