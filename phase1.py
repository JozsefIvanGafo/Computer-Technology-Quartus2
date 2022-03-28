from slist import SList, SNode
import sys

class SList2(SList):
    #method for sum the las N elements
    def sumLastN(self, n):
        #If the list is empty
        if self.isEmpty():
            return 0
        elif n<0:
            return None
        #when n>self._size then n is equal to the size of the list and then we will sum all the elemenst on the next lines of code
        if n > self._size:
            n=self._size
        #In this case, we declare a variable top, whose function is that when iterating, when i is equal or greater than top, then it will add 
        #those elements. So if the length is 10, and I want to add the last 2, when i is greater or equal to 8, it will add the element in position
        #8 and in position 9. 
        sum = 0
        node = self._head
        i=0
        top = self._size - n
        while i< self._size:
            if i >= top:
                sum += node.elem
            node = node.next
            i+=1
        return sum

    #method for inserting a new node in the middle
    def insertMiddle(self,elem):
        #If self is empty
        if self.isEmpty():
            self.addFirst(elem)
        #If the size
        else:
            i=0
            previous=None
            node=self._head
            #If the length of the list is even
            if self._size %2 == 0:
                while i != (len(self)//2):
                    previous = node
                    node = node.next
                    i+=1
            #If the length of the list is odd
            else:
                while i!=(len(self)+1)/2:
                    previous = node
                    node = node.next
                    i+=1
            #Once we get to the middle, we use the previous and the node in the middle, to insert our new node in between.
            newNode = SNode(elem)
            previous.next = newNode
            newNode.next = node
            
    #method for inserting a new node in the middle
    def insertList(self,inputList,start,end):
        if start<0 or start>end or end>=len(self) or ((type(start) or type(end)) != int):
            return None

        #we take the last node of the input list
        last_in_node=inputList._head
        while last_in_node.next!=None:
            last_in_node=last_in_node.next

        #Variable that we will use to iterate on the next conditionals
        i=0
        if start == 0 and end ==0:
            # When start and end = 0, what we do is to remove the first element, and then we say that the next node of the last element in the 
            #input list, is the second one in the first list (self)
            node=self._head.next    
            last_in_node.next = node
            self._head=inputList._head
            
        else:
            node = self._head
            while i < end+1:
                #if i=start-1 it means that we are on the previous node where we will 
                # start to replace the following nodes by the input list
                if i==start-1:
                    #start_node is the node (of the self.list) whose next node will be the first node of the input list
                    start_node=node
                node = node.next
                i+=1
            #end_node is the node whose previous is the last node of the input list
            end_node = node
            last_in_node.next=end_node
            #If start is 0 then we change the head by the head of the input list
            if start==0:
                self._head=inputList._head
            #Else we assign the start node to the head of the input list
            #start_node is the node (of the self.list) whose next node will be the first node of the input list
            else:
                start_node.next=inputList._head

    def reverseK(self,k):
        #we protect in case k is not an integer
        if type(k)!=int:
            return None
        #When k is smaller than 1 We return itself
        if k <=1:
            return self
        #if k>= than the length To reverse the whole list on the main program
        if k >= len(self):
            k=len(self)
        #Else
        node=self._head
        #Variable to say if it is the first iteration
        start=True
        while node!=None:
            i=0
            aux_list = SList()
            start_loop=True
            while i<k and node!=None:
                aux_list.addFirst(node.elem)
                if start_loop:
                    #Here, we say that the variable aux_tail is the head of the auxiliary list which in fact, is the node that is going to be
                    #connected to the next reversed "mini section" of the list. This is executed as much times as "groups" of k elements we can
                    #find in the list.
                    aux_tail=aux_list._head
                    start_loop=False
                node=node.next
                i+=1
            #IF is the first iteration of the entire program we change its head by the aux list to later add the 
            if start:
                self._head=aux_list._head
                #aux tail_prev will be used to link/connect the next reversed segment
                aux_tail_prev = aux_tail
                #we only need to executed once on the program (because is to define the head of the list)
                start=False
            else:
                #Here we link the nodes to the next reversed segment
                aux_tail_prev.next=aux_list._head
                #now the tail of the new reversed segment is the previous that we will use to connect the next reverse segment
                aux_tail_prev=aux_tail
        return self
            
    def maximumPair(self):
        #If the list is empty
        if self.isEmpty():
            return None
            
        if len(self) == 1:
            return self._head.elem
        #We create an external list where later we will sum them
        i=1
        total_list=SList()
        #If the length is even
        if len(self)%2==0:
            #We take the length//2 as a variable
            length_div2=len(self)//2
            even=True
        #If the length is odd
        else:
            #If the length is even we add it 1, because we need to take the next element
            length_div2=(len(self)//2)+1
            even=False
        node=self._head
        #total_node=None
        while node.next!=None:
            if i<=length_div2:
                #We add the elemenst on a list until we get to the middle
                #after reaching the middle we will start adding the next ones on the list 
                #(that is reversed because we will use addFirst)
                #e.g 1->2->3->4->None
                #we add it on the list having 2->1->None and we will add 2+3->2+4->None
                total_list.addFirst(node.elem)
                node = node.next
                #We reached the "half" of the list
                #The total_node is the head of the total_list which is the first half of the initial list but reversed.
                if i==length_div2 and even:
                    total_node=total_list._head
                else:
                    #since its odd we take the next node not to operate with the node in the middle.
                    #e.g 1->2->3->4->5->None, the external list we obtain 3->2->1->None so we need to do the next operations 
                    # 3->2+4->1+5->None but we must avoid the middle one (in this case 3) because we don't need to add anything.
                    total_node=total_list._head.next
                i+=1
            else:
                #Once we have the total_list created with the first half of elements of the inintial list, but reversed, we update the values
                #of the elements in the total list, by adding them to the next elements from the middle of the initial list.
                total_node.elem+=node.elem
                total_node=total_node.next
                node=node.next
        #To sum the last element (that is not included on the while)
        total_node.elem+=node.elem

        #comparison to take the maximum pair
        print(total_list)
        #We take the first element of the list as the maximum pair
        max=total_list._head.elem
        total_node=total_list._head
        #We will iterate on the external total pair to take the max pair
        while total_node!=None:
            #If total.node.elem is bigger than max it means that there is a pair that is bigger than the maximum
            if max<total_node.elem:
                max=total_node.elem
            total_node=total_node.next
        #We return the maximum pair of the list
        return max    