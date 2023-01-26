#Install customtkinter using pip3

import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


root = customtkinter.CTk()
root.geometry("800*800")
frame = customtkinter.CTkFrame(master = root)
frame.pack(pady = 20 , padx = 20 , fill = "both", expand =True)

#create labale
lable = customtkinter.CTkLabel (master = frame , text = "Login to System")
lable.pack(pady =20 , padx = 10)
#createtextbox
entry1 = customtkinter.CTkEntry(master = frame , placeholder_text = "Username")
entry1.pack(pady =12 , padx =10)
#create textbox
entry2 = customtkinter.CTkEntry(master = frame , placeholder_text = "Password", show= "*")
entry2.pack(pady =12 , padx =10)
#create button
#create check box
checkbox = customtkinter.CTkCheckBox(master = frame , text = "Remember Me")
checkbox.pack(pady =12 , padx=10)

def login():
    defaultusername = "admin"
    defaultpassword = "123456"

    if entry1 == defaultusername and entry2 == defaultpassword:
        lable = customtkinter.CTkLabel(master=frame , text = "you logged in successfuly")
        lable.pack(pady =20 , padx = 10)
        
    else :
        lable = customtkinter.CTkLabel(master=frame , text= "Username Or Password is invalid")
        lable.pack(pady =20 , padx = 10)

button = customtkinter.CTkButton(master = frame , text = "Login" , command = login)
button.pack(pady =12 , padx =10)


root.mainloop()
