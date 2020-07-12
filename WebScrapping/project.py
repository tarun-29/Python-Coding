import requests
from bs4 import BeautifulSoup
from csv import writer
from random import choice

baseurl = "https://www.quotes.toscrape.com"

def scarpeQuote()
    all_quotes = []
    url = "/page/1
    while url :
        res = requests.get(f"{baseurl}{url}")
        print(f"Now Scrapping {baseurl}{url}...")
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all(class_="quote")

        for quote in quotes:
            all_quotes.append({
                "text":quote.find(class_="text").get_text(),
                "author":quote.find(class_="author").get_text(),
                "bio-link":quote.find("a")["href"]
            })

        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None

    return all_quotes

def startGame(quotes):
    quote = choice(quotes)
    remaining_guesses = 4
    print("Here is a quote: ")
    print(quote["text"])
    guess = ""

    while guess.lower() != quote["author"].lower() and remaining_guesses>0:
        guess = input(f"Who said this quote ? guesses remaining : {remaining_guesses}")
        if guess.lower() == quote["author"].lower():
            print("You got it right")
        remaining_guesses -= 1
        if remaining_guesses==3 :
            res =  requests.get(f"{baseurl}{quote['bio-link']}")
            soup = BeautifulSoup(res.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Here is the hint the author was born on {birth_date} in {birth_place}")

        elif remaining_guesses == 2:
            print(f"Here is a hint: The author first name starts with: {quote['author'][0]}")

        elif remaining_guesses == 1:
            last_initial = quote['author'].split(" ")[1]
            print(f"Here is the hint: The author's Last name starts with : {last_initial}")
        else :
            print(f"Sorry you ran out of guesses. The answer was {quote['author']}")

    again = ""
    while again.lower() not in ('y', 'yes', 'n', 'no') :
        again = input("Would you like to play again (y/n)")

    if(again.lower() in ('y', 'yes') ) :
        return startGame()
    else:
        print("Ok Good Bye ;-)")

quotes = scarpeQuote()
startGame(quotes)