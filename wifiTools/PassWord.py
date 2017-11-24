# coding:utf-8
'''
 日 期： 2017年7月27日
#---接收wifiPassWordAll传递过来的一个(文件路径)，返回一个打包好的(.txt)列表
@作者: 张天赠
'''

import os
import collections
class TiGongMiMa:
    def __init__(self):
        
        pass
    def AllPath(self,path):
        """深度遍历"""
        listPath =[]
        self.path =path 
        MyList =collections.deque([])
        MyList.append(self.path)
        while len(MyList) !=0:
            path =MyList.popleft()
            if os.path.isdir(path):
                myFilePath =os.listdir(path)
#                 print("文件夹",path)
                for line in myFilePath:
                    myPath =path +"\\"+line
                    MyList.append(myPath)
            else:
#                 print("文件",path)
                if path.find(".txt"):
                    
                    listPath.append(path)
        return listPath
    def ruoPath(self,path):
        self.ruoPath =path
        listPath =[]
        listPath.append(self.ruoPath)
        return listPath
        pass
    
    def QiangPath(self,path):
        self.QiangPath =path
        listPath =[]
        listPath.append(self.QiangPath)
        return listPath
        pass
    
    def PhonePath(self,path):
        self.PhonePath =path
        listPath =[]
        listPath.append(self.PhonePath)
        return listPath
        pass
    
    def EmailPath(self,path):
        self.EmailPath =path
        listPath =[]
        listPath.append(self.EmailPath)
        return listPath
        pass
        
        
    
    def __del__(self):
        pass