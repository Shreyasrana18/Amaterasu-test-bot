
import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup
import ssl


# for https sites
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
username=input('Enter username:')

url = f'https://github-readme-streak-stats.herokuapp.com/?user={username}&theme=radical'
try :
    status_code = urllib.request.urlopen(url).getcode()

    response = urllib.request.urlopen(url,context=ctx).read()
    

    soup=BeautifulSoup(response,'html.parser')

    tags=soup('g',transform="translate(1,48)")

    total_contribuition=tags[0].get_text()

    tag2=soup('g',transform="translate(166,48)")
    current_streak=tag2[0].get_text()

    tag3=soup('g',transform="translate(331,48)")
    longest_streak=tag3[0].get_text()

    print('Total contributions:',total_contribuition.strip(),'Current Streak:',current_streak.strip(),'Longest Streak:',longest_streak.strip())
except :
    print('either site is down or u are down')

