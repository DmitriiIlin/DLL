"""
Реализация класса Doubled Linked List
"""
class Node:

    def __init__(self, v):
        #Инициализация класса Node
        self.value = v
        self.prev=None
        self.next = None
    
class LinkedList2:  

    def __init__(self):
        #Инициализация класса Doubled Linked List
        self.head = None
        self.tail = None
        
    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            self.next=None
            self.prev=None
        else:
            self.tail.next = item
            item.prev=self.tail
        self.tail = item
        
    def print_all_nodes(self):
        # Метод класса DLL, позволяющий вывести э-ты DLL 
        node=self.head
        while node!=None:
            print(node.value,node.prev,node.next,'вывод print all nodes')
            node=node.next

    def find(self, val):
        # Метод класса LL, реализующий поиск по значению
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None
    
    def find_all(self,val):
        #Поиск элементов и возвращение найденных значений
        element_result=[]
        i=0
        node=self.head
        while node is not None:
            if node.value==val:
                element_result.append(node)  
            node=node.next  
            i+=1
        return element_result

    def delete(self,val,all=False):
        # Метод удаления значения из DLL, при all=False удаляет 1 элемент, при all=True удаляет все искомые элементы
        node = self.head
        while node is not None:
            if (self.head == self.tail) and (self.head.value == self.tail.value == val):
                node=None
                self.head=None
                self.tail=None
                break
            if (node.value==self.head.value) and (node.value==val):
                new_head=node.next
                self.head=new_head
                if all==False:
                    break
            elif (node.value == val) and (self.tail!=node):
                node_next=node.next
                node_pr.next=node.next
                node_next.prev=node_pr
                if all==False:
                    break
            elif (node.value==self.tail.value) and (node.value==val):
                self.tail=node_pr
                node_pr.next=None
  #              self.next=node_pr.next
                if all==False:
                    break
            if node.value!=val:
                node_pr=node
            node=node.next

    def clean(self):
        # Удаление всех элементов DLL
        node=self.head
        while node is not None:
            node.value=None
            node_pr=node
            node=node.next
            node_pr.next=None
            node_pr.prev=None
        self.head=None
        self.tail=None

    def len(self):
        # Метод класса DLL, определяющий кол-во э-в класса Node в DLL (длина DLL)
        node=self.head
        l=0
        while node is not None:
            l+=1
            node=node.next
        return l 

    def insert(self,afterNode,newNode):
        # Метод класса DLL позволяющий вставить э-т newNode в DLL
        if  (self.head==None) and (afterNode==None):
            newNode.next=None
            self.head=newNode
            self.tail=newNode
        elif (self.head!=None) and (afterNode==self.tail):
            self.tail=newNode
            afterNode.next=newNode
            newNode.next=None
            newNode.prev=afterNode
            self.tail=newNode
        elif (self.head!=None) and (afterNode!=self.tail):
            newNode.next=afterNode.next
            next_Node=Node(newNode.next)
            newNode.prev=afterNode
            next_Node.prev=newNode
            afterNode.next=newNode 
            
        else:
            return None   
    
    def add_in_head(self,newNode):
        #Метод добавления э-та Node в начало DLL
        if (self.head is None) and (self.tail is None):
            self.head=newNode
            self.next=None
            self.prev=None
            self.tail=newNode
        else:
            next_node=self.head
            self.head = newNode
            newNode.next=next_node
            newNode.prev=None
            next_node.prev=newNode
        


    
def add_linked_lists(list_1,list_2):
# Функция складывающая значения двух LL при условии равенства длин и равенства содержания знач.==int
    if list_1.len()==list_2.len():
        sum_linked_list=LinkedList2()
        sum_node=None
        node_1=list_1.head
        node_2=list_2.head
        val=None
        for i in range(0,list_1.len()):
            if (int(node_1.value)==node_1.value) and (int(node_2.value)==node_2.value):
                val=node_1.value+node_2.value
                sum_node=Node(val)
                sum_linked_list.add_in_tail(sum_node)
                node_1=node_1.next
                node_2=node_2.next
        return sum_linked_list     
    else:
        return None


