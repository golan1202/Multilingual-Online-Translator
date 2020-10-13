import requests
from bs4 import BeautifulSoup
import sys

args = sys.argv

languages = ['arabic',
             'german',
             'english',
             'spanish',
             'french',
             'hebrew',
             'japanese',
             'dutch',
             'polish',
             'portuguese',
             'romanian',
             'russian',
             'turkish', ]
print('''Hello, you're welcome to the translator. Translator supports: 
1. Arabic
2. German
3. English
4. Spanish
5. French
6. Hebrew
7. Japanese
8. Dutch
9. Polish
10. Portuguese
11. Romanian
12. Russian
13. Turkish'''
      )
language1 = str(args[1])
language2 = str(args[2])
word_query = str(args[3])

headers = {"User-Agent": "Mozilla/5.0"}

if language1 not in languages and language1 != 'all':
    print(f"Sorry, the program doesn't support {language1}")
    exit()
if language2 not in languages and language2 != 'all':
    print(f"Sorry, the program doesn't support {language2}")
    exit()
if language2 == 'all':
    with open(f'{word_query}.txt', 'w+', encoding="utf-8") as f:
        for i in languages:
            if i == language1:
                continue
            url = f"https://context.reverso.net/translation/{language1}-{i}/{word_query}"
            my_request = requests.get(url, headers=headers)
            if my_request.status_code == 404:
                print(f"Sorry, unable to find {word_query}")
                exit()
            if my_request.status_code != 200:
                print("Something wrong with your internet connection")
                exit()
            soup_object = BeautifulSoup(my_request.text, "html.parser")
            sentence_examples = []
            for sentence in soup_object.find(id="examples-content").select(".ltr"):
                sentence_examples.append(sentence.text.strip())
            word_examples = []
            for word in soup_object.find(id='translations-content').select('a'):
                word_examples.append(word.text.strip())
            f.write(f"{i.capitalize()} translations:\n")
            f.write(word_examples[0] + "\n")
            f.write(f"{i.capitalize()} examples:\n")
            f.write("\n\n".join(("\n".join(j for j in sentence_examples[i:i + 2]) for i in range(0, 2, 2))) + "\n")
        f.seek(0)
        print(f.read())

else:
    url = f"https://context.reverso.net/translation/{language1}-{language2}/{word_query}"
    my_request = requests.get(url, headers=headers)
    if my_request.status_code == 404:
        print(f"Sorry, unable to find {word_query}")
        exit()
    if my_request.status_code != 200:
        print("Something wrong with your internet connection")
        exit()
    soup_object = BeautifulSoup(my_request.text, "html.parser")
    sentence_examples = []
    for sentence in soup_object.find(id="examples-content").select(".ltr"):
        sentence_examples.append(sentence.text.strip())
    word_examples = []
    for word in soup_object.find(id='translations-content').select('a'):
        word_examples.append(word.text.strip())
    print(f"{language2.capitalize()} translations:")
    print(*word_examples[:5], sep='\n')
    print(f"{language2.capitalize()} examples:")
    print("\n\n".join(("\n".join(j for j in sentence_examples[i:i + 2]) for i in range(0, 10, 2))))