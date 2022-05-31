import tkinter as tk
from tkinter import ttk
import csv
import time

class Pizza:
  def __init__(self):
    self.name = None
    self.base = None
    self.ingredients = []

  def create(self, name=None, base="", ingredients=[]):
    self.name = name
    self.base = base
    self.ingredients = ingredients

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      raise TypeError(other, " is not a Pizza type")
    if other.base == self.base and set(other.ingredients) == set(self.ingredients):
      return 10
    else: return 0

  def __str__(self):
    return "Base: " + self.base + " | Ingrédients: " + ", ".join(self.ingredients)

class Oven:
  def __init__(self, timer=30):
    self.in_oven = []
    self.timer = timer
  
  def get(self):
    return self.in_oven

  def add(self, p):
    if len(self.in_oven) > 3: return False
    self.in_oven.append(p)
    return True

  def is_empty(self):
    return True if len(self.in_oven) == 0 else False

  def is_done(self):
    time.sleep(self.timer//6)
    return True

  def quant(self):
    return len(self.in_oven)

  def clean(self):
    self.in_oven = []

class PizzaGui(tk.Frame):
  def __init__(self, parent, game_time_sec=60, bg="white", *args, **kwargs):
    tk.Frame.__init__(self, parent, bg=bg, *args, **kwargs)
    
    self.parent = parent
    self.bg = bg
    self.width  = 1170
    self.height = 800
    self.game_time_sec = game_time_sec
    
    self.pizza = Pizza()
    self.oven  = Oven()
    
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

    self.count_score = 0

    self.score = tk.StringVar()
    self.score.set(f"Score: {self.count_score}")

    self.var_status_info = tk.StringVar()
    self.var_status_info.set("Aucune" + self.info)

    self.var1 = tk.StringVar()
    self.var2 = tk.StringVar()
    self.var3 = tk.StringVar()
    self.var4 = tk.StringVar()
    self.var5 = tk.StringVar()
    self.var6 = tk.StringVar()
    self.var7 = tk.StringVar()
    self.var8 = tk.StringVar()
    self.var9 = tk.StringVar()

    self.quant1 = tk.IntVar()
    self.quant2 = tk.IntVar()
    self.quant3 = tk.IntVar()
    self.quant4 = tk.IntVar()
    self.quant5 = tk.IntVar()
    self.quant6 = tk.IntVar()
    self.quant7 = tk.IntVar()
    self.quant8 = tk.IntVar()
    self.quant9 = tk.IntVar()

    self.quant1.set(6)
    self.quant2.set(6)
    self.quant3.set(6)
    self.quant4.set(30)
    self.quant5.set(30)
    self.quant6.set(35)
    self.quant7.set(20)
    self.quant8.set(20)
    self.quant9.set(20)

    self.can_send = False

    self.pdict = {'Hawaienne': [], 'Rucola': [], 'Poulet': []}

    with open('pizza.csv', 'r') as file:
      csv_file = csv.DictReader(file)
      for v in csv_file:
        self.pdict['Hawaienne'].append(v['Hawaienne'])
        self.pdict['Rucola'].append(v['Rucola'])
        self.pdict['Poulet'].append(v['Poulet'])
    
    # Remove empty strings from a list of strings
    self.pdict['Hawaienne'] = list(filter(None, self.pdict['Hawaienne']))
    self.pdict['Rucola'] = list(filter(None, self.pdict['Rucola']))
    self.pdict['Poulet'] = list(filter(None, self.pdict['Poulet']))

    self.ph = Pizza()
    self.pr = Pizza()
    self.pp = Pizza()

    self.ph.create('Hawaienne', self.pdict['Hawaienne'][0], self.pdict['Hawaienne'][1:])
    self.pr.create('Rucola', self.pdict['Rucola'][0], self.pdict['Rucola'][1:])
    self.pp.create('Poulet', self.pdict['Poulet'][0], self.pdict['Poulet'][1:])
    
    self.mbttn1 = tk.Menubutton(self, text=list(self.pdict.keys())[0], relief=tk.RAISED)
    self.mbttn2 = tk.Menubutton(self, text=list(self.pdict.keys())[1], relief=tk.RAISED)
    self.mbttn3 = tk.Menubutton(self, text=list(self.pdict.keys())[2], relief=tk.RAISED)

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
                                    highlightbackground=self.bg, bg=self.bg, command=self.onclick1)
    self.cbtn2 = tk.Checkbutton(self, text="Base blanche", variable=self.check2,
                                    borderwidth=3, height=2, highlightthickness=5,
                                    highlightbackground=self.bg, bg=self.bg, command=self.onclick2)
    self.cbtn3 = tk.Checkbutton(self, text="Base orange", variable=self.check3, 
                                    borderwidth=3, height=2, highlightthickness=5,
                                    highlightbackground=self.bg, bg=self.bg, command=self.onclick3)

    self.lab_btn4 = tk.Label(self, textvariable=self.counter4,
                                    highlightbackground=self.bg, bg=self.bg)
    self.btn4 = tk.Button(self, text="morceaux d'ananas", command=self.onclick4,
                                    highlightbackground=self.bg, bg=self.bg)

    self.lab_btn5 = tk.Label(self, textvariable=self.counter5,
                                    highlightbackground=self.bg, bg=self.bg)
    self.btn5 = tk.Button(self, text="morceaux de jambon", command=self.onclick5,
                                    highlightbackground=self.bg, bg=self.bg)
    
    self.lab_btn6 = tk.Label(self, textvariable=self.counter6,
                                    highlightbackground=self.bg, bg=self.bg)
    self.btn6 = tk.Button(self, text="lamelles de roquette", command=self.onclick6,
                                    highlightbackground=self.bg, bg=self.bg)

    self.lab_btn7 = tk.Label(self, textvariable=self.counter7,
                                    highlightbackground=self.bg, bg=self.bg)
    self.btn7 = tk.Button(self, text="oignons", command=self.onclick7,
                                    highlightbackground=self.bg, bg=self.bg)

    self.lab_btn8 = tk.Label(self, textvariable=self.counter8,
                                    highlightbackground=self.bg, bg=self.bg)
    self.btn8 = tk.Button(self, text="piment vert", command=self.onclick8,
                                    highlightbackground=self.bg, bg=self.bg)

    self.lab_btn9 = tk.Label(self, textvariable=self.counter9,
                                    highlightbackground=self.bg, bg=self.bg)
    self.btn9 = tk.Button(self, text="épinards", command=self.onclick9,
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
    
    self.btn_start = tk.Button(self, text="Allumer le four",
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
    #self.cbtn1.bind("<Button-1>", self.onclick)
    #self.cbtn2.bind("<Button-1>", self.onclick)

  def onclick1(self):
    #print(self.cbtn1.config()["text"][-1])
    if self.check1.get():
      self.var1.set(self.cbtn1.config()["text"][-1])
      self.quant1.set(self.quant1.get() - 1)
      self.can_send = True
    else:
      self.var1.set("")
      self.can_send = False

    if self.quant1.get() <= 0:
      self.cbtn1['state'] = tk.DISABLED
    
  def onclick2(self):
    #print(self.cbtn2.config()["text"][-1])
    if self.check2.get():
      self.var2.set(self.cbtn2.config()["text"][-1])
      self.quant2.set(self.quant2.get() - 1)
      self.can_send = True
    else: 
      self.var2.set("")
      self.can_send = False

    if self.quant2.get() <= 0:
      self.cbtn2['state'] = tk.DISABLED

  def onclick3(self):
    #print(self.cbtn3.config()["text"][-1])
    if self.check3.get():
      self.var3.set(self.cbtn3.config()["text"][-1])
      self.quant3.set(self.quant3.get() - 1)
      self.can_send = True
    else: 
      self.var3.set("")
      self.can_send = False

    if self.quant3.get() <= 0:
      self.cbtn3['state'] = tk.DISABLED

  def onclick4(self):
    self.counter4.set(self.counter4.get() + 1)
    #print(str(self.counter4.get()) + ' ' + self.btn4.config()["text"][-1])
    self.var4.set(str(self.counter4.get()) + ' ' + self.btn4.config()["text"][-1])
    self.quant4.set(self.quant4.get() - 1)
    self.can_send = True

    if self.quant4.get() <= 0:
      self.btn4['state'] = tk.DISABLED

  def onclick5(self): 
    self.counter5.set(self.counter5.get() + 1)
    #print(str(self.counter5.get()) + ' ' + self.btn5.config()["text"][-1])
    self.var5.set(str(self.counter5.get()) + ' ' + self.btn5.config()["text"][-1])
    self.quant5.set(self.quant5.get() - 1)
    self.can_send = True

    if self.quant5.get() <= 0:
      self.btn5['state'] = tk.DISABLED
  
  def onclick6(self):
    self.counter6.set(self.counter6.get() + 1)
    #print(str(self.counter6.get()) + ' ' + self.btn6.config()["text"][-1])
    self.var6.set(str(self.counter6.get()) + ' ' + self.btn6.config()["text"][-1])
    self.quant6.set(self.quant6.get() - 1)
    self.can_send = True

    if self.quant6.get() <= 0:
      self.btn6['state'] = tk.DISABLED
  
  def onclick7(self): 
    self.counter7.set(self.counter7.get() + 1)
    #print(str(self.counter7.get()) + ' ' + self.btn7.config()["text"][-1])
    self.var7.set(str(self.counter7.get()) + ' ' + self.btn7.config()["text"][-1])
    self.quant7.set(self.quant7.get() - 1)
    self.can_send = True

    if self.quant7.get() <= 0:
      self.btn7['state'] = tk.DISABLED
  
  def onclick8(self): 
    self.counter8.set(self.counter8.get() + 1)
    #print(str(self.counter8.get()) + ' ' + self.btn8.config()["text"][-1])
    self.var8.set(str(self.counter8.get()) + ' ' + self.btn8.config()["text"][-1])
    self.quant8.set(self.quant8.get() - 1)
    self.can_send = True

    if self.quant8.get() <= 0:
      self.btn8['state'] = tk.DISABLED

  def onclick9(self): 
    self.counter9.set(self.counter9.get() + 1)
    #print(str(self.counter9.get()) + ' ' + self.btn9.config()["text"][-1])
    self.var9.set(str(self.counter9.get()) + ' ' + self.btn9.config()["text"][-1])
    self.quant9.set(self.quant9.get() - 1)
    self.can_send = True

    if self.quant9.get() <= 0:
      self.btn9['state'] = tk.DISABLED

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
  
  def change_all_last6_btn_state(self, normal=True):
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
    self.var1.set("")
    self.var2.set("")
    self.var3.set("")
    self.var4.set("")
    self.var5.set("")
    self.var6.set("")
    self.var7.set("")
    self.var8.set("")
    self.var9.set("")

  def send_pizza(self):
    if self.can_send:
      tmp = [x for x in (self.var1.get(), self.var2.get(), self.var3.get(), self.var4.get(), self.var5.get(), 
                         self.var6.get(), self.var7.get(), self.var8.get(), self.var9.get()) if len(x) > 0]
      
      self.pizza.create(base=tmp[0], ingredients=tmp[1:])
      self.oven.add(self.pizza)

      self.count_score += self.pizza == self.ph
      self.count_score += self.pizza == self.pr
      self.count_score += self.pizza == self.pp
      self.score.set(f"Score: {self.count_score}")

      self.pcount_oven.set(self.oven.quant())
      self.var_status_info.set(str(self.pcount_oven.get()) + self.info)

    else: self.var_status_info.set("Vous n'avez composé aucune pizza")

    if self.pcount_oven.get() == 3:
      self.btn_send_pizza['state'] = tk.DISABLED
    else: self.btn_send_pizza['state'] = tk.NORMAL

    self.reset_counter()
  
  def start(self):
    if not self.oven.is_empty():
      self.var_status_info.set(str(self.pcount_oven.get()) + self.info + "0%")
      self.bar()
    else: self.var_status_info.set("Aucune" + self.info)
    
    self.change_all_btn_state(normal=False)     

    self.change_all_btn_state()
    self.reset_counter()
    self.oven.clean()
    self.pbar['value'] = 0

  def game_over(self):
    self.change_all_btn_state(normal=False)
    self.btn_send_pizza['state'] = tk.DISABLED
    self.btn_start['state'] = tk.DISABLED
    btotal = self.quant1.get() + self.quant2.get() + self.quant3.get()
    itotal = self.quant4.get() + self.quant5.get() + self.quant6.get() + \
             self.quant7.get() + self.quant8.get() + self.quant9.get()
    self.count_score += self.final_score(btotal, 0)
    self.count_score += self.final_score(itotal, 1)
    self.score.set(f"Score: {self.count_score}")
    self.var_status_info.set(f"Fin du jeu, Score final: {self.count_score}")

  def final_score(self, total, id):
    if id == 0:
      return -4 * total 
    elif id == 1:
      return -1 * total
    else: return 0

  def bar(self):
    self.pbar['value'] = 20
    self.var_status_info.set(str(self.pcount_oven.get()) + self.info1 + str(20) + "%")
    self.update_idletasks()
    #time.sleep(1)
    self.oven.is_done()
  
    self.pbar['value'] = 40
    self.var_status_info.set(str(self.pcount_oven.get()) + self.info1 + str(40) + "%")
    self.update_idletasks()
    #time.sleep(1)
    self.oven.is_done()

    self.pbar['value'] = 50
    self.var_status_info.set(str(self.pcount_oven.get()) + self.info1 + str(50) + "%")
    self.update_idletasks()
    #time.sleep(1)
    self.oven.is_done()
  
    self.pbar['value'] = 60
    self.var_status_info.set(str(self.pcount_oven.get()) + self.info1 + str(60) + "%")
    self.update_idletasks()
    #time.sleep(1)
    self.oven.is_done()
  
    self.pbar['value'] = 80
    self.var_status_info.set(str(self.pcount_oven.get()) + self.info1 + str(80) + "%")
    self.update_idletasks()
    #time.sleep(1)
    self.oven.is_done()

    self.pbar['value'] = 100
    self.var_status_info.set(str(self.pcount_oven.get()) + self.info1 + str(100) + "%")
    self.update_idletasks()
    #time.sleep(1)
    self.oven.is_done()
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