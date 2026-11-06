from typing import List

def count_unique_words(words: List[str]) -> int:
    setting = set(words)
    my_list = list(setting)
    count = 0
    for i in my_list:
        count = count+1 
    return count
    if words == null:
        return 0

# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
