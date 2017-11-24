# coding:utf-8
'''
 日 期： 2017年7月28日
#--接收mainCeSi传来的列表,创建窗口，进行破解(mySql) 
@作者: 张天赠
'''
from tkinter import *
import tkinter.messagebox
import pymysql
import threading
import time
class PoJie:
    def __init__(self,list1):
        "初始化函数，账号字典，密码字典"
        
        self.BtnCount =0
        self.root =Tk()
        self.root.geometry("300x300")
        self.root.title("MySql破解")
        
        
        self.Lbox =Listbox(self.root,width="40")
        self.Lbox.grid(row =1,column=0)
        self.Lbox.insert(END,"查询中......")
        
        self.btn =Button(self.root,text="开始破解",command=self.XianCheng)
        self.btn.grid(row =0,column =0)
        
        self.list1 =list1
        #线程
        
        self.root.mainloop()
        
    def XianCheng(self):
        self.btn["text"]="破解中"
        self.th=threading.Thread(target=self.PoJieChangShi,args=())  
        self.th.setDaemon(True)#守护线程  
        self.th.start() 
          
    def ObjChuShiHua(self):
        self.myObj =[]
        for line in self.list1:
            file1 =open(line,"r",errors="ignore")
            self.myObj.append(file1)
         
     
    def LianJieMySql(self,word):
        try:
            db =pymysql.connect("localhost","root",word) 
            db.close()
            return True
        except:
            return False
            
    def PoJieChangShi(self):
        self.ObjChuShiHua()
        for line in self.myObj:
            while True:
                mystr=line.readline()
                if not mystr:
                    break
               
                if self.LianJieMySql(mystr):
                    self.Lbox.insert(END,"密码正确"+mystr)
                    tkinter.messagebox.showinfo(title="密码破解成功", message="密码正确:"+mystr)
                    print("密码正确----",mystr)
                    
                    
                    self.btn["text"]="开始破解"
                    self.th._stop()
                    break
                else :
                    self.Lbox.insert(END,"密码错误"+mystr)
                    print("密码错误",mystr)
                time.sleep(5)
        self.btn["text"]="开始破解"
        self.th._stop()
    def __del__(self):
        for line in self.myObj:
            line.close()
        pass

