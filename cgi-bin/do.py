#!/usr/bin/python
import cgi, cgitb
import cloze
# Import modules for CGI handling 

# Create instance of FieldStorage 
#form = cgi.FieldStorage()

# Get data from fields
#words = form.getvalue()



print("Content-type:text/html" + "\n\n")

print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program</title>")
print("</head>")
print("<body>")
args = cgi.FieldStorage()
print('\n\n' + cloze.cloze(args.getvalue('word')))
print("</body>")
print("</html>")