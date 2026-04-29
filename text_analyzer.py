import os
from colorama import Fore, Back, Style, init


init(autoreset=True)

def main():
    flag = True
    user_content=""

    while flag:
        user_content = input("Please enter your content[File/Text/List] or enter -1 to exit: ")
        if user_content == "-1":
            flag = False
        if user_content == "":
            print(Fore.BLUE+"Please enter a valid content !!")
        if user_content !="" and user_content != "-1":
            print("=================================")
            neg_word, pos_words = check_the_content(user_content)
            print(Fore.RED + f"The negative word is {neg_word}")
            print(Fore.GREEN + f"The positive word is {pos_words}")
            print("______________________")
            the_content_state(pos_words,neg_word)
            print("=================================")

def clean_word(word):
    word = word.lower()
    return word

def check_the_content(content):
    negative_words = 0
    positive_words = 0
    content = os.path.normpath(content)
    result =""
    if isinstance(content, str) and os.path.isfile(content):
        with open(content, 'r') as f:
            content = f.read().splitlines() #convert each line as an element in a list
            for sen in content:
                # print(sen)
                for word in sen.split(" "): #to take each word separately not each letter
                    word = clean_word(word)
                    result= analyze_content(word)
                    if result == -1:
                        negative_words+=1
                    elif result == 1:
                        positive_words+=1
    elif isinstance(content, str):
        for word in content.split(" "):  # to take each word separately not each letter
            word = clean_word(word)
            result=analyze_content(word)
            if result == -1:
                negative_words += 1
            elif result == 1:
                positive_words += 1

    return negative_words, positive_words

def analyze_content(text):

    positive =["happy","better","good","nice","beauty","successful","pretty","excited","perfect","fantastic","love","like","adorable", "inspiring", "easy", "cheerful", "cute", "friendly", "grateful","funny", "glad", "great", "honest", "kind", "lucky", "proud", "safe", "smart", "strong", "sweet","best","successfully","amazing","enjoyed","awesome","wonderful","fast","brave","helpful","advantage","benefit","kind","solved","brilliant","lovely","easily","peaceful","hope"]

    negative =["bad", "worst", "hate", "sad", "angry", "terrible", "awful",
    "disgusting", "boring", "difficult", "hard", "ugly", "pain","fail", "failed", "failure", "scary", "wrong", "poor", "gross","annoying", "broken", "cheap", "cruel", "dirty", "evil", "guilty","lonely", "nasty", "negative", "sick", "stupid", "weak", "worry","dislike","destroyed","upset","errors","messy","disappointed","dangerous","danger","lost","lose","rude","noisy","stupid","weak","issue"]
    if text in positive:
        return 1
    elif text in negative:
        return -1
    return 0

def the_content_state(pos,neg):
    if pos > neg:
        print(Back.GREEN+Fore.BLACK+"AI result: Positive")

    elif neg > pos:
        print(Back.RED+Fore.BLACK+"AI result: Negative")
    else:
        print(Back.WHITE+Fore.BLACK+"AI result: Neutral")


main()

