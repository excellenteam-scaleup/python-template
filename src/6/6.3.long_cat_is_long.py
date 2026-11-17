import string


def words_length(sentence):
    return [len(word) for word in sentence.split()]


def get_letters():
    lowercase = [chr(code) for code in range(ord('a'), ord('z') + 1)]
    uppercase = [chr(code) for code in range(ord('A'), ord('Z') + 1)]
    return lowercase + uppercase


def count_words(text):
    clean_text = ''.join(char for char in text.lower() if char.isalpha() or char.isspace())
    return {word: len(word) for word in clean_text.split()}


def full_names(first_names, last_names, min_length=0):
    names = [
        f"{first.capitalize()} {last.capitalize()}"
        for first in first_names
        for last in last_names
    ]
    return [name for name in names if len(name) >= min_length]


print(words_length("Toto, I've a feeling we're not in Kansas anymore"))

print(get_letters())

text = """
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat.
"""

expected_result = {'you': 3, 'see': 3, 'wire': 4, 'telegraph': 9, 'is': 2, 'a': 1, 'kind': 4, 'of': 2, 'very': 4, 'long': 4, 'cat': 3, 'pull': 4, 'his': 3, 'tail': 4, 'in': 2, 'new': 3, 'york': 4, 'and': 3, 'head': 4, 'meowing': 7, 'los': 3, 'angeles': 7, 'do': 2, 'understand': 10, 'this': 4, 'radio': 5, 'operates': 8, 'exactly': 7, 'the': 3, 'same': 4, 'way': 3, 'send': 4, 'signals': 7, 'here': 4, 'they': 4, 'receive': 7, 'them': 4, 'there': 5, 'only': 4, 'difference': 10, 'that': 4, 'no': 2}

print(count_words(text) == expected_result)

print(full_names(['avi', 'moshe', 'yaakov'], ['cohen', 'levi', 'mizrahi']))
print(full_names(['avi', 'moshe', 'yaakov'], ['cohen', 'levi', 'mizrahi'], min_length=10))
