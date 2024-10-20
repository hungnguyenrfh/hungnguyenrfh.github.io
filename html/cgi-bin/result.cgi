#!/usr/bin/python3
# -*-encoding: utf-8 -*-

import cgi
import cgitb
from datetime import datetime

cgitb.enable()

#this line sends an http header
print("Content-type: text/html\n\n")

#HTML header 
#div is created to contain the result in a box for easier formatting
print("""<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8"/>
	<title> Result </title>
	<link rel="stylesheet" type="text/css" href="./styles_result.css">
	<link rel="icon" type="image/x-icon" href="./img/html5.png">
</head>
<body>
	<div class="result-container">
	  <h2>Congratulations!</h2>
""")


#Get the values from the HTML Form
#birthdate is in string form, which will be transformed into a birthdate 
#object later on

form = cgi.FieldStorage()

name = form.getvalue("name")
birthdate_str = form.getvalue("birthdate")
gender = form.getvalue("gender")

#Parse the birthdate
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
day = birthdate.day
month = birthdate.month
year = birthdate.year

#convert the birthdate to dd-mm-yy format
birthdate_str2 = datetime.strftime(birthdate, "%d/%m/%Y")

#calculate the horoscope value for the loop
horoscopeValue = month * 100 + day;
horoscope = "None";
url="https://luongnguyenhungnguyen-20238583.s3.amazonaws.com/static/img/";
horoscopeImage = "";

#loop for horoscope
if horoscopeValue > 1221 or horoscopeValue < 120:
    horoscope = "Capricorn"
    horoscopeImage = url + "capricorn_1080x1080.png"
elif horoscopeValue < 219:
    horoscope = "Aquarius";
    horoscopeImage = url + "aquarius_1080x1080.png"
elif horoscopeValue < 321:
    horoscope = "Pisces";
    horoscopeImage = url + "pisces_1080x1080.png"
elif horoscopeValue < 420:
    horoscope = "Aries";
    horoscopeImage = url + "aries_1080x1080.png"
elif horoscopeValue < 521:
    horoscope = "Taurus";
    horoscopeImage = url + "taurus_1080x1080.png"
elif horoscopeValue < 621:
    horoscope = "Gemini";
    horoscopeImage = url + "gemini_1080x1080.png"
elif horoscopeValue < 723:
    horoscope = "Cancer";
    horoscopeImage = url + "cancer_1080x1080.png"
elif horoscopeValue < 823:
    horoscope = "Leo";
    horoscopeImage = url + "leo_1080x1080.png"
elif horoscopeValue < 923:
    horoscope = "Virgo";
    horoscopeImage = url + "virgo_1080x1080.png"
elif horoscopeValue < 1023:
    horoscope = "Libra";
    horoscopeImage = url + "libra_1080x1080.png"
elif horoscopeValue < 1122:
    horoscope = "Scorpio";
    horoscopeImage = url + "scorpio_1080x1080.png"
else:
    horoscope = "Sagittarius";
    horoscopeImage = url + "sagittarius_1080x1080.png"

print("<b>{}</b>, your birthdate is: {}".format(name, birthdate_str2))


#Display horoscope value for checking
#print("<b>Horoscope Value:</b> {}".format(horoscopeValue))
#print("<br>")

for i in range(5):
    print("<br>")

print("You are a <b>{} {}.</b>".format(gender, horoscope))

for i in range(4):
    print("<br>")

print("<img src={} alt={} width='270' height='270'>".format(horoscopeImage, horoscope))


#Closing the div Tags
print("</div>")




#Closing the HTML Tags
print("</body>")
print("</html>")

