from PyQt4 import QtCore, QtGui
from windowcargador import Ui_DockWidget
from hexadecimal import Hexadecimal
from convert import Convert
from register import Register
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
    
class Cargador(QtGui.QDockWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self)
        self.window = Ui_DockWidget()
        self.window.setupUi(self)
        self.file_name = None
        self.init = None
        self.header = None
        self.registers = None
        self.end = None
        self.rows_count = None
        self.hex = Hexadecimal()
        self.window.btnSimular.clicked.connect(self.simular)
        
    def simular(self):
        num_actions = self.get_count_next_actions()
        if num_actions == -1:
            self.window.textEdit_Actions.setText("Numero de simulaciones no Validas")
        else:
            self.make_n_simulations(num_actions)
            
    def make_n_simulations(self,number):
        
    
    def get_count_next_actions(self):
        count_actions = str(self.window.textEdit_Num.toPlainText())
        if count_actions == "":
            count_actions = 0
        elif not count_actions.isdigit():
            return -1
        return int(count_actions)
        
    def get_list_register(self):
        f = open(self.file_name)
        text = f.read()
        list = text.split("\n")
        list.remove("")
        return list

    def load_file_name(self,file_name):
        self.file_name = file_name+".os"
        list = self.get_list_register()
        self.header = list[0]
        self.end = list[-1]
        self.registers = list[1:-1]
        self.charge_in_memory()
        
    def charge_text(self):
        c = Convert()        
        for r in self.registers:
            string = r[9:]
            index = 0
            init = r[1:7]
            col_start = init[-1]+"H"
            col = int(c.to_decimal(col_start)  + 1) 
            res = self.hex.subs(init[:-1],self.init[:-1])
            dec_res = int(c.to_decimal(res))
            while index < len(string):
                byte = string[index:index+2]
                item = QtGui.QTableWidgetItem(byte)
                self.window.tableWidget.setItem(dec_res,col,item)
                index+=2
                col = (col + 1) % 17
                if col == 0:
                    col = 1
                    dec_res += 1
            
    def charge_header(self):
        init = self.header[7:13]
        self.init = init
        length = self.header[13:]
        star_rows= length[:-1]
        index = init[:-1]
        num_rows=star_rows+"H"
        c = Convert()
        num_rows=int(c.to_decimal(num_rows))
        self.window.tableWidget.setRowCount(num_rows+1)
        it = 0
        while it <= num_rows:
            dir = index+"0H"
            r = Register("T")
            dir = r.adjust_bytes(dir,6)
            item = QtGui.QTableWidgetItem(dir)
            self.window.tableWidget.setItem(it,0,item)
            it += 1
            index = self.hex.plus(index,"1H")[:-1]
    
    def charge_end_file(self):
        dir = self.end[1:]
        dir = self.hex.change_hexadecimal(dir)
        item = QtGui.QTableWidgetItem(dir)
        self.window.tableWidget_2.setItem(0,0,item)
        it = 1
        while it < 5:
            item = QtGui.QTableWidgetItem("007FFFH")
            self.window.tableWidget_2.setItem(it,0,item)
            it += 1
        

    def charge_in_memory(self):
        self.charge_header()
        self.charge_text()
        self.charge_end_file()
        self.init_empty_rows()
        
    def init_empty_rows(self):
        rows_count = self.window.tableWidget.rowCount()
        colum_count = self.window.tableWidget.columnCount()
        for i in range(rows_count):
            for j in range(colum_count):
                item = self.window.tableWidget.item(i,j)                
                if item == None:
                    item_text = QtGui.QTableWidgetItem("FF")
                    self.window.tableWidget.setItem(i,j,item_text)
            
        

	

	

	
