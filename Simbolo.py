import streamlit as st

def main():
    """Simbolo Discussion Website"""
    st.title("Simbolo Student Discussion Site")
    menu=["Home","Login","Sign Up"]
    st.sidebar.title("Welcome , Simbolo")
    choice=st.sidebar.selectbox("Main Menu",menu) 
    
    if choice == "Home":
        st.header("Welcome , Simbolo Discuss Post")
        
    elif choice == "Login":   
        st.header("Welcome , Please Login Your Account")
        
        username=st.sidebar.text_input("Username")
        password=st.sidebar.text_input("Password",type='password')
        if st.sidebar.checkbox("Login"):
            if username == "admin" and password == "12345":
                st.success("Login Success as {} ".format(username))
                

                task = st.selectbox("Task",["Add Post","Analysis"])
                if task == "Add Post":
                    st.write("Add Text")
                elif task == "Analysis":
                    st.write("Analysis")



            else:
                st.sidebar.error("Invalid Username or Password")



    elif choice == "Sign Up":
        st.header("Welcome , Please Create New Account")

        username=st.sidebar.text_input("Username",)
        password=st.sidebar.text_input("Password",type='password',key="a")
        repassword=st.sidebar.text_input("Confirm Password",type='password',key="b")
        if password == repassword:
            if st.sidebar.button("Login"):
                st.sidebar.success("Create Account Successfully.")
                st.balloons()
                st.sidebar.info("Go Main Menu to Login")
        else:
            if st.sidebar.button("Login"):
                st.sidebar.warning("Please Check Your Password")





if __name__ == '__main__':
    main()


