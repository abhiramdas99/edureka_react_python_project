from flask import Flask
from flask_mysqldb import MySQL
from flask import jsonify
from flask import flash, Request

app=Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']='python_web_mysql'

mysql=MySQL(app)


#Members api route 
@app.route("/employees")
def employees():
    try:
        cur=mysql.connection.cursor()
        data=cur.execute("select * from employee_detail")
        if data>0:
            rows=cur.fetchall()
            resp=jsonify({"employees":rows})
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)
    finally:
        cur.close()

if __name__=="__main__":
    app.run(debug=True)