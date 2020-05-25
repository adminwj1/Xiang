from tkinter import *
from tkinter import ttk
import pymysql
import threading

class Inquire(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("查询模块")
        self.root.geometry("750x500")
        self.root.resizable(width=FALSE, height=FALSE)
        self.inquire = Label(self.root, text='查询选项', font=('微软雅黑, 12'))
        self.inquire.place(x=100, y=20)
        # 绑定变量
        self.cv = StringVar()
        self.com = ttk.Combobox(self.root, textvariable=self.cv)
        self.com['value'] = ('idnumber ', 'name')
        self.com.current(1)
        self.com.place(x=170, y=20)

        self.inquireButton = Button(self.root, text='查询', command=self.inquireIncident)
        self.inquireButton.place(x=350, y=20)

        # 显示查询结果
        self.inquireResult = Text(self.root, font=('微软雅黑, 13'))
        self.inquireResult.place(x=13, y=60)
        self.root.mainloop()

    def inquireIncident(self):
        """获取下拉框事件"""
        # print(self.cv.get())
        incident = self.cv.get()
        if incident == 'name':
            self.SQL(incident)




    def SQL(self, incident):
        """查询数据库"""
        db = pymysql.connect('127.0.0.1', 'root', 'adminwj', 'info')
        cursor = db.cursor()
        sql = 'select * from test001 where name = ' + incident
        cursor.execute(sql)
        db.commit()
        reslist = cursor.fetchall()
        for item in reslist:
            infolist = ['身份证：', str(item[0]), '姓名：', item[1], '性别：', item[2], '职业：', item[3]]
            strinfolist = ' '.join(infolist)
            self.inquireResult.insert(END, strinfolist + '\n')





if __name__ == '__main__':
    inquire = Inquire()