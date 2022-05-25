import tkinter as tk
from tkinter import ttk
import csv
import time

class Pizza:
  
  def __init__(self, name, base, ingredients):
    self.name = name
    self.base = base
    self.ingredients = ingredients
    self.state = False
    
  def create_pizza(self):
    pass
  
  def is_done(self):
    pass

class PizzaGui(tk.Frame):
  def __init__(self, parent, game_time_sec=5, bg="white", *args, **kwargs):
    tk.Frame.__init__(self, parent, bg=bg, *args, **kwargs)
    
    self.parent = parent
    self.bg = bg
    self.width  = 642 #1252
    self.height = 600
    self.game_time_sec = game_time_sec
    
    self.parent.geometry(f'{self.width}x{self.height}')

    self.title = tk.Label(self, text="Welcome To Pizza Game", highlightbackground=self.bg,
                          foreground="blue", font="DejaVu 15", borderwidth=3,
                          height=2, highlightthickness=30, relief="ridge")

    self.info = " Pizza dans le four "
    self.info1 = " Pizza en cours de préparation "
    self.info2 = " Pizza faite, vous pouvez en faire d'autres "
    
    self.check1 = tk.IntVar()
    self.check2 = tk.IntVar()
    self.check3 = tk.IntVar()

    self.counter4 = tk.IntVar()
    self.counter5 = tk.IntVar()
    self.counter6 = tk.IntVar()
    self.counter7 = tk.IntVar()
    self.counter8 = tk.IntVar()
    self.counter9 = tk.IntVar()

    self.pcount_oven = tk.IntVar()
    self.pcount_oven.set(0)

    self.time_sec = tk.IntVar()
    self.time_sec.set(self.game_time_sec)

    self.timer = tk.StringVar()
    self.timer.set(f"Timer: {self.time_sec.get()}/{self.game_time_sec}")

    self.score = tk.StringVar()
    self.score.set("Score: 0")   

    self.var_status_info = tk.StringVar()
    self.var_status_info.set("Aucune" + self.info)

    self.data = {'Hawaienne': [], 'Rucola': [], 'Poulet': []}

    with open('pizza.csv', 'r') as file:
      csv_file = csv.DictReader(file)
      for v in csv_file:
        self.data['Hawaienne'].append(v['Hawaienne'])
        self.data['Rucola'].append(v['Rucola'])
        self.data['Poulet'].append(v['Poulet'])

    #print(self.data)

    self.mbttn1 = tk.Menubutton(self, text=list(self.data.keys())[0], relief=tk.RAISED)
    self.mbttn2 = tk.Menubutton(self, text=list(self.data.keys())[1], relief=tk.RAISED)
    self.mbttn3 = tk.Menubutton(self, text=list(self.data.keys())[2], relief=tk.RAISED)

    self.menu1 = tk.Menu(self.mbttn1, tearoff=0)
    self.menu2 = tk.Menu(self.mbttn2, tearoff=0)
    self.menu3 = tk.Menu(self.mbttn3, tearoff=0)

    self.menu1.add_checkbutton(label="Base tomate", state=tk.DISABLED)
    self.menu1.add_checkbutton(label="3 morceaux de jambon", state=tk.DISABLED)
    self.menu1.add_checkbutton(label="3 morceaux d'ananas", state=tk.DISABLED)

    self.menu2.add_checkbutton(label="Base tomate", state=tk.DISABLED)
    self.menu2.add_checkbutton(label="7 lamelles de roquette", state=tk.DISABLED)

    self.menu3.add_checkbutton(label="Base blanche", state=tk.DISABLED)
    self.menu3.add_checkbutton(label="1 piment vert", state=tk.DISABLED)
    self.menu3.add_checkbutton(label="2 oignons", state=tk.DISABLED)

    self.mbttn1["menu"] = self.menu1
    self.mbttn2["menu"] = self.menu2
    self.mbttn3["menu"] = self.menu3
    
    self.cbtn1 = tk.Checkbutton(self, text="Base tomate", variable=self.check1,
                                    borderwidth=3, height=2, highlightthickness=5,
                                    highlightbackground=self.bg, bg=self.bg)
    self.cbtn2 = tk.Checkbutton(self, text="Base blanche", variable=self.check2,
                                    borderwidth=3, height=2, highlightthickness=5,
                                    highlightbackground=self.bg, bg=self.bg)
    self.cbtn3 = tk.Checkbutton(self, text="Base orange", variable=self.check3, 
                                    borderwidth=3, height=2, highlightthickness=5,
                                    highlightbackground=self.bg, bg=self.bg)

    self.lab_btn4 = tk.Label(self, textvariable=self.counter4,
                                    highlightbackground=self.bg, bg=self.bg)
    self.btn4 = tk.Button(self, text="Morceau d'ananas", command=self.on_click4,
                                    highlightbackground=self.bg, bg=self.bg)

    self.lab_btn5 = tk.Label(self, textvariable=self.counter5,
                                    highlightbackground=self.bg, bg=self.bg)
    self.btn5 = tk.Button(self, text="Morceau de jambon", command=self.on_click5,
                                    highlightbackground=self.bg, bg=self.bg)
    
    self.lab_btn6 = tk.Label(self, textvariable=self.counter6,
                                    highlightbackground=self.bg, bg=self.bg)
    self.btn6 = tk.Button(self, text="Lamelle de roquette", command=self.on_click6,
                                    highlightbackground=self.bg, bg=self.bg)

    self.lab_btn7 = tk.Label(self, textvariable=self.counter7,
                                    highlightbackground=self.bg, bg=self.bg)
    self.btn7 = tk.Button(self, text="Oignon", command=self.on_click7,
                                    highlightbackground=self.bg, bg=self.bg)

    self.lab_btn8 = tk.Label(self, textvariable=self.counter8,
                                    highlightbackground=self.bg, bg=self.bg)
    self.btn8 = tk.Button(self, text="Piment vert", command=self.on_click8,
                                    highlightbackground=self.bg, bg=self.bg)

    self.lab_btn9 = tk.Label(self, textvariable=self.counter9,
                                    highlightbackground=self.bg, bg=self.bg)
    self.btn9 = tk.Button(self, text="Épinard", command=self.on_click9,
                                    highlightbackground=self.bg, bg=self.bg)

    self.lab_timer = tk.Label(self, textvariable=self.timer, borderwidth=3,
                                    highlightthickness=30, relief="ridge",
                                    highlightbackground=self.bg)
    self.lab_score = tk.Label(self, textvariable=self.score, borderwidth=3,
                                    highlightthickness=30, relief="ridge",
                                    highlightbackground=self.bg)

    self.btn_send_pizza = tk.Button(self, text="Envoyer au four",
                                    bg='#0280FF', fg='white',
                                    relief=tk.FLAT,
                                    activeforeground='white',
                                    activebackground='#3D99F4',
                                    command=self.send_pizza,
                                    highlightthickness=20,
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
                                    command=self.start,
                                    highlightthickness=20,
                                    borderwidth=3,
                                    highlightbackground=self.bg)

    self.show_frame()
    self.countdown()
    #self.btn_send_pizza['state'] = tk.DISABLED
    #self.btn_start['state'] = tk.DISABLED
    #self.cbtn1.bind("<Button-1>", self.on_click_btn)
    #self.cbtn2.bind("<Button-1>", self.on_click_btn)
    #self.cbtn3.bind("<Button-1>", self.on_click_btn)
    #self.btn_send_pizza.bind("<Button-1>", self.on_click_btn)

  def on_click_btn(self, event):
    print(self.check1.get(), self.check2.get(), self.check3.get())
    #if self.check1.get() or self.check2.get() or self.check3.get():
    #  self.btn_send_pizza['state'] = tk.DISABLED
    #  print("Clicked")
    #else:
    #  self.btn_send_pizza['state'] = tk.NORMAL
    #  print("Not Clicked")

  def on_click4(self): self.counter4.set(self.counter4.get() + 1)
  def on_click5(self): self.counter5.set(self.counter5.get() + 1)
  def on_click6(self): self.counter6.set(self.counter6.get() + 1)
  def on_click7(self): self.counter7.set(self.counter7.get() + 1)
  def on_click8(self): self.counter8.set(self.counter8.get() + 1)
  def on_click9(self): self.counter9.set(self.counter9.get() + 1)

  def change_btn_state(self, btn, normal=True):
    if normal: btn['state'] = tk.NORMAL
    else: btn['state'] = tk.DISABLED
  
  def change_all_btn_state(self, normal=True):
    self.change_btn_state(self.cbtn1, normal=normal)
    self.change_btn_state(self.cbtn2, normal=normal)
    self.change_btn_state(self.cbtn3, normal=normal)
    self.change_btn_state(self.btn4, normal=normal)
    self.change_btn_state(self.btn5, normal=normal)
    self.change_btn_state(self.btn6, normal=normal)
    self.change_btn_state(self.btn7, normal=normal)
    self.change_btn_state(self.btn8, normal=normal)
    self.change_btn_state(self.btn9, normal=normal)

  def reset_counter(self):
    self.check1.set(0)
    self.check2.set(0)
    self.check3.set(0)
    self.counter4.set(0)
    self.counter5.set(0)
    self.counter6.set(0)
    self.counter7.set(0)
    self.counter8.set(0)
    self.counter9.set(0)
    self.pcount_oven.set(0)

  def send_pizza(self):
    if self.check1.get() or self.check2.get() or self.check3.get():
      self.pcount_oven.set(self.pcount_oven.get() + 1)
      self.var_status_info.set(str(self.pcount_oven.get()) + self.info)
    else: self.var_status_info.set("Vous n'avez composé aucune pizza")
  
  def start(self):
    if self.check1.get() or self.check2.get() or self.check3.get():
      self.var_status_info.set(str(self.pcount_oven.get()) + self.info + "0%")
    else: self.var_status_info.set("Aucune" + self.info)
    
    self.change_all_btn_state(normal=False)
    
    if self.pcount_oven.get() > 0:
      self.bar()

    self.change_all_btn_state()
    self.reset_counter()
    self.pbar['value'] = 0

  def game_over(self):
    self.change_all_btn_state(normal=False)
    self.btn_send_pizza['state'] = tk.DISABLED
    self.btn_start['state'] = tk.DISABLED
    self.var_status_info.set("Fin du jeu")

  def bar(self):
    self.pbar['value'] = 20
    self.var_status_info.set(str(self.pcount_oven.get()) + self.info1 + str(20) + "%")
    self.update_idletasks()
    time.sleep(1)
  
    self.pbar['value'] = 40
    self.var_status_info.set(str(self.pcount_oven.get()) + self.info1 + str(40) + "%")
    self.update_idletasks()
    time.sleep(1)
  
    self.pbar['value'] = 50
    self.var_status_info.set(str(self.pcount_oven.get()) + self.info1 + str(50) + "%")
    self.update_idletasks()
    time.sleep(1)
  
    self.pbar['value'] = 60
    self.var_status_info.set(str(self.pcount_oven.get()) + self.info1 + str(60) + "%")
    self.update_idletasks()
    time.sleep(1)
  
    self.pbar['value'] = 80
    self.var_status_info.set(str(self.pcount_oven.get()) + self.info1 + str(80) + "%")
    self.update_idletasks()
    time.sleep(1)
    self.pbar['value'] = 100
    self.var_status_info.set(str(self.pcount_oven.get()) + self.info1 + str(100) + "%")
    self.update_idletasks()
    time.sleep(1)
    self.var_status_info.set(str(self.pcount_oven.get()) + self.info2)

  def countdown(self):
    time.sleep(1)
    self.time_sec.set(self.time_sec.get() - 1)
    self.timer.set(f"Timer: {self.time_sec.get()}/{self.game_time_sec}")

    if self.time_sec.get() == 0:
      self.game_over()
    else: self.after(1000, self.countdown)

  def show_frame(self):
    #self.rowconfigure(0, weight=1)
    #self.columnconfigure(0, weight=1)
    #self.columnconfigure(1, weight=1)

    self.title.grid(row=0, column=1, sticky="nswe")
    
    self.mbttn1.grid(row=1, column=0, sticky="nswe")
    self.mbttn2.grid(row=1, column=1, sticky="nswe")
    self.mbttn3.grid(row=1, column=2, sticky="nswe")

    self.cbtn1.grid(row=2, column=2, sticky="nswe")
    self.cbtn2.grid(row=2, column=1, sticky="nswe")
    self.cbtn3.grid(row=2, column=0, sticky="nswe")

    self.lab_btn4.grid(row=3, column=0, sticky="nswe")
    self.lab_btn5.grid(row=3, column=1, sticky="nswe")
    self.lab_btn6.grid(row=3, column=2, sticky="nswe")

    self.btn4.grid(row=4, column=0, sticky="nswe")
    self.btn5.grid(row=4, column=1, sticky="nswe")
    self.btn6.grid(row=4, column=2, sticky="nswe")

    self.lab_btn7.grid(row=5, column=0, sticky="nswe")
    self.lab_btn8.grid(row=5, column=1, sticky="nswe")
    self.lab_btn9.grid(row=5, column=2, sticky="nswe")

    self.btn7.grid(row=6, column=0, sticky="nswe")
    self.btn8.grid(row=6, column=1, sticky="nswe")
    self.btn9.grid(row=6, column=2, sticky="nswe")

    self.btn_send_pizza.grid(row=7, column=1, sticky="nswe")

    self.lab_timer.grid(row=8, column=0, sticky="nswe")
    self.lab_status_info.grid(row=8, column=1, sticky="nswe")
    self.lab_score.grid(row=8, column=2, sticky="nswe")

    self.pbar.grid(row=9, column=1, sticky="nswe")

    self.btn_start.grid(row=10, column=1, sticky="nswe")
  
def run():
    root = tk.Tk()
    root.title("Pizza")
    PizzaGui(root).pack(fill="both", expand=True)
    root.mainloop()

#--------------------------------          
if __name__ == '__main__': run()