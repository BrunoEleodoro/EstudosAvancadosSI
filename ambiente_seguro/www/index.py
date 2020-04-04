# Infrastructure test page.
import os
from flask import Flask
from flask import Markup
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask import request

app = Flask(__name__)

# Configure MySQL connection.
db = SQLAlchemy()
db_uri = 'mysql://root:supersecure@db/ambienteInseguro'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route("/")
def test():
    mysql_result = False
    query_string = text("SELECT 1")
    # TODO REMOVE FOLLOWING LINE AFTER TESTING COMPLETE.
    db.session.query("1").from_statement(query_string).all()
    try:
        if db.session.query("1").from_statement(query_string).all():
            mysql_result = True
    except:
        pass

    if mysql_result:
        result = Markup('<span style="color: green;">PASS</span>')
    else:
        result = Markup('<span style="color: red;">FAIL</span>')

    # Return the page with the result.
    return render_template('index.html', result=result)

@app.route("/teste")
def teste():
    id_user = request.args.get('id')
    
    # sql_select_Query = text(format(id_user))
    
    result = db.engine.execute("select * from user where id=%d", [id_user])

    # user = [row[1] for row in result]
    content = "<table>"
    content = content + str("<tr>")
    content = content + str("<th>nome</th>")
    content = content + str("<th>email</th>")
    content = content + str("<th>nro cartao</th>")
    content = content + str("</tr>")

    for row in result:
        content = content + str("<tr>")
        content = content + str("<td>"+str(row[1])+"</td>")
        content = content + str("<td>"+str(row[2])+"</td>")
        content = content + str("<td>"+str(row[3])+"</td>")
        content = content + str("</tr>")
        

    content = content + str("</table>")
    # print(content)
    result = Markup(content)

    return render_template('index.html', result=result)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
