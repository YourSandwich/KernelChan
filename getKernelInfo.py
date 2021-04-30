import urllib.request
import os
from bs4 import BeautifulSoup

theurl = "https://archive.archlinux.org/packages/l/linux/"
thepage = urllib.request.urlopen(theurl)

soup = BeautifulSoup(thepage)

project_href = [i['href'] for i in soup.find_all('a', href=True)]
del project_href[0]

KernelVerList = []

## Making complicated stuff to extract only the Kernal Version from the WebScrap
for t in project_href[::2]:
    KernelVer = os.popen("echo " + t + " | cut -b 1-14 | cut -d'.' -f1,2,3 | sed 's/.arc//g' | sed 's/.ar//g' | sed 's/h//g' | sort -V")
    for i in KernelVer.read().split('\n')[::2]:   
        KernelVerList.append(i)