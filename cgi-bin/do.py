#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb
import cloze

# Create instance of FieldStorage 
#form = cgi.FieldStorage()

# Get data from fields
#words = form.getvalue()
print(cloze.cloze("word"))

args = cgi.FieldStorage()


print("Content-type:text/html" + "\n\n")

print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program</title>")
print("</head>")
print("<body>")
print('\n\n' + cloze.cloze(args.getvalue('word')))
print("</body>")
print("</html>")