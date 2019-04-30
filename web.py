#!/usr/bin/env python
from flask import Flask, render_template
import mysql.connector
app = Flask("Sait")

mydb = mysql.connector.connect(
  host = "localhost",
  user = "yassen_test_user",
  passwd = "lordbiznes2004",
  database = "yassen_test"
)

@app.route("/")
def index():
   return render_template("index.html")

if __name__ == '__main__':
   app.run(debug = True)
