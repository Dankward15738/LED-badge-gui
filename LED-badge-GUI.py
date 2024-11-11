#!/usr/bin/python3
#
# TKInter-Gui for the Modul lednamebadge in the Projekt https://github.com/jnweiger/led-name-badge-ls32
#
# The MIT License (MIT)
#
# 2024  Dankward Nuerenberg
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# The Gui has to be set in the same folder as the File lednamebadge.py
#
from lednamebadge import *
from tkinter import *
from array import array
def uebertragen():
    creator = SimpleTextAndIcons()
    scene_a_bitmap = creator.bitmap(entry1.get())
    scene_b_bitmap = creator.bitmap(entry2.get())
    scene_c_bitmap = creator.bitmap(entry3.get())
    lengths = (scene_a_bitmap[1], scene_b_bitmap[1],scene_c_bitmap[1])
    buf = array('B')
    buf.extend(LedNameBadge.header(lengths,(int(entry6.get()),int(entry6.get())) , (int(entry5.get()),int(entry5.get())), (0,0,0), (0,0,1), int(entry4.get())))
    buf.extend(scene_a_bitmap[0])
    buf.extend(scene_b_bitmap[0])
    buf.extend(scene_c_bitmap[0])
    LedNameBadge.write(buf)





   
    
fenster = Tk()
fenster.title("LED-badge")
fenster.geometry("600x400")
var=IntVar()
label = Label(fenster, text = "Steuerung des LED -Panels")
label.grid(row = 1, column = 1) #Anordnung durch Grid-Manager
label = Label(fenster, text = "Text 1  auf dem Panel")
label.grid(row = 2, column = 1) #Anordnung durch Grid-Manager
label = Label(fenster, text = "Text 2  auf dem Panel")
label.grid(row = 3, column = 1) #Anordnung durch Grid-Manager
label = Label(fenster, text = "Text 3  auf dem Panel")
label.grid(row = 4, column = 1) #Anordnung durch Grid-Manager
label = Label(fenster, text = "Helligkeit")
label.grid(row = 5, column = 1) #Anordnung durch Grid-Manager
label = Label(fenster, text = "Modi(0-8)")

label.grid(row = 6, column = 1) #Anordnung durch Grid-Manager
label = Label(fenster, text = "Geschwindigkeit(0-8)")

label.grid(row = 7, column = 1) #Anordnung durch Grid-Manager
entry1 = Entry(fenster, text="",width=50,bg="white"  )
#entry1.pack()
entry1.grid(row = 2, column = 2)
entry2 = Entry(fenster, text="",width=50,bg="white"  )
#entry1.pack()
entry2.grid(row = 3, column = 2)
entry3 = Entry(fenster, text="",width=50,bg="white"  )
#entry1.pack()
entry3.grid(row = 4, column = 2)
entry4 = Entry(fenster, text="",width=5,bg="white"  )
#entry1.pack()
entry4.grid(row = 5, column = 2)
entry4.insert(0,50)
entry5 = Entry(fenster, text="",width=5,bg="white"  )
#entry1.pack()
entry5.grid(row = 6, column = 2)
entry5.insert(0,0)
entry6 = Entry(fenster, text="",width=5,bg="white"  )
entry6.grid(row = 7, column = 2)
entry6.insert(0,7)
def select():
    global var
    entry5.delete(0,"end")
    entry5.insert(0,str(var.get()))
    print(var)
R1 = Radiobutton(fenster, text="Scroll links", variable=var, value=0,command=select)
R1.grid(row = 8, column=1)
R2 = Radiobutton(fenster, text="Scroll rechts", variable=var, value=1,command=select)
R2.grid(row = 9, column=1)
R3 = Radiobutton(fenster, text="Scroll nach oben", variable=var, value=2,command=select)
R3.grid(row=10,column=1)
R4 = Radiobutton(fenster, text="Scroll nach unten", variable=var, value=3,command=select)
R4.grid(row=11,column=1)
R5 = Radiobutton(fenster, text="unbeweglich", variable=var, value=4,command=select)
R5.grid(row = 8, column=2)
R6 = Radiobutton(fenster, text="animation", variable=var, value=5,command=select)
R6.grid(row = 9, column=2)
R7 = Radiobutton(fenster, text="drop-down", variable=var, value=6,command=select)
R7.grid(row=10,column=2)
R8 = Radiobutton(fenster, text="Laser", variable=var, value=8,command=select)
R8.grid(row=11,column=2)
button1 = Button(fenster, text="Übertragen", command=uebertragen)
button1.grid(row = 12, column=1)
fenster.mainloop()
