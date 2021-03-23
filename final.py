from tkinter import *
import pandas as pd
from tkinter import messagebox
from PIL import Image, ImageTk


def isnan(str) : 
    return str != str

def out() : 
    
    for i in symptoms : 
        if var[i].get() == 1 :
            user.append(i)
            
    freq = dict()
    maxfreq = 0
    
    for x in user:
        for i in range (1, m) :
            if isnan(graph[idx[x]][i]) == 1:
                break
            val = freq.setdefault( graph[idx[x]][i], 0)
            freq[ graph[idx[x]][i]] = val + 1
            maxfreq = max(maxfreq, val + 1)

    mostProbable = []
    lessProbable = []
    
    for key,val in freq.items() :
        if val == maxfreq :
            mostProbable.append(key)
        elif val == maxfreq - 1 :
            lessProbable.append(key)
        
    messagebox.showinfo(message="MOST PROBABLE ARE:  " + str(mostProbable))
    messagebox.showinfo(message="SOME OTHER POSSIBILITES ARE: " + str(lessProbable))

#graph reading
graph = pd.read_csv("D:\datacsv.csv").values
n = len(graph) #no. of rows
m = len(graph[0]) #no of cols

symptoms = [ graph[i][0] for i in range(n) ]
idx = dict()

for i in range(n) :
    idx[symptoms[i]] = i

user = []
root = Tk()
root.title("Disease Predictor")
root.geometry("1200x1200")
root.configure(background = "black")
root.iconbitmap("health.ico")
my_label = Label(root , text= "Which SYMPTOMS do you have??",font = ('Arial',15), fg= "#0D0D4F",  bg="#E7EA13").pack(side = TOP ,fill = X,expand = 2)



logo = Image.open('doct.jpg')
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.pack(side= LEFT, padx = 30, pady =40)



var = dict()

for i in symptoms :
    var[i] = IntVar()
    chk = Checkbutton(root, text = i, variable = var[i], width = 15, fg= "#FAE82B",  bg="#872919")
    chk.pack(side = TOP , fill=Y)
    
sub = Button(root, text = "Submit",command = out, font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
sub.pack(side = BOTTOM, fill = Y)
root.mainloop()