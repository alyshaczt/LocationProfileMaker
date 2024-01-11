#!/usr/bin/ruby

require 'cgi'

cgi = CGI.new

city = cgi['city'].capitalize
province = cgi['province'].capitalize
country = cgi['country'].capitalize
picture_url = cgi['picture_url']

puts "Content-type: text/html\n\n"
puts "<html>"
puts "<head>"
puts "<title>City Information</title>"
puts "<style>"
puts "body { background-color: #c06378; }"
puts "h1 { color: #c06378; background-color: #663845; text-align: center; padding: 0.5em; width: 80%; margin: auto; border-radius: 15px; }"
puts "img { width: 100%; }"
puts "</style>"
puts "</head>"
puts "<body>"
puts "<h1>#{city}, #{province}, #{country}</h1>"
puts "<img src='#{picture_url}' alt='#{city}'>"
puts "</body>"
puts "</html>"
