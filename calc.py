from tkinter import *
import math
from pygame import mixer
import speech_recognition


mixer.init()

def click(value):
    ex = entryField.get()  # 789 ex=ex[0:len(ex)-1]
    answer=''
    try:
        if value=='C':
            ex=ex[0:len(ex)-1]  #78
            entryField.delete(0,END)
            entryField.insert(0,ex)
        elif value=='CE':
            entryField.delete(0,END)

        elif value=='√':
            answer=math.sqrt(eval(ex))

        elif value=='π':
            answer=math.pi

        elif value=='cosθ':
            answer=math.cos(math.radians(eval(ex)))
        elif value=='sinθ':
            answer=math.sin(math.radians(eval(ex)))
        elif value=='tanθ':
            answer=math.tan(math.radians(eval(ex)))
        elif value=='2π':
            answer=2*math.pi
        elif value == 'cosh':
            answer=math.cosh(math.radians(eval(ex)))
        elif value=='sinh':
            answer=math.sinh(math.radians(eval(ex)))
        elif value=='tanh':
            answer=math.tanh(math.radians(eval(ex)))

        elif value == chr(8731):
            answer=eval(ex)**(1/3)
        elif value == 'x\u02b8': #7**2
            entryField.insert(END,'**')
            return
        elif value == 'x\u00B3':
            answer=eval(ex)**3
        elif value == 'x\u00B2':
            answer=eval(ex)**2
        elif value == 'ln':
            answer=math.log2(eval(ex))
        elif value == 'deg':
            answer=math.degrees(eval(ex))
        elif value == 'rad':
            answer=math.radians(eval(ex))
        elif value == 'log':
            answer=math.log10(eval(ex))
        elif value == 'x!':
            answer=math.factorial(ex)
        elif value==chr(247): #7/2=3.5 that mean this is devision button work
            entryField.insert(END,"/")
            return
        elif value=='=':
            answer=eval(ex)
        else:
            entryField.insert(END,value)
            return
        entryField.delete(0,END)
        entryField.insert(0,answer)
    except SyntaxError:
        pass

def add(a,b):
    return a+b

def sub(a,b):
    return a-b
def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b

def lcm(a,b):
    l=math.lcm(a,b)
    return l
def hcf(a,b):
    h=math.gcd(a,b)
    return h

operations={'ADD':add,'ADDITION':add,'SUM':add,'PLUS'
            'SUBTICRATION':sub, 'DIFFERENCE':sub ,'MINUS':sub,' SUBTRACT':sub,
            'PRODUCT':mul,' MULTIPLICATION':mul,' MULTIPLY':mul,
            'DIVISION':div,'DIV':div,'DIVIDE':div,
            'LCM':lcm, 'HCF':hcf,
            'MOD':mod,'REMINDER':mod,'MODULUS':mod}

def findNumbers(t):
    l=[]
    for num in t:
        try:
            l.append(int(num))
        except ValueError:
            pass
    return l
def audio():
    mixer.music.load('music1.mp3')
    mixer.music.play()
    sr=speech_recognition.Recognizer()
    with speech_recognition.Microphone()as m:
        try:
            sr.adjust_for_ambient_noise(m,duration=0.2)
            voice=sr.listen(m)
            text=sr.recognize_google(voice)

            mixer.music.load('music2.mp3')
            mixer.music.play()
            text_list=text.split(' ')
            for word in text_list:
                if word.upper()in operations.keys():
                    l=findNumbers(text_list)
                    print(l)
                    result=operations[word.upper()](l[0],l[1])
                    entryField.delete(0,END)
                    entryField.insert(END,result)
                else:
                    pass

        except:
            pass

root=Tk()
root.title('Smart Calculator')
root.config(bg='dodgerblue3')
root.geometry('680x486+100+100')

logo_imagae=PhotoImage(file='logo.png')
logo_lable=Label(root,image=logo_imagae,bg='dodgerblue3')
logo_lable.grid(row=0,column=0)

entryField=Entry(root,font=('arial',20,'bold'),bg='dodgerblue3',fg='white',border=10,relief=SUNKEN,width=30)
entryField.grid(row=0,column=0,columnspan=8)

mice_imagae=PhotoImage(file='microphone.png')
mic_Button=Button(root,image=mice_imagae,bd=0, bg='dodgerblue3'
                  ,command=audio)
mic_Button.grid(row=0,column=7)

button_text_list=["C", "CE", "√", "+", "π", "cosθ", "sinθ", "tanθ",
                  "1", "2", "3", "-", "2π", "cosh", "sinh", "tanh",
                  "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2" ,
                  "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                  "0", ".", "%", "=", "log", "(", ")", "x!"]


row_value=1
column_value=0
for i in button_text_list:
    button=Button(root,width=5,height=2,bd=2,relief=SUNKEN,text=i,bg='dodgerblue3',fg='white',
                  font=('arial',18,'bold',),activebackground='dodgerblue3' ,command=lambda button=i: click(button))
    button.grid(row=row_value,column=column_value,pady=1)
    column_value+=1
    if column_value>7:
        row_value+=1
        column_value=0

root.mainloop()