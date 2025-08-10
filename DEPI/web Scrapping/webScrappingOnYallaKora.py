import requests
import csv
from bs4 import BeautifulSoup

# date = input("Enter date in format MM/DD/YYYY: ")
date = "8/9/2025"
page = requests.get(f"https://www.yallakora.com/match-center?date={date}")

src = page.content # return the content of page in byte code format 
# print(src)


# because byte code is not readable for us we need to parsing it 
# parsing : convert byte code to code we can read it 
# To parse we need bs4 

soup = BeautifulSoup(src,"lxml") # lxml type of parsing 
# print(soup)

championships = soup.find_all("div" , {"class" : "matchCard"}) 
# print(championships)

nameOfChampionships = championships[0].contents[1].find("h2").text.strip()
allDate = championships[0].contents[3].find_all("div" , {"class" : ["item" , "finish" ,"liItem"]})
# print(allDate)
all_matchs = allDate[0].contents[1].contents[1].find("div" , {"class":"teamCntnr"}).contents[1]

matchA = all_matchs.find("div" ,{"class" : ["teams", "teamA"]}).find("p").text.strip()
matchB = all_matchs.find("div" , {"class" : ["teamB"]}).find("p").text.strip()
print(matchB)
print(matchA)

