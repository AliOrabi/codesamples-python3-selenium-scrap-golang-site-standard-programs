# codesamples-python3-selenium-scrap-golang-site-standard-repositories
Python 3.x Selenium Chrome driver scrapping the Playground page with Standard Programs moved from main page from Go language web site using custom programs provided
# Description
Python script attempt to scrap Playground page from Golang site https://play.golang.org/ 
using the test programs located in goprograms folder. 
# Purpose
To demonstrate the ability to create Web site scrapping scripts on Python 3.x using Selenium
And to honour another Great progrmming language - Go - https://golang.org/
# Requirements
Python 3.x - Python 3.6 recommended
Selenium, Chrome WebDriver
# Installation instructions (approximate, not the last ones to follow):
On Ubuntu Ubuntu 18.04.4 LTS
1) sudo apt-get install python3-pip
2) pip3 install selenium
3) sudo apt-get install chromium-browser
4) point 3) probably should install Chromium version 80.x
5) follow https://sites.google.com/a/chromium.org/chromedriver/downloads
6) on point 5) download appropriate chromedriver for chromium from points 3),4) - in our case 80.0.3987.106
7) extract the zip archieve from point 6) to your home folder
8) direct Linux Terminal application to your home folder with extracted chromedriver
9) [in Terminal] sudo mv chromedriver /usr/bin
10) [in Terminal] cd /usr/bin
11) [in Terminal] chmod a+x chromedriver
# How to run?
1) python3 PythonToGo.py to display help - e.g. the list of the standard example programs from https://golang.org/ with descriptions for you to choose
2) python3 PythonToGo.py hello to run the script featuring the example mentioned on https://golang.org/ site
# Notes
1) examples loacated in goprograms folder
2) please do not write comaplex and huge Go lang progarams, since the scrapper using the Playground from Go lang site, to spare some resources there for others and for the site itself
3) do not - not under any circumstances - attempt to DDoS https://golang.org/ site or any other site related to GoLang using this script 
