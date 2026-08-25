import re

sentence = "Ali bought 3 books, 12 Pens and 5 notebooks in 2023"

def find_num(text):
    """ فقط اعداد را پیدا کرده و تعداد انها را  برمیگرداند"""
    pattern = r"\d+"
    find = re.findall(pattern , text)
    return f"Find {len(find)} number in this text"


def find_upper_word(text):
    """ لیست کلماتی که با حروف بزرگ شروع میشن رو میده و همچنین تعداد اونهارو"""
    pattern = r"\b[A-Z][A-Za-z]*\b"
    find = re.findall(pattern , text)
    return f"there are {find}  word that are upper and it's len is : {len(find)}"


print(find_num(sentence))
print(find_upper_word(sentence))



