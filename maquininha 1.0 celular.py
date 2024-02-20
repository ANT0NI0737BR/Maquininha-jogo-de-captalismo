import PySimpleGUI as sg
import time
jog=[15000,15000,15000,15000]
reset=[15000,15000,15000,15000]
v=""

def delet():
    v=""
    
op=[
[sg.Button("RESET",key=("res"),size=(40,3))]
]

numpad=[
[sg.Button("7",key=("7"),size=(8,3)),sg.Button("8",key=("8"),size=(8,3)),sg.Button("9",key=("9"),size=(8,3))],
[sg.Button("4",key=("4"),size=(8,3)),sg.Button("5",key=("5"),size=(8,3)),sg.Button("6",key=("6"),size=(8,3))],
[sg.Button("3",key=("3"),size=(8,3)),sg.Button("2",key=("2"),size=(8,3)),sg.Button("1",key=("1"),size=(8,3))],
[sg.Button("cc",key=("cc"),size=(8,3)),sg.Button("0",key=("0"),size=(8,3)),sg.Button("cc",key=("cc"),size=(8,3))],
[sg.Button("j1+",key=("j1+"),size=(5,2)),sg.Button("j2+",key=("j2+"),size=(5,2)),sg.Button("j3+",key=("j3+"),size=(5,2)),sg.Button("j4+",key=("j4+"),size=(5,2))],
[sg.Button("j1-",key=("j1-"),size=(5,2)),sg.Button("j2-",key=("j2-"),size=(5,2)),sg.Button("j3-",key=("j3-"),size=(5,2)),sg.Button("j4-",key=("j4-"),size=(5,2))]
]

layout=[
[sg.In(key=("valor"),size=(50,70))],
[sg.Frame("",op)],
[sg.Frame("",numpad)]
]

j=sg.Window("RPG MK9.1",layout,finalize=True)
j.maximize()
while True:
    #jo=[str(jog[0]),str(jog[1]),str(jog[2]),str(jog[3])]

    
    e1,e2=j.read()

    if e1 == sg.WINDOW_CLOSED:
        break

    if e1=="res":
        jog=reset
    
    if e1=="j1+":
        j["valor"].update(jog[0])
    
    if e1=="j2+":
        j["valor"].update(jog[1])
        
    if e1=="j3+":
        j["valor"].update(jog[2])
        
    if e1=="j4+":
        j["valor"].update(jog[3])
        
    if e1=="cc":
        v=""
        j["valor"].update(v)
        
    if e1=="1":
        v=v+"1"
        j["valor"].update(v)
        
    if e1=="2":
        v=v+"2"
        j["valor"].update(v)
        
    if e1=="3":
        v=v+"3"
        j["valor"].update(v)
        
    if e1=="4":
        v=v+"4"
        j["valor"].update(v)
        
    if e1=="5":
        v=v+"5"
        j["valor"].update(v)
        
    if e1=="6":
        v=v+"6"
        j["valor"].update(v)
        
    if e1=="7":
        v=v+"7"
        j["valor"].update(v)
        
    if e1=="8":
        v=v+"8"
        j["valor"].update(v)
        
    if e1=="9":
        v=v+"9"
        j["valor"].update(v)
        
    if e1=="0":
        v=v+"0"
        j["valor"].update(v)
        
    if v!="" and e1=="j1+":
        V=jog[0]+int(v)
        
        j["valor"].update(V)
        jog[0]=V
        v=""
        
    if v!="" and e1=="j1-":
        V=jog[0]-int(v)
        
        j["valor"].update(V)
        jog[0]=V
        
    #----
    
    if v!="" and e1=="j2+":
        V=jog[1]+int(v)
        
        j["valor"].update(V)
        jog[1]=V
        v=""
        
    if v!="" and e1=="j2-":
        V=jog[1]-int(v)
        
        j["valor"].update(V)
        jog[1]=V
        
    #----
    
    if v!="" and e1=="j3+":
        V=jog[2]+int(v)
        
        j["valor"].update(V)
        jog[2]=V
        v=""
        
    if v!="" and e1=="j3-":
        V=jog[2]-int(v)
        
        j["valor"].update(V)
        jog[2]=V
        
    #----
    
    if v!="" and e1=="j4+":
        V=jog[3]+int(v)
        
        j["valor"].update(V)
        jog[3]=V
        v=""
        
        
    if v!="" and e1=="j4-":
        V=jog[3]-int(v)
        
        j["valor"].update(V)
        jog[3]=V
        
        