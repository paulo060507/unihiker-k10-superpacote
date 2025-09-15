import tkinter as tk
r=tk.Tk();r.title('K10 - Hello (sim)')
c=tk.Canvas(r,width=240,height=320,bg='black');c.pack()
c.create_text(120,160,text='Olá, K10!',fill='white',font=('Arial',18))
r.mainloop()
