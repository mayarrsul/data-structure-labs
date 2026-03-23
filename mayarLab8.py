print('mayar')



'''
mayar alhassani
446002675
group 5    
'''

def main():
    print ('mayar')
    mer = BST()
    students = {50: 88.5, 30: 91.0, 70: 79.5, 
                20: 85.0, 40: 90.0, 60: 95.0, 80: 77.5}

    for id, grade in students.items() :
        mer.insert(id , grade)

    print('the bst items in order :')
    mer.inorder(mer.root)
    print('\n search for 60 ', mer.search(60))
    print('search for 25', mer.search(25))

    mer.delete(30)
    mer.delete(70)
    print('\n the bst items in order :')
    mer.inorder(mer.root)





class Node:
    def __init__(self, id, grade):
        self.id = id
        self.grade = grade
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self, id, grade):
        if self.root is None:
            self.root = Node(id,grade)
            return
        
        current = self.root
        while True:
            if id < current.id:

                if current.left is None:
                    current.left = Node(id , grade) 
                    return
                else:
                    current = current.left 

            elif id > current.id:

                if current.right is None:
                    current.right = Node(id , grade) 
                    return
                else:
                    current = current.right 
            else:

                return




    def search(self, id):

        current = self.root
        while current is not None:
            if id == current.id:
                return True 
            elif id < current.id:
                current = current.left 
            else:
                current = current.right 
        return False




    def delete(self, id):
        self.root = self._delete_recursive(self.root, id)

    def _delete_recursive(self, node, id):

        if node is None:
            return None 
        if id < node.id:
            node.left = self._delete_recursive(node.left,id)
        elif id > node.id:
            node.right = self._delete_recursive(node.right, id)
        else:

            if node.left is None and node.right is None:
                return None


            if node.left is None:
                return node.right # replace node by its right child
            if node.right is None:
                return node.left # replace node by its left child

            successor = self._find_min(node.right)
            node.id = successor.id # copy value to current node
            node.right = self._delete_recursive(node.right, successor.id)

        return node
    
    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    

    def inorder(self , node):
        if not node:
            return

        self.inorder(node.left)
        print((node.id, node.grade))   
        self.inorder(node.right)

main()
