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
LabelStatus.grid(row=5, column=0,  columnspan=6)


def refresh():
    # Reset var and delete all old options
    var.set('')
    new_choices = [] 
    serial_selected['menu'].delete(0, 'end')
    ports = list(serial.tools.list_ports.comports())

    # Insert list of new options (tk._setit hooks them up to var)
    for p in ports:
        new_choices.append (p.device)
    for choice in new_choices:
        serial_selected['menu'].add_command(label=choice, command=tk._setit(var, choice))
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

serial_selected = tk.OptionMenu(root, var, *choices)
serial_selected.grid(row=0, column=0)

tk.Label(root,text="Id :").grid(row=1,column=0)
Id = tk.Entry(root)
Id.grid(row=1,column=1)
Id.insert(0,"1");

# I made this quick refresh button to demonstrate
BtRefresh = tk.Button(root, text='Refresh', command=refresh)
BtRefresh.grid(row=0, column=1)
BtConnect = tk.Button(root, text='Connect', command=connect)
BtConnect.grid(row=0, column=2)

def checksum(data):
	checksum = 0 ; 
	for p in range (1,6):
		checksum += data[p]
	checksum &= 255
	return (checksum)

def cmdleft():
    command = bytearray(b'\xFF\x01\x00\x04\x3F\x00\x44')
    command[1]= int(Id.get())
    if (len(command) <= 6):
	    command.extend (b'\x00') 
    command[6] = checksum (command)
    ser.write(command)
    LabelStatus.config(text = "send left")
def cmdright():
    command = bytearray(b'\xFF\x01\x00\x02\x3F\x00\x42')
    command[1]= int(Id.get())
    if (len(command) <= 6):
	    command.extend (b'\x00') 
    command[6] = checksum (command)
    ser.write(command)
    LabelStatus.config(text = "send right")
def cmdup():
    command = bytearray(b'\xFF\x01\x00\x08\x00\x3F\x48')
    command[1]= int(Id.get())
    if (len(command) <= 6):
	    command.extend (b'\x00') 
    command[6] = checksum (command)
    ser.write(command)
    LabelStatus.config(text = "send uo")
def cmddown():
    command = bytearray(b'\xFF\x01\x00\x10\x00\x3F\x50')
    command[1]= int(Id.get())
    if (len(command) <= 6):
	    command.extend (b'\x00') 
    command[6] = checksum (command)
    ser.write(command)
    LabelStatus.config(text = "send down")
def cmdupleft():
    command = bytearray(b'\xFF\x01\x00\x0c\x3F\x3F\x8b')
    command[1]= int(Id.get())
    if (len(command) <= 6):
	    command.extend (b'\x00') 
    command[6] = checksum (command)
    ser.write(command)
    LabelStatus.config(text = "send cmd up left")
def cmdupright():
    command = bytearray(b'\xFF\x01\x00\x0a\x3F\x3F\x89')
    command[1]= int(Id.get())
    if (len(command) <= 6):
	    command.extend (b'\x00') 
    command[6] = checksum (command)
    ser.write(command)
    LabelStatus.config(text = "send cmd up right")
def cmddownleft():
    command = bytearray(b'\xFF\x01\x00\x14\x3F\x3F\x93')
    command[1]= int(Id.get())
    if (len(command) <= 6):
	    command.extend (b'\x00') 
    command[6] = checksum (command)
    ser.write(command)
    LabelStatus.config(text = "send cmd up right")
def cmddownright():
    command = bytearray(b'\xFF\x01\x00\x12\x3F\x3F\x91a')
    command[1]= int(Id.get())
    if (len(command) <= 6):
	    command.extend (b'\x00') 
    command[6] = checksum (command)
    ser.write(command)
    LabelStatus.config(text = "send cmd up right")
def cmdstop():
    command = bytearray(b'\xFF\x01\x00\x00\x00\x00\x01')
    command[1]= int(Id.get())
    if (len(command) <= 6):
	    command.extend (b'\x00') 
    command[6] = checksum (command)
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