class HashTable:
    def __init__(self, size):
        self.tabel = [None] * size

    def store(self, string):
        self.tabel[ self.hash_function(string) ] = string

    def lookup(self, string):
        hash_value = self.hash_function(string)  # index
        value = self.tabel[hash_value]
        if not value:
            return -1
        return hash_value

    def hash_function(self, string):
        return ord(string[0])*10 + ord(string[1])

if __name__ == "__main__":
    h = HashTable(5000)
    h.store("Ania")
    h.store("Leszek")
    h.store("Radek")

    print(h.lookup("Radek"))
    print(h.lookup("Paweł"))

