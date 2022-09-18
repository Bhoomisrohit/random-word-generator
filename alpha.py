from cProfile import label
from tkinter import*
import random
root=Tk()
root.title("List")
root.geometry("400x400")
label=Label(root,text="name in ascii : ",bg="yellow",fg="black")


def randomalpha():
    alpha_list=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    random_no1=random.randint(1,26)
    random_no2=random.randint(1,26)
    random_no3=random.randint(1,26)
    random_no4=random.randint(1,26)
    random_no5=random.randint(1,26)
    random_apha1=alpha_list[random_no1]
    random_apha2=alpha_list[random_no2]
    random_apha3=alpha_list[random_no3]
    random_apha4=alpha_list[random_no4]
    random_apha5=alpha_list[random_no5]
    text

btn=Button(root,text="who is your lucky friend?", command=randomnumber)    
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()