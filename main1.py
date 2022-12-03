from tkinter import *
from tkinter import messagebox
import random
color = "#ffffb3"
#CREATING GUI

window = Tk()
window.title("Password Manager")
window.minsize(width=700,height=700)
window.config(padx=100,pady=50,background=color)

canvas = Canvas(width=370,height=300,background=color)


img = PhotoImage(file="pwm.png")
canvas.create_image(210,200,image=img)
canvas.grid(row=0,column=1)

web_label = Label(text="Website :",font=('Arial',14,'bold'),pady=10,background=color)
web_label.grid(row=2,column=0)
web_input = Entry(width=35)
web_input.focus()
web_input.grid(row=2,column=1)

user_label = Label(text="E-mail/Username :",font=('Arial',14,'bold'),pady=10,background=color)
user_label.grid(row=3,column=0)
user_input = Entry(width=35)
user_input.insert(0,string='user@gmail.com')
user_input.grid(row=3,column=1)



pw_label = Label(text="Password :",font=('Arial',14,'bold'),pady=10,background=color)
pw_label.grid(row=4,column=0)
pw_input = Entry(width=26)
pw_input.grid(row=4,column=1)

#GENERATING PASSWORD
def generate() :
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        pw_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
        pw_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
        pw_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

        password_list = pw_letters + pw_numbers + pw_symbols
        random.shuffle(password_list)
        password = "".join(password_list)
        print(password)
        pw_input.insert(0,password)




gen_button = Button(text="Generate Password",width=30,background="green",command=generate)
gen_button.grid(row=4,column=2)


# SAVING PASSWORDS INTO A FILE
def save():
        web = web_input.get()
        user = user_input.get()
        pw = pw_input.get()

        if len(web)==0 or len(pw)==0:
            messagebox.showwarning(title="OOPS!",message="Please dont leave any field empty")
        else:
            is_ok = messagebox.askokcancel(title=web,message=f"These are the details entered\n"
                                                     f"E-Mail : {user}\n"
                                                     f"Password : {pw}\n"
                                                     f"Is it ok ?")
            if is_ok:
                with open("PASSWORD-MANAGER.txt", 'a') as file:
                    file.write(f"\n{web} | {user}+ | {pw}")
                    web_input.delete(0,END)
                    pw_input.delete(0,END)


add_button = Button(text="Add",width=30,background="red",command=save)
add_button.grid(row=5,column=1,pady=20)

window.mainloop()
