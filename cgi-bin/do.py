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
try:  # 這一段單純為了不要讓網頁的error被使用者看到而添加的
    args = cgi.FieldStorage()
    print('\n\n' + cloze.cloze(str(args.getvalue('word'))).lower())
except:
    pass
print("</body>")
print("</html>")