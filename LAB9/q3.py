#! C:\Python27\python.exe
import cgi
import cgitb

cgitb.enable(display=1)
print "Content-Type: text/html"
form = cgi.FieldStorage()
if "name" not in form or "pswd" not in form:
	print "<h1>ERROR</h1>"
	print "Please fill in the name and addr fields."
	return

if form["name"].value == "admin":
	if form["pswd"].value == "password":
		print "<h1>LOGIN SUCCESSFUL</h1>"
	else:
		print "<h1>FAILED</h1>"
else:
	print "<h1>FAILED</h1>"