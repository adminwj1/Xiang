import xlrd
from tkinter import *
import pymysql
from tkinter import filedialog
from tkinter import messagebox
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
        # self.nameLabel = Label(self.root, text='选择查询方式：')
        # self.nameLabel.place(x=310, y=420)

        # self.cv = StringVar()
        # self.com = ttk.Combobox(self.root, textvariable=self.cv, width=13)
        # self.com['value'] = ('name', 'country', 'area', 'gender', 'native', 'identity', 'nation', 'alias', 'stature',
        #                      'bloodtype', 'speciality', 'occupation', 'remark', 'formername', 'birth', 'marriage',
        #                      'politics', 'religion', 'militaryservice', 'education', 'speciality', 'permanent', 'property',
        #                      'phone', 'certificate', 'idnumber', 'birthplace')
        # self.com.current(0)
        # self.com.place(x=399, y=421)

        # 查询
        # 两个字
        # Name  姓名
        self.nameLabel = Label(self.root, text='姓名', font=(', 11'))
        self.nameLabel.place(x=0, y=98)
        self.nameEntry = Entry(self.root)
        self.nameEntry.bind("<Button-1>", self.name_label)
        self.nameEntry.place(x=50, y=98)
        # self.nameLabel.bind("<Button-1>",self.p_label)

        # ticket    票号
        self.ticketidLabel = Label(self.root, text='票号', font=(', 11'))
        self.ticketidLabel.place(x=0, y=125)
        self.ticketidEntry = Entry(self.root)
        self.ticketidEntry.bind("<Button-1>", self.ticketid_label)
        self.ticketidEntry.place(x=50, y=125)

        # trainnumber    车次
        self.trainnumberLabel = Label(self.root, text='车次', font=(', 11'))
        self.trainnumberLabel.place(x=0, y=152)
        self.trainnumberEntry = Entry(self.root)
        self.trainnumberEntry.bind("<Button-1>", self.trainnumber_label)
        self.trainnumberEntry.place(x=50, y=152)

        # startingstation   发站
        self.startingstationLabel = Label(self.root, text='发站', font=(', 11'))
        self.startingstationLabel.place(x=0, y=178)
        self.startingstationEntry = Entry(self.root)
        self.startingstationEntry.bind("<Button-1>", self.startingstation_label)
        self.startingstationEntry.place(x=50, y=178)

        # destination 到站
        self.destinationLabel = Label(self.root, text='到站', font=(', 11'))
        self.destinationLabel.place(x=0, y=205)
        self.destinationEntry = Entry(self.root)
        self.destinationEntry.bind("<Button-1>", self.destination_label)
        self.destinationEntry.place(x=50, y=205)

        # Seats 席别
        self.seatsLabel = Label(self.root, text='席别', font=(', 11'))
        self.seatsLabel.place(x=0, y=232)
        self.seatsEntry = Entry(self.root)
        self.seatsEntry.bind("<Button-1>", self.seats_Label)
        self.seatsEntry.place(x=50, y=232)

        # 票种    ticket
        self.ticketLabel = Label(self.root, text='票种', font=(', 11'))
        self.ticketLabel.place(x=0, y=259)
        self.ticketEntry = Entry(self.root)
        self.ticketEntry.bind("<Button-1>",self.ticket_Label)
        self.ticketEntry.place(x=50, y=259)

        # ticketrates   票价
        self.ticketratesLabel = Label(self.root, text='票价', font=(', 11'))
        self.ticketratesLabel.place(x=0, y=286)
        self.ticketratesEntry = Entry(self.root)
        self.ticketratesEntry.bind("<Button-1>", self.ticketrates_Label)
        self.ticketratesEntry.place(x=50, y=286)

        # 窗口    window
        self.windowLabel = Label(self.root, text='窗口', font=(', 11'))
        self.windowLabel.place(x=0, y=313)
        self.windowEntry = Entry(self.root)
        self.windowEntry.bind("<Button-1>", self.window_Label)
        self.windowEntry.place(x=50, y=313)

        # 座位号   SeatNumber
        self.seatnumberLabel = Label(self.root, text='座位号', font=(', 11'))
        self.seatnumberLabel.place(x=0, y=340)
        self.seatnumberEntry = Entry(self.root)
        self.seatnumberEntry.bind("<Button-1>", self.seatnumber_Label)
        self.seatnumberEntry.place(x=60, y=340)

        # 车厢号   carriagenumber
        self.carriagenumberLabel = Label(self.root, text='车厢号', font=(', 11'))
        self.carriagenumberLabel.place(x=0, y=367)
        self.carriagenumberEntry = Entry(self.root)
        self.carriagenumberEntry.bind("<Button-1>", self.carriagenumber_Labek)
        self.carriagenumberEntry.place(x=60, y=367)


        # 操作员   operator
        self.operatorLabel = Label(self.root, text='操作员', font=(', 11'))
        self.operatorLabel.place(x=0, y=394)
        self.operatorEntry = Entry(self.root)
        self.operatorEntry.bind("<Button-1>", self.operator_Labek)
        self.operatorEntry.place(x=60, y=394)

        # certificate   证件类型
        self.certificateLabel = Label(self.root, text='证件类型', font=(', 11'))
        self.certificateLabel.place(x=320, y=98)
        self.certificateEntry = Entry(self.root)
        self.certificateEntry.bind("<Button-1>", self.certificate_label)
        self.certificateEntry.place(x=398, y=98)

        # 售票处   ticket place
        self.ticketplaceLabel = Label(self.root, text='证件类型', font=(', 11'))
        self.ticketplaceLabel.place(x=320, y=125)
        self.ticketplaceEntry = Entry(self.root)
        self.ticketplaceEntry.bind("<Button-1>", self.ticketplace_Label)
        self.ticketplaceEntry.place(x=398, y=125)

        # ID Number 证件号码
        self.idnumberLabel = Label(self.root, text='证件号码', font=(', 11'))
        self.idnumberLabel.place(x=320, y=125)
        self.idnumberEntry = Entry(self.root)
        self.idnumberEntry.bind("<Button-1>", self.idnumber_Label)
        self.idnumberEntry.place(x=398, y=125)

        # todate    乘车日期
        self.todateLabel = Label(self.root, text='乘车日期', font=(', 11'))
        self.todateLabel.place(x=320, y=152)
        self.todateEntry = Entry(self.root)
        self.todateEntry.bind("<Button-1>", self.todate_Label)
        self.todateEntry.place(x=398, y=152)

        # totime    乘车时间
        self.totimeLabel = Label(self.root, text='乘车时间', font=(', 11'))
        self.totimeLabel.place(x=320, y=179)
        self.totimeEntry = Entry(self.root)
        self.totimeEntry.bind("<Button-1>", self.totime_Label)
        self.totimeEntry.place(x=398, y=179)

        # totickettime  售票时间
        self.totickettimeLabel = Label(self.root, text='售票时间', font=(', 11'))
        self.totickettimeLabel.place(x=320, y=206)
        self.totickettimeEntry = Entry(self.root)
        self.totickettimeEntry.bind("<Button-1>", self.totickettime_Label)
        self.totickettimeEntry.place(x=398, y=206)

        # country   国家
        # self.CountryLabel = Label(self.root, text='国家：', font=(', 11'))
        # self.CountryLabel.place(x=0, y=125)
        # self.CountryEntry = Entry(self.root)
        # self.CountryEntry.place(x=50, y=125)

        # area    地区
        # self.AreaLabel = Label(self.root, text='地区：', font=(', 11'))
        # self.AreaLabel.place(x=0, y=152)
        # self.AreaEntry = Entry(self.root)
        # self.AreaEntry.place(x=50, y=152)

        # gender    性别
        # self.GenderLabel = Label(self.root, text='性别：', font=(', 11'))
        # self.GenderLabel.place(x=0, y=178)
        # self.GenderEntry = Entry(self.root)
        # self.GenderEntry.place(x=50, y=178)

        # nativeplace    籍贯
        # self.NativeplaceLabel = Label(self.root, text='籍贯：', font=(', 11'))
        # self.NativeplaceLabel.place(x=0, y=205)
        # self.NativeplaceEntry = Entry(self.root)
        # self.NativeplaceEntry.place(x=50, y=205)

        # identity  身份
        # self.IdentityLabel = Label(self.root, text='身份：', font=(', 11'))
        # self.IdentityLabel.place(x=0, y=232)
        # self.IdentityEntry = Entry(self.root)
        # self.IdentityEntry.place(x=50, y=232)

        # nation  民族
        # self.NationLabel = Label(self.root, text='民族：', font=(', 11'))
        # self.NationLabel.place(x=0, y=259)
        # self.NationEntry = Entry(self.root)
        # self.NationEntry.place(x=50, y=259)

        # alias  别名
        # self.AliasLabel = Label(self.root, text='别名：', font=(', 11'))
        # self.AliasLabel.place(x=0, y=286)
        # self.AliasEntry = Entry(self.root)
        # self.AliasEntry.place(x=50, y=286)

        # stature  身高
        # self.StatureLabel = Label(self.root, text='身高：', font=(', 11'))
        # self.StatureLabel.place(x=0, y=313)
        # self.StatureEntry = Entry(self.root)
        # self.StatureEntry.place(x=50, y=313)

        # bloodtype  血型
        # self.BloodtypeLabel = Label(self.root, text='血型：', font=(', 11'))
        # self.BloodtypeLabel.place(x=0, y=340)
        # self.BloodtypeEntry = Entry(self.root)
        # self.BloodtypeEntry.place(x=50, y=340)

        # speciality  专长
        # self.SpecialityLabel = Label(self.root, text='专长：', font=(', 11'))
        # self.SpecialityLabel.place(x=0, y=367)
        # self.SpecialityEntry = Entry(self.root)
        # self.SpecialityEntry.place(x=50, y=367)

        # occupation  职业
        # self.OccupationLabel = Label(self.root, text='职业：', font=(', 11'))
        # self.OccupationLabel.place(x=0, y=394)
        # self.OccupationEntry = Entry(self.root)
        # self.OccupationEntry.place(x=50, y=394)

        # remark  备注
        # self.RemarkLabel = Label(self.root, text='备注：', font=(', 11'))
        # self.RemarkLabel.place(x=0, y=421)
        # self.RemarkEntry = Entry(self.root)
        # self.RemarkEntry.place(x=50, y=421)


        # 三个字
        # former name   曾用名
        # self.FormerNameLabel = Label(self.root, text='曾用名：', font=(', 11'))
        # self.FormerNameLabel.place(x=0, y=448)
        # self.FormerNameEntry = Entry(self.root)
        # self.FormerNameEntry.place(x=60, y=448)

        # birthplace     出身地
        # self.BirthplaceLabel = Label(self.root, text='出身地：', font=(', 11'))
        # self.BirthplaceLabel.place(x=0, y=475)
        # self.BirthplaceEntry = Entry(self.root)
        # self.BirthplaceEntry.place(x=60, y=475)

        # 四个字
        # marriage  婚姻状态
        # self.MaritalstatusLabel = Label(self.root, text='婚姻状态：', font=(', 11'))
        # self.MaritalstatusLabel.place(x=320, y=98)
        # self.MaritalstatusEntry = Entry(self.root)
        # self.MaritalstatusEntry.place(x=398, y=98)

        # politicsstatus  政治面貌
        # self.PoliticsstatusLabel = Label(self.root, text='政治面貌：', font=(', 11'))
        # self.PoliticsstatusLabel.place(x=320, y=125)
        # self.PoliticsstatusEntry = Entry(self.root)
        # self.PoliticsstatusEntry.place(x=398, y=125)

        # faith  宗教信仰
        # self.FaithLabel = Label(self.root, text='宗教信仰：', font=(', 11'))
        # self.FaithLabel.place(x=320, y=152)
        # self.FaithEntry = Entry(self.root)
        # self.FaithEntry.place(x=398, y=152)

        # jointhearmy   兵役情况
        # self.JointhearmyLabel = Label(self.root, text='兵役情况：', font=(', 11'))
        # self.JointhearmyLabel.place(x=320, y=178)
        # self.JointhearmyEntry = Entry(self.root)
        # self.JointhearmyEntry.place(x=398, y=178)

        # educationbackground 教育程度
        # self.EducationbackgroundLabel = Label(self.root, text='教育程度：', font=(', 11'))
        # self.EducationbackgroundLabel.place(x=320, y=205)
        # self.EducationbackgroundEntry = Entry(self.root)
        # self.EducationbackgroundEntry.place(x=398, y=205)

        # personnelspecialty    人员特长
        # self.PersonnelspecialtyLabel = Label(self.root, text='人员特长：', font=(', 11'))
        # self.PersonnelspecialtyLabel.place(x=320, y=232)
        # self.PersonnelspecialtyEntry = Entry(self.root)
        # self.PersonnelspecialtyEntry.place(x=398, y=232)

        # permanent 户籍地址
        # self.PermanentLabel = Label(self.root, text='户籍地址：', font=(', 11'))
        # self.PermanentLabel.place(x=320, y=259)
        # self.PermanentEntry = Entry(self.root)
        # self.PermanentEntry.place(x=398, y=259)

        # property  人员属性
        # self.PropertyLabel = Label(self.root, text='人员属性：', font=(', 11'))
        # self.PropertyLabel.place(x=320, y=286)
        # self.PropertyEntry = Entry(self.root)
        # self.PropertyEntry.place(x=398, y=286)

        # phone 联系电话
        # self.PhoneLabel = Label(self.root, text='联系电话：', font=(', 11'))
        # self.PhoneLabel.place(x=320, y=313)
        # self.PhoneEntry = Entry(self.root)
        # self.PhoneEntry.place(x=398, y=313)



        # birthplace    出生日期
        # self.BirthplaceLabel = Label(self.root, text='出生日期：', font=(', 11'))
        # self.BirthplaceLabel.place(x=320, y=394)
        # self.BirthplaceEntry = Entry(self.root)
        # self.BirthplaceEntry.place(x=398, y=394)

        # 选项查询按钮
        self.InquireButton = Button(self.root, text='查询', font=(', 15'), command=self.OptionInsert)
        self.InquireButton.place(x=348, y=520, width=200)

        # 清除按钮
        self.clearButton = Button(self.root, text='清除', font=(', 15'), command=self.clear)
        self.clearButton.place(x=0, y=520, width=200)
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
        try:
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
                        # print("这个数是：", rowVale[3])
                        dataRowVale = ','.join(rowVale[1:])
                        InsertData = datarowVale + dataRowVale  # 插入信息
                        # print(InsertData)
                        # 将其装换为list，用于插入数据库中
                        self.dataSql = InsertData.split(',')
                        # 在界面中显示正在插入条数
                        self.num += 1
                        self.label["text"] ="正在插入第"+str(self.num)+"条数据"
                        self.label.update()
                        time.sleep(0.01)
                        # 存入数据库
                        print(self.dataSql[17])
                        self.depositSql()
        #   文件操作的异常处理
        except TypeError:
            messagebox.showinfo(title='打开文件', message='数据格式不匹配！！！')
        except FileNotFoundError:
            messagebox.showinfo(title='打开文件', message='用户取消了导入！！！')

    def OptionInsert(self):
        """选项查询"""
        # 获取标签内容
        if self.option == "姓名":
            option = "name"
            name = self.nameEntry.get()
            self.SQL(option, name)

        elif self.option == "证件类型":
            option = "certificate"
            certificate = self.certificateEntry.get()
            self.SQL(option, certificate)

        elif self.option == "乘车日期":
            option = "todate"
            todate = self.todateEntry.get()
            self.SQL(option, todate)

        elif self.option == "乘车时间":
            option = "totime"
            totime = self.totimeEntry.get()
            self.SQL(option, totime)

        elif self.option == "票号":
            option = "ticketid"
            ticketid = self.ticketidEntry.get()
            self.SQL(option, ticketid)

        elif self.option == "车次":
            option = "trainnumber"
            trainnumber = self.trainnumberEntry.get()
            self.SQL(option, trainnumber)

        elif self.option == "发站":
            option = "startingstation"
            startingstation = self.startingstationEntry.get()
            self.SQL(option, startingstation)

        elif self.option == "到站":
            option = "destination"
            destination = self.destinationEntry.get()
            self.SQL(option, destination)

        elif self.option == "席别":
            option = "seats"
            seats = self.seatsEntry.get()
            self.SQL(option, seats)

        elif self.option == "票种":
            option = "ticket"
            ticket = self.ticketEntry.get()
            self.SQL(option, ticket)

        elif self.option == "票价":
            option = "ticketrates"
            ticketrates = self.ticketratesEntry.get()
            self.SQL(option, ticketrates)

        elif self.option == "窗口":
            option = "window"
            window = self.windowEntry.get()
            self.SQL(option, window)

        elif self.option == "座位号":
            option = "seatnumber"
            seatnumber = self.seatnumberEntry.get()
            self.SQL(option, seatnumber)

        elif self.option == "车厢号":
            option = "carriagenumber"
            carriagenumber = self.carriagenumberEntry.get()
            self.SQL(option, carriagenumber)

        elif self.option == "操作员":
            option = "operator"
            operator = self.operatorEntry.get()
            self.SQL(option, operator)

        elif self.option == "出票时间":
            option = "totickettime"
            totickettime = self.totickettimeEntry.get()
            self.SQL(option, totickettime)

        elif self.option == "证件号码":
            option = "idnumber"
            idnumber = self.idnumberEntry.get()
            self.SQL(option, idnumber)

    # 触发事件
    def name_label(self, events):
        self.option = self.nameLabel.cget("text")

    def certificate_label(self, events):
        self.option = self.certificateLabel.cget("text")
        # print(certificate)

    def ticketid_label(self, events):
        self.option = self.ticketidLabel.cget("text")
        # print(ticketid)

    def trainnumber_label(self, events):
        self.option = self.trainnumberLabel.cget("text")
        # print(trainnumber)

    def startingstation_label(self, events):
        self.option = self.startingstationLabel.cget("text")
        # print(startingstation)

    def destination_label(self, events):
        self.option = self.destinationLabel.cget("text")
        # print(destination)

    def seats_Label(self, events):
        self.option = self.seatsLabel.cget("text")
        # print(seats)

    def ticket_Label(self, events):
        self.option = self.ticketLabel.cget("text")
        # print(ticket)

    def ticketrates_Label(self, events):
        self.option = self.ticketratesLabel.cget("text")
        # print(ticketrates)

    def window_Label(self, events):
        self.option = self.windowLabel.cget("text")
        # print(window)

    def seatnumber_Label(self, events):
        self.option = self.seatnumberLabel.cget("text")
        # print(seatnumber)

    def carriagenumber_Labek(self, events):
        self.option = self.carriagenumberLabel.cget("text")
        # print(carriagenumber)

    def operator_Labek(self, events):
        self.option = self.operatorLabel.cget("text")
        # print(operator)

    def ticketplace_Label(self, events):
        self.option = self.ticketplaceLabel.cget("text")
        # print(ticketplace)

    def idnumber_Label(self, events):
        self.option = self.idnumberLabel.cget("text")
        # print(idnumber)

    def todate_Label(self, events):
        self.option = self.todateLabel.cget("text")
        # print(todate)

    def totime_Label(self,events):
        self.option = self.totimeLabel.cget("text")
        # print(totiem)

    def totickettime_Label(self, events):
        self.option = self.totickettimeLabel.cget("text")
        # print(totickettime)



    def SQL(self, option, info):
        """选项查询操作"""
        db = pymysql.connect('127.0.0.1', 'root', 'adminwj', 'info')
        cursor = db.cursor()
        sql = 'select * from ticket where %s = "%s"' % (option, info)
        try:
            cursor.execute(sql)
            db.commit()
            reslist = cursor.fetchall()
            if reslist:
                for item in reslist:
                    infolist = ['姓名:', item[1], '证件类别:', item[2], '证件号码:', item[3], '乘车日期:', item[4], '乘车时间:', item[5],
                                '票号:', item[6], '车次:', item[7], '发站:', item[8], '到站:', item[9], '车厢号:', item[10], '席别:',
                                item[11], '座位号:', item[12], '票种:', item[13], '票价:', item[14], '售票处:', item[15], '窗口:',
                                item[16], '操作员:', item[17], '售票时间：',item[18]]
                    strinfolist = ' '.join(infolist)
                    self.RightInfotext.insert(END, strinfolist + '\n')
            else:
                messagebox.showinfo(title='查询', message='未查询到数据！！！')
        except:
            db.rollback()
            cursor.close()
            messagebox.showinfo(title='查询', message='查询异常请联系管理人员！！！')
        finally:
            db.close()


    # def OneClickQuery(self):
    #     """一键查询"""
    #     db = pymysql.connect('127.0.0.1', 'root', 'adminwj', 'info')
    #     cursor = db.cursor()
    #     sql = 'select * from personalinformation'
    #     cursor.execute(sql)
    #     db.commit()
    #     reslist = cursor.fetchall()
    #     for item in reslist:
    #         # 这里占时不能根据数据库的字段进行自动增加或减少
    #         infolist = ['姓名：', str(item[1]), '证件类别：', item[2], '证件号码：', item[3], '出生日期：', item[4], '国家：', item[5], '地区：', item[6]
    #                     , '性别：', item[7], '籍贯：', item[8], '身份：', item[9], '曾用名：', item[10], '民族：', item[11]
    #         , '别名：', item[12], '婚姻状态：', item[13], '政治面貌：', item[14], '宗教信仰：', item[15], '身高：', item[16],
    #         '血型：', item[17], '兵役情况：', item[18], '教育程度：', item[19], '专长：', item[20], '人员特长：', item[21],
    #         '职业：', item[22], '户籍地址：', item[23], '出生地：', item[24], '人员属性：', item[25], '联系电话：', item[26],
    #         '备注：', item[27]]
    #         strinfolist = ' '.join(infolist)
    #         sum = item[0]
    #         print(sum)
    #         self.RightInfotext.insert(END, strinfolist + '\n')
    #         self.RightInfotext.update()
    #         self.label["text"] ="正在插入第"+str(sum)+"条数据"
    #         self.label.update()
    #     messagebox.showinfo(title='查询', message='查询完成！！！')


    def depositSql(self):
        """插入数据库操作"""
        db = pymysql.connect('127.0.0.1', 'root', 'adminwj', 'info')
        cursor = db.cursor()
        sql = 'insert into ticket values(0,"{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'\
            .format(self.dataSql[0], self.dataSql[1], self.dataSql[2],self.dataSql[3],
                    self.dataSql[4], self.dataSql[5], self.dataSql[6], self.dataSql[7],
                    self.dataSql[8], self.dataSql[9], self.dataSql[10], self.dataSql[11],
                    self.dataSql[12],self.dataSql[13], self.dataSql[14], self.dataSql[15],
                    self.dataSql[16], self.dataSql[17])
        try:
            cursor.execute(sql)
            db.commit()
            messagebox.showinfo(title="插入模块", message="插入完成！！！")
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