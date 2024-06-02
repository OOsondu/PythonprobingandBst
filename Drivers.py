class Node:
    def __init__(self, word):
        self.word = word
        self.frequency = 1
        self.left = None
        self.right = None

class BSTWordFrequency:
    def __init__(self):
        self.root = None

    def insert(self, root, word):
        if root is None:
            return Node(word)

        if word < root.word:
            root.left = self.insert(root.left, word)
        elif word > root.word:
            root.right = self.insert(root.right, word)
        else:
            root.frequency += 1

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(f"{root.word}, {root.frequency}; ", end='')
            self.inorder(root.right)

    def delete(self, root, word):
        if root is None:
            print("The word is not found.")
            return root

        if word < root.word:
            root.left = self.delete(root.left, word)
        elif word > root.word:
            root.right = self.delete(root.right, word)
        else:
            if root.frequency > 1:
                root.frequency -= 1
                print(f"The frequency of {root.word} is now {root.frequency}.")
                return root

            print("The word is removed from the BST.")
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            root.word = self.min_value(root.right)
            root.right = self.delete(root.right, root.word)

        return root

    def min_value(self, root):
        min_val = root.word
        while root.left:
            min_val = root.left.word
            root = root.left
        return min_val

def main():
    bst = BSTWordFrequency()
    sentence = input("Enter a sentence: ")
    words = sentence.split()

    for word in words:
        cleaned_word = ''.join(filter(str.isalpha, word)).lower()
        if cleaned_word:
            bst.root = bst.insert(bst.root, cleaned_word)

    print("The words and their frequencies in the BST: ", end='')
    bst.inorder(bst.root)
    print()

    delete_word = input("Enter the word to be deleted: ").lower()
    cleaned_delete_word = ''.join(filter(str.isalpha, delete_word))
    bst.root = bst.delete(bst.root, cleaned_delete_word)

if __name__ == "__main__":
    main()
