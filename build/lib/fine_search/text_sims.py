import threading
import string


class TextSimilarity:

    def __init__(self, text, search):
        super().__init__()
        self.text = text
        self.search = search
        self.text_hash = {}
        self.search_hash = {}
        self.threads = []
        self.alphabets = self.init_alphabets()

    def init_alphabets(self):
        alphabets = {}
        for char in string.ascii_lowercase:
            alphabets[char] = char
        return alphabets

    def word_cleaning(self, word):
        new_word = []
        for char in word.lower():
            if char in self.alphabets:
                new_word.append(char)
        return ''.join(new_word)

    def str_to_hash(self, string, hash_):
        word_list = string.split(" ")
        for word in word_list:
            if not self.word_cleaning(word) in hash_:
                hash_[self.word_cleaning(word)] = 1
    
    def text_to_hash(self):
        self.str_to_hash(self.text, self.text_hash)
        
    def search_to_hash(self):
        self.str_to_hash(self.search, self.search_hash)

    def split_to_hash(self):
        thread1 = threading.Thread(target=self.search_to_hash)
        self.threads.append(thread1)
        thread1.start()
        thread2 = threading.Thread(target=self.text_to_hash)
        self.threads.append(thread2)
        thread2.start()

    def evaluate(self):
        self.split_to_hash()
        for thread in self.threads:
            thread.join()
        word_count = 0
        for word in self.search_hash:
            if word in self.text_hash:
                word_count += 1
        return word_count / len(self.text_hash)