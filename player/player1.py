from tkinter import *
from tkinter import ttk
import tkinter


root = Tk()
root.title("MISTER DJ ")
root.state('zoomed')

#root.columnconfigure(1, weight=4)
#root.columnconfigure(0, weight=1)   
#root.rowconfigure(0, weight=4)
#root.rowconfigure(1, weight=1)
#estilo=ttk.Style()
#estilo.theme_use()
#pw = PanedWindow(root,orient=HORIZONTAL)





pesquisa= Label(root,text="pesquisa do youtube", background="red", width=57)

pesquisa.pack(side=LEFT, fill=Y)

biblioteca_pw= PanedWindow(root,orient="vertical", background="blue")


biblioteca= Label(biblioteca_pw,text="Mister Id é foda, e essa é a biblioteca dele",background="purple", height=35)

biblioteca_pw.add(biblioteca)
biblioteca_pw.pack(side=TOP, fill=BOTH)

decks= Frame(root)





deck1= Label(decks,text="deck1",background="#f1c232")
pross_bar1=ttk.Progressbar(deck1, maximum=50).pack()
deck1.pack(side=LEFT, fill=BOTH, expand=True)
deck2= Label(decks,text="deck2",background="#6aa84f")
deck2.pack(side=RIGHT, fill=BOTH, expand=True)
#deck2.pack()
pross_bar2=ttk.Progressbar(deck2, maximum=50)
pross_bar2.pack()
#pross_bar2.pack()

decks.pack(side=BOTTOM, fill=BOTH, expand=True)







#biblioteca.grid(column=1, row=0)
#pesquisa.grid(column=0,row=0,rowspan=2)
#decks.grid(column=1, row=1)
#deck1.grid(column=0, row=0)
#deck2.grid(column=1, row=0)
#biblioteca.columnconfigure(0,weight=2)
#decks.columnconfigure(0, weight=1)
#decks.columnconfigure(1, weight=1)
#decks.rowconfigure(0,weight=1)



#biblioteca_pw.pack(fill="y",expand=True)
#decks.pack( expand=True)
'''
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)


'''

root.mainloop()