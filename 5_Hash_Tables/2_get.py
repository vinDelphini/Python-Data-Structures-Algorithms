class HashTable:

    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 27) % (len(self.data_map))
        return my_hash

    def print_table(self):
        for i, key in enumerate(self.data_map):
            print(i, " : ", key)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for pair in self.data_map[index]:
                if pair[0] == key:
                    return pair[1]
        return None


my_hash_table = HashTable()
my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

my_hash_table.print_table()
print(my_hash_table.get_item('lumber'))
