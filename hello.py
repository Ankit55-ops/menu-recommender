import random
with open("words_dictionary.txt","r") as file:
    words = [line.strip() for line in file if line.strip()]
    num=int(input("Enter number of words: "))
    if num > len(words):
        print(f"Sorry, you have only {len(words)} words.")
    else:
           random_word=random.sample(words,num)
print(random_word)


