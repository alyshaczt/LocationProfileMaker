#!/usr/bin/python

import cgi, cgitb

cgitb.enable()

form = cgi.FieldStorage()
city = form.getvalue('city').upper()
province = form.getvalue('province').upper()
country = form.getvalue('country').upper()
picture_url = form.getvalue('picture_url')

print "Content-type:text/html\n\n"

print "<html>"
print "<head>"
print "<title>City Information</title>"
print "<style>"
print "body {background-color: #321e25;}"
print "h1 {font-size: 2em; color: #e894a7; background-color: #8b4e5e; text-align: center; padding: 0.5em; width: 70%; margin:auto; border-radius: 10px;}"
print "img {width: 80%; margin: auto; border: 30px solid #e894a7; display: block; border-radius: 10px;}"
print "</style>"
print "</head>"
print "<body>"
print "<h1>{}, {}, {}</h1>".format(city, province, country)
print "<img src='{}' alt='{}'>".format(picture_url, city)
print "</body>"
print "</html>"

