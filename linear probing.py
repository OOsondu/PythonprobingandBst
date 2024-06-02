class LinearProbingHashTable:
    HASH_TABLE_SIZE = 11

    def __init__(self):
        self.hash_table = [0] * self.HASH_TABLE_SIZE

    def hash_function(self, key):
        return ((3 * key) + 5) % self.HASH_TABLE_SIZE

    def insert(self, key):
        index = self.hash_function(key)
        while self.hash_table[index] != 0:
            index = (index + 1) % self.HASH_TABLE_SIZE
        self.hash_table[index] = key

    def print_hash_table(self):
        print("\nHash Table:")
        for i in range(self.HASH_TABLE_SIZE):
            print(f"Index {i}: {self.hash_table[i]}")

def main():
    hash_table = LinearProbingHashTable()
    
    while True:
        key = int(input("\nEnter an integer key to insert into the hash table: "))
        hash_table.insert(key)
        hash_table.print_hash_table()

        choice = input("\nDo you want to continue? (y/n): ")
        if choice.lower() != 'y':
            break

    print("Program terminated.")

if __name__ == "__main__":
    main()
