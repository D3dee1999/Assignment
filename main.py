import streamlit as st
import sqlite3 
import pandas as pd

conn = sqlite3.connect('data.db')
c = conn.cursor()
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data

def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data

def main():
    #main page headtitle
    st.title("Welcome From Simbolo Registration")

    #for sidebar menu
    st.sidebar.title("Welcome !!")
    
    main = ["Home","Sign In","Sign Up"]

    choice = st.sidebar.selectbox("Main Menu",main) 

    if choice == 'Home':
        st.sidebar.title('Hello')
        
    elif choice == 'Sign In':
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password",type = "password")
        if st.sidebar.checkbox("Login"):
            create_usertable()
            result = login_user(username,password)
            
            if result:
                st.sidebar.success("Logined in Successfully as {} ".format(username))
                st.subheader("Welcome , {}".format(username))

                userchoice = st.selectbox("",["Add Post","Users' Profile",])
                    
                if userchoice == "Add Post":
                    st.subheader("Add Your Post")

                elif userchoice == "Users' Profile":
                    st.subheader("User's List")
                    user_list = view_all_users()
                    db = pd.DataFrame(user_list,columns=["Username","Password"])
                    st.dataframe(db)
                    
            else:
                st.sidebar.warning("Invalid Username or Password.")

    elif choice == 'Sign Up':
        regusername = st.text_input('Enter Username ')
        regpassowrd = st.text_input('Enter Password',type='password')
        regpassword2 = st.text_input('Confirm Your Password',type='password')
        
        if regpassowrd == regpassword2:
            if st.button("Sign Up"):
                create_usertable()
                add_userdata(regusername,regpassowrd)
                st.success('Welcome From Simbolo,Your New Account is created successfully.')
                st.info("Please Sign In From Main Menu")
                st.balloons()
            
            
        else:
            if st.button("Sign Up"):
                st.warning('Please Confirm Your Password.')
    

if __name__ == '__main__':
    main()