# coding:utf-8
'''
 日 期： 2017年7月27日
#---接收mainCeShi传递过来的一个(密码类型)，返回一个(.txt)文件列表
@作者: 张天赠
'''
from wifiTools import PassWord
class passWordAll:
    def __init__(self):
        self.ObjectType = PassWord.TiGongMiMa()
        
        pass
    def AllPassWord(self):
        self.ALLpath = r"C:\Users\Administrator\Desktop\密码"
        result=self.ObjectType.AllPath(self.ALLpath)
        return result
        pass
    def ruoPassWord(self):
        self.ruoPath =r""
        result=self.ObjectType.AllPath(self.ruoPath)
        return result
        pass
    
    def QiangPassWord(self):
        self.QiangPath =r""
        result=self.ObjectType.AllPath(self.QiangPath)
        return result
        pass
    
    def PhonePassWord(self):
        self.PhonePath =r""
        result=self.ObjectType.AllPath(self.PhonePath)
        return result
        pass
    
    def EmailPassWord(self):
        self.EmailPath =r""
        result=self.ObjectType.AllPath(self.EmailPath)
        return result
        pass
    
    def __del__(self):
        pass