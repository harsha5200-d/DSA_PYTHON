class Node:

    def __init__(self,data):

        self.data = data
        self.next = None

class LinkedLists:

    def CreateNode(self,arr):

        if not arr:
            return None
        
        head = Node(arr[0])
        temp = head

        for i in range(1,len(arr)):
            temp.next = Node(arr[i])

            temp = temp.next

        return head

    def partition(self,head,x):

        dummy1 = Node(0)
        dummy2 = Node(0)

        tail1 = dummy1
        tail2 = dummy2

        temp = head
        while temp:

            if(temp.data < x):
                tail1.next = Node(temp.data)
                tail1= tail1.next
            else:
                tail2.next = Node(temp.data)
                tail2 = tail2.next
        
            temp = temp.next
        
        tail1.next = dummy2.next

        return dummy1.next

    def Display(self,head):

        if not head:
            return 
        
        temp = head
        while temp:

            print(temp.data, end=" ")
            temp = temp.next
        
        print()


n = int(input("enter the number of elements in the lists "))
arr = list(map(int,input().split()))[:n]

LL = LinkedLists()

head = LL.CreateNode(arr)

x = int(input("enter the partition number"))


res = LL.partition(head,x)
LL.Display(res)



            