# Python code to illustrate and create a
# table in database
import mysql.connector
import login as log
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="system",
  database="register"
)

mycursor = mydb.cursor()
#sql = "DROP TABLE reg_tb"

#mycursor.execute(sql)

#mycursor.execute("CREATE TABLE reg_tb (name VARCHAR(255),user_id VARCHAR(255)  PRIMARY KEY,age int(50),email VARCHAR(50),password VARCHAR(50))");
#mycursor.execute("SHOW TABLES")

sql = "SELECT * FROM reg_tb "

mycursor.execute(sql)

myresult = mycursor.fetchall()
for i in myresult:
  print(i)

#for x in myresult:
  #print(x)

    #if "page" not in st.session_state:
        #st.session_state.page = "Home"
    #if st.session_state.page == "Login":
        #log.login_form()
    #elif st.session_state.page == "app":
     #   ap.app()
