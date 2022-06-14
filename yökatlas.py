from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from tkinter import*
win=Tk()
def ara():
    l2.delete(0,END)
    giris=e1.get()
    driver=webdriver.Chrome()
    url="https://yokatlas.yok.gov.tr/"
    driver.get(url)
    search_input=driver.find_element(by=By.NAME, value="search")
    time.sleep(2)
    search_input.send_keys(giris)
    time.sleep(2)
    search_input.send_keys(Keys.DOWN)
    search_input.send_keys(Keys.ENTER)
    result=driver.find_elements(by=By.CSS_SELECTOR, value=".row h4 a")
    liste=[]
    count=0
    for i in result:
        count+=1
        liste.append(f"{count}-) {i.text}")
    liste.pop()
    f=open(f"{giris}.txt","w",encoding='utf-8')
    for i in liste:
        f.write(i+"\n")
    f.close()
    for element in liste:
        #print(element.text)
        l2.insert(END,element)
win.geometry("500x500+500+200")
l1=Label(win,text="aradığınız bölüm:").place(x=30, y=10)
e1=Entry(win)
e1.place(x=140,y=10)
Button(win,text="ARA",command=ara).place(x=275,y=10)
xx=Scrollbar(win,orient=HORIZONTAL)
xx.pack(side=BOTTOM,padx=70,pady=70)
l2=Listbox(win,xscrollcommand=xx.set)
l2=Listbox(win,width=60,height=20)
l2.place(x=70, y=70)
xx.config(command=l2.xview)
mainloop()
