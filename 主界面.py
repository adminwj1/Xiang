import xlrd
from tkinter import *
import pymysql
import threading
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import time


class SearchInformation(object):
    # 界面功能
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1220x700")
        self.root.title("小王信息查询工具")
        self.root.resizable(width=False, height=False)
        # 创建菜单条
        menubar = Menu(self.root)
        # 创建绑定变量
        self.vLang = StringVar()
        # tearoff=0 防止选项弹出界面窗口
        filemenu = Menu(menubar, tearoff=0)
        for k in ['打开文件', '导出数据', '连接数据库']:
            # 触发函数，获取事件值
            filemenu.add_radiobutton(label=k, command=self.OpenFile, variable=self.vLang)

        # 显示在菜单上
        menubar.add_cascade(label='菜单', menu=filemenu)
        self.root['menu'] = menubar
        # 创建一个进度条
        self.v = StringVar()
        self.label = Label(self.root, font=(', 10'))
        self.label.place(x=0, y=0)

        # 右侧信息输出框

        self.RightInfotext = Text(self.root, font=(', 12'))
        self.RightInfotext.place(x=550, y=50, height=630)
        self.scroll = Scrollbar()
        self.scroll.pack(side=RIGHT, fill=Y)
        self.scroll.config(command=self.RightInfotext.yview)
        self.RightInfotext.config(yscrollcommand=self.scroll.set)


        # 边框样式
        self.backgrpund = Label(self.root)
        self.backgrpund.place(x=10, y=50, width=540, height=630)

        # 查询选项
        """全查和单查"""
        self.inquire = Label(self.root, text='查询功能区', font=(', 20'), bg='green')
        self.inquire.place(x=0, y=50, width=550)

        """标签选项"""
        # 分隔标签
        self.TopInquireLable01 = Label(self.root, bg='white')
        self.TopInquireLable01.place(x=0, y=90, width=550, height=2)

        self.BottomInquireLable = Label(self.root, bg='white')
        self.BottomInquireLable.place(x=0, y=560, width=550, height=2)

        # 选项标签
        self.nameLabel = Label(self.root, text='选择查询方式：')
        self.nameLabel.place(x=310, y=420)

        self.cv = StringVar()
        self.com = ttk.Combobox(self.root, textvariable=self.cv, width=13)
        self.com['value'] = ('name', 'country', 'area', 'gender', 'native', 'identity', 'nation', 'alias', 'stature',
                             'bloodtype', 'speciality', 'occupation', 'remark', 'formername', 'birth', 'marriage',
                             'politics', 'religion', 'militaryservice', 'education', 'speciality', 'permanent', 'property',
                             'phone', 'certificate', 'idnumber', 'birthplace')
        self.com.current(0)
        self.com.place(x=399, y=421)

        # 查询
        # 两个字
        # Name  姓名
        self.nameLabel = Label(self.root, text='姓名：', font=(', 11'))
        self.nameLabel.place(x=0, y=98)
        self.nameEntry = Entry(self.root)
        self.nameEntry.place(x=50, y=98)

        # country   国家
        self.CountryLabel = Label(self.root, text='国家：', font=(', 11'))
        self.CountryLabel.place(x=0, y=125)
        self.CountryEntry = Entry(self.root)
        self.CountryEntry.place(x=50, y=125)

        # area    地区
        self.AreaLabel = Label(self.root, text='地区：', font=(', 11'))
        self.AreaLabel.place(x=0, y=152)
        self.AreaEntry = Entry(self.root)
        self.AreaEntry.place(x=50, y=152)

        # gender    性别
        self.GenderLabel = Label(self.root, text='性别：', font=(', 11'))
        self.GenderLabel.place(x=0, y=178)
        self.GenderEntry = Entry(self.root)
        self.GenderEntry.place(x=50, y=178)

        # nativeplace    籍贯
        self.NativeplaceLabel = Label(self.root, text='籍贯：', font=(', 11'))
        self.NativeplaceLabel.place(x=0, y=205)
        self.NativeplaceEntry = Entry(self.root)
        self.NativeplaceEntry.place(x=50, y=205)

        # identity  身份
        self.IdentityLabel = Label(self.root, text='身份：', font=(', 11'))
        self.IdentityLabel.place(x=0, y=232)
        self.IdentityEntry = Entry(self.root)
        self.IdentityEntry.place(x=50, y=232)

        # nation  民族
        self.NationLabel = Label(self.root, text='民族：', font=(', 11'))
        self.NationLabel.place(x=0, y=259)
        self.NationEntry = Entry(self.root)
        self.NationEntry.place(x=50, y=259)

        # alias  别名
        self.AliasLabel = Label(self.root, text='别名：', font=(', 11'))
        self.AliasLabel.place(x=0, y=286)
        self.AliasEntry = Entry(self.root)
        self.AliasEntry.place(x=50, y=286)

        # stature  身高
        self.StatureLabel = Label(self.root, text='身高：', font=(', 11'))
        self.StatureLabel.place(x=0, y=313)
        self.StatureEntry = Entry(self.root)
        self.StatureEntry.place(x=50, y=313)

        # bloodtype  血型
        self.BloodtypeLabel = Label(self.root, text='血型：', font=(', 11'))
        self.BloodtypeLabel.place(x=0, y=340)
        self.BloodtypeEntry = Entry(self.root)
        self.BloodtypeEntry.place(x=50, y=340)

        # speciality  专长
        self.SpecialityLabel = Label(self.root, text='专长：', font=(', 11'))
        self.SpecialityLabel.place(x=0, y=367)
        self.SpecialityEntry = Entry(self.root)
        self.SpecialityEntry.place(x=50, y=367)

        # occupation  职业
        self.OccupationLabel = Label(self.root, text='职业：', font=(', 11'))
        self.OccupationLabel.place(x=0, y=394)
        self.OccupationEntry = Entry(self.root)
        self.OccupationEntry.place(x=50, y=394)

        # remark  备注
        self.RemarkLabel = Label(self.root, text='备注：', font=(', 11'))
        self.RemarkLabel.place(x=0, y=421)
        self.RemarkEntry = Entry(self.root)
        self.RemarkEntry.place(x=50, y=421)


        # 三个字
        # former name   曾用名
        self.FormerNameLabel = Label(self.root, text='曾用名：', font=(', 11'))
        self.FormerNameLabel.place(x=0, y=448)
        self.FormerNameEntry = Entry(self.root)
        self.FormerNameEntry.place(x=60, y=448)

        # birth     出身地
        self.BirthLabel = Label(self.root, text='出身地：', font=(', 11'))
        self.BirthLabel.place(x=0, y=475)
        self.BirthEntry = Entry(self.root)
        self.BirthEntry.place(x=60, y=475)

        # 四个字
        # marriage  婚姻状态
        self.MarriageLabel = Label(self.root, text='婚姻状态：', font=(', 11'))
        self.MarriageLabel.place(x=320, y=98)
        self.MarriageEntry = Entry(self.root)
        self.MarriageEntry.place(x=398, y=98)

        # politics  政治面貌
        self.PoliticsLabel = Label(self.root, text='政治面貌：', font=(', 11'))
        self.PoliticsLabel.place(x=320, y=125)
        self.PoliticsEntry = Entry(self.root)
        self.PoliticsEntry.place(x=398, y=125)

        # religion  宗教信仰
        self.ReligionLabel = Label(self.root, text='宗教信仰：', font=(', 11'))
        self.ReligionLabel.place(x=320, y=152)
        self.ReligionEntry = Entry(self.root)
        self.ReligionEntry.place(x=398, y=152)

        # militaryservice   兵役情况
        self.ReligionLabel = Label(self.root, text='兵役情况：', font=(', 11'))
        self.ReligionLabel.place(x=320, y=178)
        self.ReligionEntry = Entry(self.root)
        self.ReligionEntry.place(x=398, y=178)

        # education 教育程度
        self.EducationLabel = Label(self.root, text='教育程度：', font=(', 11'))
        self.EducationLabel.place(x=320, y=205)
        self.EducationEntry = Entry(self.root)
        self.EducationEntry.place(x=398, y=205)

        # personnelspecialty    人员特长
        self.personnelspecialtyLabel = Label(self.root, text='人员特长：', font=(', 11'))
        self.personnelspecialtyLabel.place(x=320, y=232)
        self.personnelspecialtyEntry = Entry(self.root)
        self.personnelspecialtyEntry.place(x=398, y=232)

        # permanent 户籍地址
        self.PermanentLabel = Label(self.root, text='户籍地址：', font=(', 11'))
        self.PermanentLabel.place(x=320, y=259)
        self.PermanentEntry = Entry(self.root)
        self.PermanentEntry.place(x=398, y=259)

        # property  人员属性
        self.PropertyLabel = Label(self.root, text='人员属性：', font=(', 11'))
        self.PropertyLabel.place(x=320, y=286)
        self.PropertyEntry = Entry(self.root)
        self.PropertyEntry.place(x=398, y=286)

        # phone 联系电话
        self.PhoneLabel = Label(self.root, text='联系电话：', font=(', 11'))
        self.PhoneLabel.place(x=320, y=313)
        self.PhoneEntry = Entry(self.root)
        self.PhoneEntry.place(x=398, y=313)

        # certificate   证件类型
        self.CertificateLabel = Label(self.root, text='证件类型：', font=(', 11'))
        self.CertificateLabel.place(x=320, y=340)
        self.CertificateEntry = Entry(self.root)
        self.CertificateEntry.place(x=398, y=340)

        # ID Number 证件号码
        self.IDNumberLabel = Label(self.root, text='证件号码：', font=(', 11'))
        self.IDNumberLabel.place(x=320, y=367)
        self.IDNumberEntry = Entry(self.root)
        self.IDNumberEntry.place(x=398, y=367)

        # birthplace    出生日期
        self.BirthplaceLabel = Label(self.root, text='出生日期：', font=(', 11'))
        self.BirthplaceLabel.place(x=320, y=394)
        self.BirthplaceEntry = Entry(self.root)
        self.BirthplaceEntry.place(x=398, y=394)

        # 选项查询按钮
        self.InquireButton = Button(self.root, text='查询', font=(', 15'), command=self.OptionInsert)
        self.InquireButton.place(x=348, y=520, width=200)

        # 清除按钮
        self.clearButton = Button(self.root, text='清除', font=(', 15'), command=self.clear)
        self.clearButton.place(x=0, y=520, width=200)

        # 全部查询
        self.OneClickQuerylabel = Label(self.root, text='查询所有数据', font=(', 15'))
        self.OneClickQuerylabel.place(x=400, y=570)

        self.OneClickQuery = Button(self.root, text='一键查询', command=self.OneClickQuery)
        self.OneClickQuery.place(x=348, y=600, width=200, height=50)

        self.root.mainloop()

    # 逻辑实现
    def OpenFile(self):
        """打开文件方法"""
        Information = self.vLang.get()      # 绑定变量函数
        if Information == "打开文件":
            print("你选择了打开文件")
            self.insert()

        else:
            messagebox.showinfo(title='文件导出！', message="导出功能暂未开发！！")

    def insert(self):
        """数据插入"""
        self.file = filedialog.askopenfilename()
        print(self.file)    # 显示文件存放地址（绝对地址）
        data = xlrd.open_workbook(self.file)
        print(data)
        table = data.sheet_by_index(0)
        print(table)
        self.dataList = []
        self.num = 0
        for rowNum in range(table.nrows):  # 总行数
            rowVale = table.row_values(rowNum)  # 整行值
            for colNum in range(table.ncols):  # 总列数
                # print(table.ncols)
                if rowNum > 0 and colNum == 0:
                    # 此次可能有bug，后期测试修改
                    datarowVale = rowVale[0] + ','
                    print("这个数是：", rowVale[26])
                    dataRowVale = ','.join(rowVale[1:])
                    InsertData = datarowVale + dataRowVale  # 插入信息
                    # 将其装换为list，用于插入数据库中
                    self.dataSql = InsertData.split(',')
                    # 在界面中显示正在插入条数
                    self.num += 1
                    self.label["text"] ="正在插入第"+str(self.num)+"条数据"
                    self.label.update()
                    time.sleep(0.01)
                    # 存入数据库
                    print(self.dataSql)
                    self.depositSql()
        messagebox.showinfo(title="插入模块", message="插入完成！！！")

    def OptionInsert(self):
        """选项查询"""
        # self.option = self.cv.get()     # 这里是获取下拉列表类容
        # if self.option == 'idnumber':
        #     idnumber = self.idnumberEntry.get()
        #     # 验证用户输入的身份证号码是否违规
        #     if len(idnumber) != 18:
        #         messagebox.showinfo(title='错误！', message='你输入的证件号码不足18位！')
        #     elif idnumber.isdigit() or idnumber[-1] == 'x' or idnumber[-1] == 'X':
        #         # 操作数据库进行查询
        #         self.SQL(idnumber)
        #     else:
        #         messagebox.showinfo(title='错误！', message='你输入的证件号码有误请重新输入！')
        # elif self.option == 'name':
        #     name = self.nameEntry.get()
        #     self.SQL(name)
        #
        # else:
        #     messagebox.showinfo(title='错误！', message="你可以选择或输入有误！！")
        option = self.cv.get()     # 这里是获取下拉列表类容
        self.Option(option)


    def Option(self, option):
        """选项判断"""
        # print(option)
        if option == 'name':
            name = self.nameEntry.get()
            self.SQL(option, name)

        elif option == 'country':
            country = self.CountryEntry.get()
            self.SQL(option, country)
        elif option == 'area':
            area = self.AreaEntry.get()
            self.SQL(option, area)
        elif option == 'gender':
            gender = self.GenderEntry.get()
            self.SQL(option, gender)
        elif option == 'nativeplace':
            nativeplace = self.NativeplaceEntry.get()
            self.SQL(option, nativeplace)
        elif option == 'identity':
            identity = self.IdentityEntry.get()
            self.SQL(option, identity)
        elif option == 'alias':
            alias = self.AliasEntry.get()
            self.SQL(option, alias)
        elif option == 'stature':
            stature = self.StatureEntry.get()
            self.SQL(option, stature)
        elif option == 'bloodtype':
            bloodtype = self.BloodtypeEntry.get()
            self.SQL(option, bloodtype)
        elif option == 'speciality':
            speciality = self.SpecialityEntry.get()
            self.SQL(option, speciality)
        elif option == 'occupation':
            pass
        elif option == 'formername':
            pass
        elif option == 'birth':
            pass
        elif option == 'marriage':
            pass
        elif option == 'politics':
            pass
        elif option == 'religion':
            pass
        elif option == 'militaryservice':
            pass
        elif option == 'education':
            pass
        elif option == 'personnelspecialty':
            pass
        elif option == 'permanent':
            pass
        elif option == 'property':
            pass
        elif option == 'phone':
            pass
        elif option == 'certificate':
            pass
        elif option == 'idnumber':
            pass
        elif option == 'remark':
            pass
        elif option == 'formername':
            pass


    def SQL(self, option, info):
        """选项查询操作"""
        db = pymysql.connect('127.0.0.1', 'root', 'adminwj', 'info')
        cursor = db.cursor()
        # print(option,info)
        sql = 'select * from personalinformation where %s = "%s"' % (option, info)
        cursor.execute(sql)
        db.commit()
        reslist = cursor.fetchall()
        if reslist:
            for item in reslist:
                infolist = ['姓名:', str(item[1]), '证件类别:', item[2], '证件号码:', item[3], '出生日期:', item[4], '国家:', item[5],
                            '地区:', item[6], '性别:', item[7], '籍贯:', item[8], '身份:', item[9], '曾用名:', item[10], '民族:',
                            item[11], '别名:', item[12], '婚姻状态:', item[13], '政治面貌:', item[14], '宗教信仰:', item[15], '身高:',
                            item[16], '血型:', item[17], '兵役情况:', item[18], '教育程度:', item[19], '专长:', item[20], '人员特长:',
                            item[21], '职业:', item[22], '户籍地址:', item[23], '出生地:', item[24], '人员属性:', item[25], '联系电话:',
                            item[26], '备注:', item[27]]
                strinfolist = ' '.join(infolist)
                self.RightInfotext.insert(END, strinfolist + '\n')
        else:
            messagebox.showinfo(title='查询', message='未查询到数据！！！')


    def OneClickQuery(self):
        """一键查询"""
        db = pymysql.connect('127.0.0.1', 'root', 'adminwj', 'info')
        cursor = db.cursor()
        sql = 'select * from personalinformation'
        cursor.execute(sql)
        db.commit()
        reslist = cursor.fetchall()
        for item in reslist:
            # 这里占时不能根据数据库的字段进行自动增加或减少
            infolist = ['姓名：', str(item[1]), '证件类别：', item[2], '证件号码：', item[3], '出生日期：', item[4], '国家：', item[5], '地区：', item[6]
                        , '性别：', item[7], '籍贯：', item[8], '身份：', item[9], '曾用名：', item[10], '民族：', item[11]
            , '别名：', item[12], '婚姻状态：', item[13], '政治面貌：', item[14], '宗教信仰：', item[15], '身高：', item[16],
            '血型：', item[17], '兵役情况：', item[18], '教育程度：', item[19], '专长：', item[20], '人员特长：', item[21],
            '职业：', item[22], '户籍地址：', item[23], '出生地：', item[24], '人员属性：', item[25], '联系电话：', item[26],
            '备注：', item[27]]
            strinfolist = ' '.join(infolist)

            self.RightInfotext.insert(END, strinfolist + '\n')
            self.RightInfotext.update()


    def depositSql(self):
        """插入数据库操作"""
        db = pymysql.connect('127.0.0.1', 'root', 'adminwj', 'info')
        cursor = db.cursor()
        try:
            sql ='insert into personalinformation values(0,"{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}"' \
                 ',"{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'\
                .format(self.dataSql[0], self.dataSql[1], self.dataSql[2], self.dataSql[3],
                        self.dataSql[4], self.dataSql[5], self.dataSql[6], self.dataSql[7], self.dataSql[8],
                        self.dataSql[9], self.dataSql[10], self.dataSql[11], self.dataSql[12], self.dataSql[13],
                        self.dataSql[14], self.dataSql[15], self.dataSql[16], self.dataSql[17],
                        self.dataSql[18], self.dataSql[19], self.dataSql[20], self.dataSql[21], self.dataSql[22],
                        self.dataSql[23], self.dataSql[24], self.dataSql[25], self.dataSql[26])
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
            cursor.close()
            messagebox.showinfo(title="插入模块", message="插入失败！！！")
        finally:
            db.close()

    def clear(self):
        """清除"""
        self.RightInfotext.delete('0.0', END)
        self.RightInfotext.update()





if __name__ == '__main__':
    searchinformation = SearchInformation()