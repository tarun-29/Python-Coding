from pyfiglet import Figlet

ans = input("What msg you want to print")
color = input("What Color")
f = Figlet()
print (f.renderText(ans))