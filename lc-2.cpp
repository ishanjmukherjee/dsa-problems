/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* cur1 = l1; // to iterate through l1
        ListNode* cur2 = l2; // to iterate through l2
        ListNode* ans = new ListNode; // will store each new node of the final ans
        ListNode* final_ans = ans; // will be returned
        bool carry = false;
        int cur_sum = 0;
        while (cur1 != nullptr || cur2 != nullptr || carry)
        {
            cur_sum = 0;
            // add a node from either list only if the node isn't nullptr
            if (cur1 != nullptr)
                cur_sum += cur1->val;
            if (cur2 != nullptr)
                cur_sum += cur2->val;
            // cur_sum = cur_sum + {1 (if carry is true) or 0 (if carry is false)} 
            cur_sum = cur_sum + carry;
            
            // create a new node 
            // if new node isn't created here, a more operation-expensive 
            // alternative at bottom of this loop will need to be employed
            ans->next = new ListNode;
            ans = ans->next;
            ans->val = cur_sum % 10;
            
            // to carry in next addition if sum / 10 > 0
            carry = cur_sum > 9;
            
            if (cur1 != nullptr)
            {
                cur1 = cur1->next;
            }
            if (cur2 != nullptr)
            {
                cur2 = cur2->next;
            }

            // operation-expensive alternative to creating a new node at time of answer node insertion
            // if (cur1 != nullptr || cur2 != nullptr || carry)
            // {
            //     ans->next = new ListNode;
            //     ans = ans->next;
            // }
        }
        // since first node of final_ans is empty
        return final_ans->next;
    }
};
