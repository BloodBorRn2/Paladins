import time
import webbrowser
print("Hello human, its a liitle test for you.")
time.sleep(0.7)
print("Say me your name, human")
time.sleep(0.7)
a= input(("I am "))
print("Loading...")
time.sleep(2)
print("Okay",a,",lets start")
print("You can answer only Yes or No")
time.sleep(0.7)
print("1)",a,",do You play videgames?")
time.sleep(0.7)
b = input()
if b == "Yes" or b == "yes":
    print("Very nice")
elif b == "No" or b == "no":
    print("Dont be dumb, i know that you play videogames")
else:
    print("I wrote, Yes or No, pussy")
    exit()
time.sleep(0.7)
print("2)Do you have social life or girlfriend?")
time.sleep(0.7)
c = input()
if c == "No" or c == "no":
    webbrowser.open_new("https://store.steampowered.com/app/444090/Paladins/")
elif c == "Yes" or c == "yes":
    print("You are lier.")
    exit()
else:
    print("You are dumb dude")
    exit()
