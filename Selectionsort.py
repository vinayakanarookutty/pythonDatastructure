class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:        
        def __init__(self):
            self.head=None
        def append(self,data):
               new_node= Node(data) 
               if not self.head:
                   self.head=new_node
               last_node=self.head
               while last_node.next:
                   last_node=last_node.next
               last_node=new_node    
        def display(self):
            current=self.head
            while current:
                print(current.data,end="")
                current=current.next          
            print()   
             
hi=LinkedList()
hi.append(7)      
hi.append(89)    
hi.append(67)     
hi.display()     