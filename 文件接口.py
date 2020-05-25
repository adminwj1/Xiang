#   文件接口，读取txt和xlxs文件类容
import xlrd
from tkinter import *
import pymysql
import threading
from tkinter import filedialog
from tkinter import messagebox

class fileApi(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("导入模块")
        self.root.geometry("700x400")
        self.root.resizable(width=FALSE, height=False)
        self.label = Label(self.root, text="目标文件：", font=('微软雅黑,10'))
        self.label.place(x=150, y=10)

        self.Entry = Entry(self.root, font=('微软雅黑,10'))
        self.Entry.place(x=240, y=13)
        self.Button = Button(self.root, text='选择文件', command=self.SelectFile)
        self.Button.place(x=450, y=10)

        self.toLead = Button(self.root, text='导入数据', command=self.toLead)
        self.toLead.place(x=260, y=80, width=150, heigh=50)
        
        # 文本框，用于显示读取数据进度
        self.text = Text(self.root)
        self.text.place(x=70, y=160, height=200)
        scroll = Scrollbar()
        scroll.pack(side=RIGHT, fill=Y)
        scroll.config(command=self.text.yview)
        self.text.config(yscrollcommand=scroll.set)
        self.root.mainloop()

    def SelectFile(self):
        """选择需要导入的文件方法"""
        # 返回文件路径（绝对路径）
        self.file = filedialog.askopenfilename()
        # 将路径插入到单行文本中
        self.Entry.insert(0, self.file)

    def toLead(self):
        """导入excel和txt文件类容"""
        file = self.file.split('.')[-1]
        if file == 'xlsx':
            self.excel()
        elif file == 'txt':
            print('txt')
        else:
            print('未知文件格式，无发导入')

    def excel(self):
        """导入Excel文件方法"""
        '''
            测试Excel文件中只有4个字段
        '''
        data = xlrd.open_workbook(self.file)
        table = data.sheet_by_index(0)
        self.dataList = []
        for rowNum in range(table.nrows):  # 总行数
            rowVale = table.row_values(rowNum)  # 整行值
            for colNum in range(table.ncols):  # 总列数
                if rowNum > 0 and colNum == 0:
                    # print(rowVale)
                    # 此次可能有bug，后期测试修改
                    # 将输出的信息显示在文本框中
                    datarowVale = str(int(rowVale[0])) + ','
                    # print(datarowVale)
                    dataRowVale = ','.join(rowVale[1:])
                    InsertData = datarowVale + dataRowVale  # 插入信息
                    # 将其装换为list，用于插入数据库中
                    self.dataSql = InsertData.split(',')
                    # print(dataSql)
                    # 插入信息更换为进度条
                    self.text.insert(END, InsertData + '\n')
                    self.text.update()
                    # 存入数据库
                    self.depositSql()
        pp = self.dataSql[0]
        messagebox.showinfo(title="插入模块", message="插入完成！！！一共插入：" + pp + "条数据")
    def txt(self):
        """导入txt文件函数"""
        pass


    def depositSql(self):
        """数据库操作"""
        db = pymysql.connect('127.0.0.1', 'root', 'adminwj', 'info')
        cursor = db.cursor()
        try:
            sql ='insert test001 values(0,"{}","{}","{}")'.format(self.dataSql[1], self.dataSql[2], self.dataSql[3])
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
            cursor.close()
            messagebox.showinfo(title="插入模块", message="插入失败！！！")
        finally:
            db.close()
if __name__ == '__main__':
    File = fileApi()