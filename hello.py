
"""from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000,debug=True)


"""
from flask import *  
import sqlite3

  
app = Flask(__name__)  
 
@app.route("/")  
def index():  
    return render_template("index.html");  
 
@app.route("/add")  
def add():  
    return render_template("add.html")  
 
@app.route("/savedetails",methods = ["POST","GET"])  
def saveDetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            name = request.form["name"]  
            email = request.form["email"]  
            # address = request.form["address"]  
            with sqlite3.connect("employee.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into Employees (name, email) values (?,?)",(name,email))  
                con.commit()  
                msg = "Attendance successfully Added"  
        except:  
            con.rollback()  
            msg = "We can not add the student to the list"  
        finally:  
            return render_template("success.html",msg = msg)  
            con.close()  
 
@app.route("/view")  
def view():  
    con = sqlite3.connect("employee.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Employees")  
    rows = cur.fetchall()  
    return render_template("view.html",rows = rows)  
 
 
"""@app.route("/delete")  
def delete():  
    return render_template("delete.html")

@app.route("/deleterecord",methods = ["POST"])  
def deleterecord():  
    id = request.form["id"]  
    with sqlite3.connect("employee.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("delete from Employees where id = ?",id)  
            msg = "record successfully deleted"  
        except:  
            msg = "can't be deleted"  
        finally:  
            return render_template("delete_record.html",msg = msg)  """
  
if __name__ == "__main__":

    import qrcode
    from PIL import Image
    import socket
    url_final = socket.gethostbyname(socket.gethostname())
    data = f"http://{url_final}:4500"
    img1 = qrcode.make(data)
    img1.save('site.png')
    logo = Image.open('site.png')
    logo.show()
    app.run('0.0.0.0',port=4500,debug = True)
    









