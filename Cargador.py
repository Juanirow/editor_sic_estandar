from PyQt4 import QtCore, QtGui
from windowcargador import Ui_DockWidget
from hexadecimal import Hexadecimal
from convert import Convert
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
        self.hex = Hexadecimal()

    def get_list_register(self):
		f = open(self.file_name)
		text = f.read()
		list = text.split("\n")
		return list

    def load_file_name(self,file_name):
        self.file_name = file_name+".os"
        list = self.get_list_register()
        self.header = list[0]
        self.end = list[-1]
        self.registers = list[1:-2]
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
#            print init,self.init,res,dec_res,col
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
            item = QtGui.QTableWidgetItem(index+"0H")
            self.window.tableWidget.setItem(it,0,item)
            it += 1
            index = self.hex.plus(index,"1H")[:-1]

    def charge_in_memory(self):
        self.charge_header()
        self.charge_text()

	

	

	
