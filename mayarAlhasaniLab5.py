print('mayar')

def main():
    print('mayar')
    mer=DoublyLinkedList()
    mer.append('shap Of You')
    mer.append('blinding linghts')
    mer.append('perfect')
    mer.append('havana')
    mer.display_forward()
    mer.display_backward()
    mer.delete('perfect')
    mer.display_forward()



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
        self.prev = None 

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            ##
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node


    def display_forward(self):
        current = self.head
        print("Forward:")
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        

    def display_backward(self):
        current = self.tail
        print("Backward:")
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        

    def delete(self, value):
        current = self.head
        while current:
            if current.data == value:

                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None

                elif current.next is None:
                    self.tail = current.prev
                    self.tail.next = None

                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                print(f"Deleted: {value}")
                return
            current = current.next
            


main()





