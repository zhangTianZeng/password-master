# coding:utf-8
'''
 日 期： 2017年7月27日
 
@作者: 张天赠
#--接收MainUi(主窗口)传递过来的值(密码类型,破解对象)
#--然后分析类型对象,无论什么类型，首先获取密码类型，打开密码库，创建密码列表
#--其次根据破解对象，调用不同处理窗口(wifi,mysql,...)
'''
import wifiPassWordAll
import wifiPoJie#wifi破解类
import mySqlPoJie
#("wifi破解","MySql破解","Oracle破解","SqlServer破解")
class MainStart:
    def __init__(self):#
        
    
        pass
    def Start(self,typeValue1,pathValue2):
        self.V1=typeValue1
        self.V2=pathValue2
        self.List1 =[]
        result =wifiPassWordAll.passWordAll()
        if self.V2 =="弱口令":
            self.List1= result.ruoPassWord()
            
        elif self.V2 =="复杂口令":
            self.List1=result.QiangPassWord()
            
        elif self.V2 =="手机号":
            self.List1=result.PhonePassWord()
            
        elif self.V2 =="邮箱":
            self.List1= result.EmailPassWord()
            
        else:
            self.List1= result.AllPassWord()
            
        
        if self.V1 =="wifi破解":
            
            wifiPoJie.PoJie(self.List1)
            
        elif self.V1 =="MySql破解" :
            mySqlPoJie.PoJie(self.List1)
            pass
        
        elif self.V1 =="Oracle破解":
            
            pass
        
        else :
            
            pass


        
        

        


