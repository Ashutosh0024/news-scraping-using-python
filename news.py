import requests
import csv
import time
from bs4 import BeautifulSoup
import pdb

url = "https://www.livemint.com/mostpopular"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
for a in soup.findAll('a'):
  href = a.get('href')
  a["href"] = "https://www.livemint.com" + str(href)
headlines = soup.find_all("h2")

f = open("news.html", "w")
f.write('<html><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"><link rel="stylesheet" href="style.css"><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous"><body style="background-color:#F7F7F7;"><title>top news</title><nav class="navbar navbar-dark bg-primary"><a class="navbar-brand"><b style="color:white";>TRENDING NEWS</b></a><form class="form-inline"><input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search"><button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button></form></nav><hr><div class="icon-bar"><a href="#" class="facebook"><i class="fa fa-facebook"></i></a> <a href="#" class="twitter"><i class="fa fa-twitter"></i></a> <a href="#" class="google"><i class="fa fa-google"></i></a> <a href="#" class="linkedin"><i class="fa fa-linkedin"></i></a><a href="#" class="youtube"><i class="fa fa-youtube"></i></a> </div><img src="https://www.realviewdigital.com/wp-content/uploads/2016/11/American_Newspapers-stock.jpg" class="img-fluid" alt="Responsive image"><hr class="style-three"><div id="container">')
for headline in headlines:
  f.write(str(headline))
  f.write('<br>')
f.write('</div></div></html>')
f.close()
