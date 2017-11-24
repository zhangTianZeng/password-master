# coding:utf-8
'''
 日 期： 2017年7月27日
#  ----主界面-----
@作者: 张天赠
'''
from wifiPassWordAll import passWordAll
from wifiPoJie import PoJie
from tkinter import *
from tkinter.ttk import *
import mainCeShi
import time
class mainUi:
    def __init__(self):
        "初始化窗口"
        
        self.root =Tk()#初始化一个顶层窗口
        self.root.title("万能密码破解工具")#设置界面的名称标签
        self.root.geometry("300x300")#设置顶层窗体大小
        
        self.Lab1 =Label(self.root,text="选择破解对象:")
        self.Lab1.grid(row =0,column =0)
        self.textValue =StringVar()#文本变量的设置
        self.textValue2 =StringVar()
        self.differentAll =Combobox(self.root,textvariable=self.textValue)#变量值和下拉列表绑定
        self.typeSetAll =Combobox(self.root,textvariable=self.textValue2)#变量值和下拉列表绑定
        self.differentAll["values"]=("wifi破解","MySql破解","Oracle破解","SqlServer破解")
        self.differentAll.current(0)
        self.differentAll.grid(row = 0, column = 1)
        
        self.textValue2 =StringVar()
        self.Lab2 =Label(self.root,text="选择密码类库:")
        self.Lab2.grid(row =1,column =0)
        self.typeSetAll["values"]=("弱口令","复杂口令","手机号","邮箱","全部选择")
        self.typeSetAll.current(0)
        self.typeSetAll.grid(row =1,column =1)
        
        self.QuDingButton =Button(self.root,text="确定",command=self.queDing)
        self.QuDingButton.grid(row =3,columnspan=2)
        
#         self.Lbox =Listbox(self.root,width="40")
#         self.Lbox.grid(row =2,columnspan=2)
        pass
        
    def show(self):
        self.root.mainloop()
        pass
    def queDing(self):
        value1=self.differentAll.get()
        value2=self.typeSetAll.get()
        print(value1)
        print(value2)  
        main1 =mainCeShi.MainStart()
       
        main1.Start(value1,value2)
        
            
    def __del__(self):
        
        pass


if __name__ == '__main__':
    file1 =mainUi()
    file1.show()
        
    

