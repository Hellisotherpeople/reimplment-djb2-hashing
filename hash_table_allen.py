

class hash_table:

    def __init__(self, size):
        self.hash_array = [None] * size
        self.size = size

    def display(self):
        print(self.hash_array)

    def djb2(self, to_hash):
        cur_hash = 5280

        for char in to_hash.strip():
            cur_hash = cur_hash * 33 + ord(char)
        hash_loc = cur_hash % self.size
        print("string hashed to " + str(hash_loc))
        return hash_loc

        #print("string hashed to " + str(cur_hash % len_of_table))

    def add(self, entry):
        hash_loc = self.djb2(entry)
        if self.hash_array[hash_loc]:
            print("Collision at: " + str(hash_loc) + "\n" + "Ejecting current output: " +
                  self.hash_array[hash_loc] + " and replacing with: " + entry)
        self.hash_array[hash_loc] = entry


len_of_table = 20
the_table = hash_table(len_of_table)

the_table.add("hello!")
the_table.add("smello")
the_table.add("cello")
the_table.add("cello")
the_table.display()
