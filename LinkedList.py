class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    # Constructor of a linked list ( a differentiation is that this is a method and not a function )
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1 

    # print a list 
    def print_list(self):

        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Append an item from the end of the list 
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1 

        return True

    # this is to pop the item at the end of the list 
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head

        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -=1 

        if self.length == 0:
            self.head = None
            self.tail = None
        return True  

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1 
        return True


    # pop first item of the list 

    def pop_first(self):

        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None
        return temp

    # def get 
    def get(self, index):

        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp 


    # set value of th elinked list 
    def set(self, index, value):

        temp = self.get(index)

        if temp:
            temp.value = value
            return True
        return False 

    def insert(self, index, value):

        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        new_node = Node(value)

        temp = self.get(index -1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1 
        return True


    def remove(self, index, value):
        if index < 0 or index >= self.length:
            return None

        if self.index == 0:
            return self.pop_first()

        if self.index == self.length -1:
            return self.pop()

        prev = self.get(index - 1)
        temp = prev.next 
        prev.next = temp.next 
        temp.next = None
        self.length -= 1 
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp 
            temp = after

# Find middle node

    def find_midde(self):
        fast = self.head
        slow = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

# find if has a loop 
    def has_loop(self):
        fast = self.head
        slow = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

# remove duplicates
    def remove_duplicates(self):
        current = self.head

        while current is not None:
            runner = current 

            while runner.next is not None:
                if runner.next.value == current.value:
                    runner.next = runner.next.next 

                    self.length -=1
                else:
                    runner = runner.next

            current = current.next

