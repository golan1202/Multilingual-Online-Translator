# Multilingual-Online-Translator
Everyone’s familiar with online translators. They giving us a handy way to translate on the go.
In this project, you’re about to write an app that translates the words you type and gives you many usage examples based on the context.

## Work on project. Stage 1/7: Repeater

### Description
Your very first step is writing a program that begins with an invitation message for choosing the translation direction. 
It then takes the input from your keyboard as an argument and repeats the same process for the word you want to translate.

Here's what you’re going to do:

Add the ability to choose the translation direction between two languages (for instance, English and French)
Type the word you want to translate
First, you will get a call from the program to choose the mode. 
Next, you should be asked to enter the word you want to translate. After that, the program should output the information it gathered.

## Work on project. Stage 2/7: Over the internet

### Description
Here you will connect your app to an online web service to get the translation data from it.
To establish the connection, you have to form the request, send it to the website, and check the HTTP status of the response. 
If your status code is ```200```, then you are good to proceed!

### Create the request
Now, go to [ReversoContext](https://context.reverso.net/translation/) and type any word you want to translate. 
After receiving the result, pay attention to the address bar of your browser. You will see the URL, for example:

[https://context.reverso.net/translation/english-french/cheese](https://context.reverso.net/translation/english-french/cheese)

Here you see the language-translation pair «English-French», which represents the direction of translation, meaning that the translation is from English to French and not the other way around. 
After the last backslash, you can see the word being translated.

Your goal is to make your program act as if it visits the website for you. 
To make it happen, tell your program to generate the correct URL with the word you type, 
determine the translation direction as you chose it at the previous stage, and send the URL to the website using the requests package.

### Select text data
Your program already knows how to send a request. What it still doesn’t know is how to handle incoming data to get the translation examples. This is possible with the BeautifulSoup package.

Have you already tried ReversoContext? It gives you two types of text data:

- Single translated words
- Sentences with usage examples

## Work on project. Stage 3/7: Translations

### Description
To get readable results, you need to format all the data you get from the web.
Good thing that Python is a rich programming language with a powerful text formatting out of the box!

Use Python’s built-in text formatting to:

- Remove all the quotation marks and commas
- Place each word and example sentence in a new line
- You might also want to cut the results to 5 words and 5 example sentences to keep it compact

## Work on project. Stage 4/7: All of them

### Description
Good! You now have a basic translation app that works well. Wouldn’t it be great though to expand it and include all available languages? This will add the ability to translate from/to any language in the list.

The maximum number of languages our translator can support is 13. They are:

- Arabic
- German
- English
- Spanish
- French
- Hebrew
- Japanese
- Dutch
- Polish
- Portuguese
- Romanian
- Russian
- Turkish
They should be enumerated in the program. A great idea is to present them with relevant numbers, so that the user can choose the first as the original language and the second as a translation.

## Work on project. Stage 5/7: Simultaneous translation

### Description
You’ve done a great job! There are just a couple of stages left. Your translation app is flexible enough to be appreciated by many people worldwide, so let's make it even better.

This stage is meant to teach you how to work with files.

First, you’re going to add another cool feature to the project. Think how great it would be if you could translate to all the languages at once and save it for later!

Here's what you’ll do:

- Add the ability to translate to all languages at once
- Save results to the file on your computer
- Output the results to the terminal as well

To make the first feature possible, there’s a way to expand the existing language list with zero, which will mean the translation to all languages listed below.

Since you will get a long output with all these translations coming one after another, it’s better to save it to the file on your computer so that you can read it later (but don't forget to print results anyway).
You can name this file as the word in the input.
Tip: just place the listed languages into the URL depending on the user’s choice!
Tip-2: Try to convert the input to lower case: it may cause an error if the user's input is in upper case or mixed. You can do it with Python's built-in functionality.

## Work on project. Stage 6/7: Faster translation

### Description
There’s a faster way to translate a word without being asked by the program every time. To make your program more convenient, you can use command-line arguments.
They make it possible to provide a program with all the data it needs using a simple command.

At this stage, you should add command-line argument handling in your code. This is possible via Python sys package.

You'll see some significant changes in the usability of the app!

## Work on project. Stage 7/7: Unexpected

### Description
Okay, it seems like your program translates as expected. However, there’s a problem you should always keep in mind: something can break your program.

Up to this stage, you were thinking about things that should be in your code. But what if things go wrong? For example, you gave your program to someone who’s not familiar with the concept behind it. What if they try to translate to or from languages different from those you have in your code, or even start typing jabberwocky? That can break your program.

All these situations are called exceptions because you didn’t expect them to happen, and now you have to handle them.
