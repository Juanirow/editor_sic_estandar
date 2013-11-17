from PyQt4 import QtCore, QtGui
from hexadecimal import Hexadecimal
from convert import Convert
from register import Register
from tabse import Tabse

    
class Cargadorx():
    def __init__(self,window):
        self.window = window
        self.tabse = Tabse()
        self.lonsc = "0H"
        self.dirsc = "0H"
        self.dirprog = "0H"
        self.direj = "0H"
        self.hexa = Hexadecimal()
        self.convert = Convert()
        self.register = Register("A")
        self.error_indefinido = False
        self.error_duplicado = False

    def show_error(self,msg):
        QtGui.QMessageBox.about(self,"Error",msg)

    def load_file_name(self,list_obj,dirprog):
        val_int = self.convert.to_decimal(dirprog)
        self.dirprog = self.convert.decimal_to_hexadecimal(val_int)
        self.dirprog = self.register.adjust_bytes(self.dirprog,6,False)+"H"
        self.dirsc = self.dirprog
        self.step_1(list_obj)
        if not self.error_duplicado:
            self.create_memory()
            self.dirsc = self.dirprog
            self.direj = self.dirprog
            self.step_2(list_obj)
            self.init_empty_rows()
            self.tabse.print_tabse()
            if self.error_indefinido:
                self.show_error("Error en simbolo indefinido")
        else:
            self.show_error("Error simbolo duplicado")



    def step_1(self,list_obj):
        for list_n in list_obj:
            for n in list_n:
                if len(n) > 0:
                    if n[0] == "H":
                        self.step_h(n,1)
                    elif n[0] == "D":
                        self.step_1_d(n)
            self.dirsc = self.hexa.plus(self.dirsc,self.lonsc)

    def step_h(self,n,step):
        name = n[1:7]
        name = name.strip()
        self.lonsc = n[13:]+"H"
        if step == 1:
            if not self.tabse.exist_node(name):
                self.tabse.insert_section(name,self.dirsc,self.lonsc)
            else:
                ##print name
                self.error_duplicado = True

    def step_1_d(self,n):
        num = (len(n)-1)/12
        it = 0
        # print "num",num,len(n)
        while it < num:
            index1 = (it * 12)+1
            index2 = index1 + 6
            index3 = index2 + 6
            name = n[index1:index2].strip()
            #print "name",name 
            if index3 >= len(n):
                len_r = n[index2:]+"H"
            else:
                len_r = n[index2:index3]+"H"
            if not self.tabse.exist_node(name):
                val = self.hexa.plus(len_r,self.dirsc)
                self.tabse.insert_variable(name,val)
            else:
                print "error",name
                self.error_duplicado = True
            it += 1

    def step_2(self,list_obj):
        for list_n in list_obj:
            for n in list_n:
                if len(n) > 0:
                    if n[0] == "H":
                        self.step_h(n,2)
                    elif n[0] == "T":
                        self.charge_obj_code(n)
                    elif n[0] == "M":
                        self.change_m_register(n)
                    elif n[0] == "E":
                        self.reg_e(n)
            self.dirsc = self.hexa.plus(self.dirsc,self.lonsc) 

    def reg_e(self,r):
        if len(r) < 1:
            val = r[1:] + "H"
            self.direj = self.hexa.plus(self.dirsc,val)

    def charge_obj_code(self,r):
        string = r[9:]
        index = 0
        init = r[1:7]
        init = self.hexa.plus(init+"H",self.dirsc)[:-1]
        col_start = init[-1]+"H"
        col = int(self.convert.to_decimal(col_start)  + 1)
        dat1 = self.get_part_dat(init)
        res = self.hexa.subs(dat1,self.dirprog[:-2])
        dec_res = int(self.convert.to_decimal(res))
        while index < len(string):
            byte = string[index:index+2]
            item = QtGui.QTableWidgetItem(byte)
            self.window.tableWidget.setItem(dec_res,col,item)
            index+=2
            col = (col + 1) % 17
            if col == 0:
                col = 1
                dec_res += 1

    def get_part_dat(self,dat):
        if len(dat) == 1:
            return "0"
        else:
            return dat[:-1]

    def change_m_register(self,r):
        val = r[1:7]
        med_byte = r[7:9]
        sign = r[9]
        name = r[10:].strip()
        # print val,med_byte,sign,name
        n = self.tabse.get_register(name)
        if n:
            # print "existe"
            val = self.hexa.plus(val,self.dirsc)[:-1]
            content = self.get_content_at(val,3)
            # print val,content
            ant_content = ""
            if med_byte == "5":
                ant_content = content[0]
                content = content[1:]
            dir_es = n.get_dir()
            new_dir = self.make_operation(sign,content,dir_es)
            # print "perico",new_dir,content,sign,dir_es
            new_dir = self.register.adjust_bytes(new_dir,6,True)
            if med_byte == "5":
                new_dir = ant_content + new_dir[1:]
            new_dir = ant_content + new_dir
            # print new_dir
            col_num = val[-1] + "H"
            col = int(self.convert.to_decimal(col_num) + 1)
            val = self.get_part_dat(val)
            ren = self.hexa.subs(val,self.dirprog[:-2])
            ren = int(self.convert.to_decimal(ren))
            index = 0
            while index < len(new_dir):
                byte = new_dir[index:index+2]
                item = QtGui.QTableWidgetItem(byte)
                self.window.tableWidget.setItem(ren,col,item)
                index+=2
                col = (col + 1) % 17
                if col == 0:
                    col = 1
                    ren += 1
        else:
            self.error_indefinido = True

    def make_operation(self,sign,dat1,dat2):
        val1 = self.get_int_operator(dat1)
        val2 = self.get_int_operator(dat2)
        if sign == "-":
            ret = val1-val2
        else:
            ret = val1+val2
        ret = self.exp_to_hexadecimal(ret)
        return ret

    def get_int_operator(self,dat):
        if dat[-1] == "H":
            dat = dat[:-1]
        if dat[0] == "F":
            string = ""
            it = 0
            while it < len(dat):
                if not dat[it] == "F":
                    string += dat[it]
                it += 1
            if len(string) == 0:
                return -1
            else:
                val = "1"+("0"*len(string))+"H"
                val = self.convert.to_decimal(val)
                val2 = self.convert.to_decimal(string+"H")
                return val2-val
        else:
            return self.convert.to_decimal(dat+"H")


    def get_content_at(self,dirr,num):
        dir_n = dirr[-1]+"H"
        col = int(self.convert.to_decimal(dir_n) + 1)
        dire = self.get_part_dat(dirr)
        ren = self.hexa.subs(dire,self.dirprog[:-2])
        ren = int(self.convert.to_decimal(ren))
        it = 0
        text = ""
        while it < num:
            item = self.window.tableWidget.item(ren,col)
            text += str(item.text())
            it += 1
            col = (col + 1) % 17
            if col == 0:
                col = 1
                ren += 1 
        return text

    def exp_to_hexadecimal(self,val):
        if val < 0:
            val = int(val * -1)
            val = val ^ 65535
            val += 1
        if val == 0:
            val = "0H"
        else:
            val = self.convert.decimal_to_hexadecimal(val)
            if val[0] == "F" and len(val) > 6:
                val = "0"+val
        return val



    def create_memory(self):
        init = self.dirprog[:-1]
        length = self.hexa.subs(self.dirsc,self.dirprog)[:-1]
        star_rows= length[:-1]
        index = init[:-1]
        num_rows=star_rows+"H"
        num_rows=int(self.convert.to_decimal(num_rows))
        self.window.tableWidget.setRowCount(num_rows+1)
        it = 0
        while it <= num_rows:
            dir = index+"0H"
            dir = self.register.adjust_bytes(dir,6,False)
            item = QtGui.QTableWidgetItem(dir)
            self.window.tableWidget.setItem(it,0,item)
            it += 1
            index = self.hexa.plus(index,"1H")[:-1]

    def init_empty_rows(self):
        rows_count = self.window.tableWidget.rowCount()
        colum_count = self.window.tableWidget.columnCount()
        for i in range(rows_count):
            for j in range(colum_count):
                item = self.window.tableWidget.item(i,j)                
                if item == None:
                    item_text = QtGui.QTableWidgetItem("FF")
                    self.window.tableWidget.setItem(i,j,item_text)
