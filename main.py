import tkinter as tk
from tkinter import ttk
import csv
import time
import pizza

class PizzaGui(tk.Frame):
  def __init__(self, parent, bg="white", *args, **kwargs):
    tk.Frame.__init__(self, parent, bg=bg, *args, **kwargs)
    
    self.parent = parent
    self.bg = bg
    self.width  = 1252
    self.height = 600
    
    self.parent.geometry(f'{self.width}x{self.height}')

    self.title = tk.Label(self, text="Welcome To Pizza Game", highlightbackground=self.bg,
                          foreground="blue", font="DejaVu 15", borderwidth=3,
                          height=2, highlightthickness=30, relief="ridge")
    
    self.recipe1 = tk.Label(self, text="Recipe", width=20,
                            foreground="black", highlightbackground=self.bg)

    self.recipe2 = tk.Label(self, text="Recipe", width=20,
                            foreground="black", highlightbackground=self.bg)
    
    self.recipe3 = tk.Label(self, text="Recipe", width=20,
                            foreground="black", highlightbackground=self.bg)

    self.info = "Pizza en cours de préparation "
    
    self.var1 = tk.IntVar()
    self.var2 = tk.IntVar()
    self.var3 = tk.IntVar()

    self.var_status_info = tk.StringVar()
    self.var_status_info.set(self.info + " 0%")

    self.data = {'Hawaienne': [], 'Rucola': [], 'Poulet': []}

    with open('pizza.csv', 'r') as file:
      csv_file = csv.DictReader(file)
      for v in csv_file:
        self.data['Hawaienne'].append(v['Hawaienne'])
        self.data['Rucola'].append(v['Rucola'])
        self.data['Poulet'].append(v['Poulet'])

    print(self.data)

    self.mbttn1 = tk.Menubutton(self, text=list(self.data.keys())[0], relief=tk.RAISED)
    self.mbttn2 = tk.Menubutton(self, text=list(self.data.keys())[1], relief=tk.RAISED)
    self.mbttn3 = tk.Menubutton(self, text=list(self.data.keys())[2], relief=tk.RAISED)

    self.menu1 = tk.Menu(self.mbttn1, tearoff=0)
    self.menu2 = tk.Menu(self.mbttn2, tearoff=0)
    self.menu3 = tk.Menu(self.mbttn3, tearoff=0)

    self.menu1.add_checkbutton(label="Base tomate", variable=self.var1)
    self.menu2.add_checkbutton(label="Base tomate", variable=self.var2)
    self.menu3.add_checkbutton(label="Base blanche", variable=self.var3)

    self.mbttn1["menu"] = self.menu1
    self.mbttn2["menu"] = self.menu2
    self.mbttn3["menu"] = self.menu3

    self.lab_timer = tk.Label(self, text="Timer: 1/5", borderwidth=3,
                                    height=2, highlightthickness=30, relief="ridge",
                                    highlightbackground=self.bg)
    self.lab_score = tk.Label(self, text="Score: 20", borderwidth=3,
                                    height=2, highlightthickness=30, relief="ridge",
                                    highlightbackground=self.bg)

    self.btn_send_pizza = tk.Button(self, text="Envoyer au four",
                                    bg='#0280FF', fg='white',
                                    relief=tk.FLAT,
                                    activeforeground='white',
                                    activebackground='#3D99F4',
                                    command=self.bar,
                                    highlightthickness=30,
                                    borderwidth=3,
                                    highlightbackground=self.bg)
    s = ttk.Style()
    s.theme_use('default')
    s.configure("red.Horizontal.TProgressbar", foreground='#69E206', background='#69E206', highlightbackground=self.bg)
    self.pbar = ttk.Progressbar(self, style="red.Horizontal.TProgressbar", orient=tk.HORIZONTAL,
                              length=100, mode='determinate')

    self.lab_status_info = tk.Label(self, textvariable=self.var_status_info, borderwidth=3,
                                    height=2, highlightthickness=20, relief="ridge",
                                    highlightbackground=self.bg)
    
    self.btn_start = tk.Button(self, text="Démarrer",
                                    bg='green', fg='white',
                                    relief=tk.FLAT,
                                    activeforeground='white',
                                    activebackground='#6eaa5e',
                                    highlightthickness=20,
                                    borderwidth=3,
                                    highlightbackground=self.bg)

    self.show_frame()

  def bar(self):
    self.pbar['value'] = 20
    self.var_status_info.set(self.info + str(20) + "%")
    self.update_idletasks()
    time.sleep(1)
  
    self.pbar['value'] = 40
    self.var_status_info.set(self.info + str(40) + "%")
    self.update_idletasks()
    time.sleep(1)
  
    self.pbar['value'] = 50
    self.var_status_info.set(self.info + str(50) + "%")
    self.update_idletasks()
    time.sleep(1)
  
    self.pbar['value'] = 60
    self.var_status_info.set(self.info + str(60) + "%")
    self.update_idletasks()
    time.sleep(1)
  
    self.pbar['value'] = 80
    self.var_status_info.set(self.info + str(80) + "%")
    self.update_idletasks()
    time.sleep(1)
    self.pbar['value'] = 100
    self.var_status_info.set(self.info + str(100) + "%")

  def show_frame(self):
    #self.rowconfigure(0, weight=1)
    #self.columnconfigure(0, weight=1)
    #self.columnconfigure(1, weight=1)

    self.title.grid(row=0, column=1, sticky="nswe")
    
    self.recipe1.grid(row=1, column=0, sticky="nswe")
    self.recipe2.grid(row=1, column=1, sticky="nswe")
    self.recipe3.grid(row=1, column=2, sticky="nswe")
    
    self.mbttn1.grid(row=2, column=0, sticky="nswe")
    self.mbttn2.grid(row=2, column=1, sticky="nswe")
    self.mbttn3.grid(row=2, column=2, sticky="nswe")

    self.lab_timer.grid(row=3, column=0, sticky="nswe")
    self.btn_send_pizza.grid(row=3, column=1, sticky="nswe")
    self.lab_score.grid(row=3, column=2, sticky="nswe")

    self.pbar.grid(row=4, column=1, sticky="nswe")

    self.lab_status_info.grid(row=5, column=1, sticky="nswe")

    self.btn_start.grid(row=6, column=1, sticky="nswe")
  
def run():
    root = tk.Tk()
    root.title("Pizza")
    PizzaGui(root).pack(fill="both", expand=True)
    root.mainloop()

#--------------------------------          
if __name__ == '__main__': run()