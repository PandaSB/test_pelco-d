#!/bin/python
import tkinter as tk
import serial.tools.list_ports
import serial



root = tk.Tk()
choices = ['']
IsConnected = False

           
var = tk.StringVar(root)
ports = list(serial.tools.list_ports.comports())

LabelStatus = tk.Label(root,text="init")
LabelStatus.grid(row=3, column=0)


def refresh():
    # Reset var and delete all old options
    var.set('')
    new_choices = [] 
    network_select['menu'].delete(0, 'end')
    ports = list(serial.tools.list_ports.comports())

    # Insert list of new options (tk._setit hooks them up to var)
    for p in ports:
        new_choices.append (p.device)
    for choice in new_choices:
        network_select['menu'].add_command(label=choice, command=tk._setit(var, choice))
    var.set(new_choices[0] )

def connect():
    global ser 
    ser = serial.Serial(port=var.get(), baudrate=9600,timeout=10) 
    if ser.isOpen():
        print ( ser.name + " is open…")
        print ( ser.get_settings())
        LabelStatus.config(text="connect")
    else :
        LabelStatus.config(text="not connected")
    return (0)

network_select = tk.OptionMenu(root, var, *choices)
network_select.grid(row=0, column=0)

# I made this quick refresh button to demonstrate
BtRefresh = tk.Button(root, text='Refresh', command=refresh)
BtRefresh.grid(row=0, column=1)
BtConnect = tk.Button(root, text='Connect', command=connect)
BtConnect.grid(row=0, column=2)

def cmdleft():
    command = b'\xFF\x01\x00\x04\x3F\x00\x44'
    ser.write(command)
    LabelStatus.config(text = "send left")
def cmdright():
    command = b'\xFF\x01\x00\x02\x3F\x00\x42'
    ser.write(command)
    LabelStatus.config(text = "send right")
def cmdup():
    command = b'\xFF\x01\x00\x08\x00\x3F\x48'
    ser.write(command)
    LabelStatus.config(text = "send uo")
def cmddown():
    command = b'\xFF\x01\x00\x10\x00\x3F\x50'
    ser.write(command)
    LabelStatus.config(text = "send down")
def cmdupleft():
    command = b'\xFF\x01\x00\x0c\x3F\x3F\x8b'
    ser.write(command)
    LabelStatus.config(text = "send cmd up left")
def cmdupright():
    command = b'\xFF\x01\x00\x0a\x3F\x3F\x89'
    ser.write(command)
    LabelStatus.config(text = "send cmd up right")
def cmddownleft():
    command = b'\xFF\x01\x00\x14\x3F\x3F\x93'
    ser.write(command)
    LabelStatus.config(text = "send cmd up right")
def cmddownright():
    command = b'\xFF\x01\x00\x12\x3F\x3F\x91a'
    ser.write(command)
    LabelStatus.config(text = "send cmd up right")
def cmdstop():
    command = b'\xFF\x01\x00\x00\x00\x00\x01'
    ser.write(command)
    LabelStatus.config(text = "send cmd stop")

BtCmd1 = tk.Button(root, text='Left', command=cmdleft)
BtCmd1.grid(row=3, column=3)
BtCmd2 = tk.Button(root, text='Right', command=cmdright)
BtCmd2.grid(row=3, column=5)
BtCmd3 = tk.Button(root, text='Up', command=cmdup)
BtCmd3.grid(row=2, column=4)
BtCmd4 = tk.Button(root, text='Down', command=cmddown)
BtCmd4.grid(row=4, column=4)
BtCmd5 = tk.Button(root, text='Stop', command=cmdstop)
BtCmd5.grid(row=3, column=4)
BtCmd6 = tk.Button(root, text='UpLeft', command=cmdupleft)
BtCmd6.grid(row=2, column=3)
BtCmd7 = tk.Button(root, text='UpRight', command=cmdupright)
BtCmd7.grid(row=2, column=5)
BtCmd8 = tk.Button(root, text='DownLeft', command=cmddownleft)
BtCmd8.grid(row=4, column=3)
BtCmd9 = tk.Button(root, text='downRight', command=cmddownright)
BtCmd9.grid(row=4, column=5)

refresh()

root.mainloop()