import urllib.request
import os
from bs4 import BeautifulSoup

# TODO: Change Bash cut to RegEx and fix the Version sorting

theurl = "https://archive.archlinux.org/packages/l/linux/"
thepage = urllib.request.urlopen(theurl)

soup = BeautifulSoup(thepage)

project_href = [i['href'] for i in soup.find_all('a', href=True)]
del project_href[0]

KernelURL = []
KernelVerList = []

for m in project_href[::2]:   
    KernelURL.append("https://archive.archlinux.org/packages/l/linux/"+m)

## Making complicated stuff to extract only the Kernal Version from the WebScrap
for t in project_href[::2]:
    KernelVer = os.popen("echo " + t + " | cut -d'.' -f1,2,3 | sed 's/.arc//g' | sed 's/-x86_64//g' | sed 's/.ar//g' | sed 's/h//g'")
    for i in KernelVer.read().split('\n')[::2]:   
        KernelVerList.append(i)