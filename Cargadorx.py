from PyQt4 import QtCore, QtGui
from windowcargador import Ui_DockWidget
from hexadecimal import Hexadecimal
from convert import Convert
from register import Register
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
    
class Cargadorx(QtGui.QDockWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self)
        self.window = Ui_DockWidget()
        self.window.setupUi(self)
        # self.file_name = None
        # self.init = None
        # self.header = None
        # self.registers = None
        # self.end = None
        # self.rows_count = None
        # self.end_program = None
        # self.cc = "="
        # self.hex = Hexadecimal()
        # self.reg = Register("T")
        # self.window.btnSimular.clicked.connect(self.simular)
        # self.operations = {"18":self.add,"00":self.lda,"40":self.andop,
        #                    "28":self.cmp_op,"24":self.div,"3C":self.j_op,
        #                    "30":self.jeq,"34":self.jgt,"38":self.jlt,
        #                    "48":self.jsub,"50":self.ldch,"08":self.ldl,
        #                    "04":self.ldx,"20":self.mul,"4C":self.rsub,
        #                    "0C":self.sta,"54":self.stch,"14":self.stl,
        #                    "E8":self.stsw,"10":self.stx,"1C":self.sub,"2C":self.tix}
        # self.operations_text = {"18":"ADD","00":"LDA","40":"AND",
        #                    "28":"COMP","24":"DIV","3C":"J",
        #                    "30":"JEQ","34":"JGT","38":"JLT",
        #                    "48":"JSUB","50":"LDCH","08":"LDL",
        #                    "04":"LDX","20":"MUL","4C":"RSUB",
        #                    "0C":"STA","54":"STCH","14":"STL",
        #                    "E8":"STSW","10":"STX","1C":"SUB","2C":"TIX"}

     
    def load_file_name(self,list_obj):
         print "Hola"   
    # def simular(self):
    #     num_actions = self.get_count_next_actions()
    #     if num_actions == -1:
    #         self.window.textEdit_Actions.setText("Numero de simulaciones no Validas")
    #     else:
    #         self.make_n_simulations(num_actions)
            
    # def make_n_simulations(self,number):
    #     cp = self.get_CP_value()
    #     if self.hex.minus_than(cp,self.end_program):
    #         it = 0
    #         while it < number:            
    #             register = self.get_instruct()
    #             operation = register[0:2]
    #             address = register[2:]
    #             val = self.get_address_tarjet(address)
    #             fun = self.operations[operation]    
    #             fun(val)
    #             it+=1
    #     else:
    #         self.window.textEdit_Actions.setText("El programa se ha terminado no puede continuar la simulacion")
        
    # def increment_cp(self,num):
    #     c = Convert()        
    #     num = c.decimal_to_hexadecimal(num)
    #     cp = self.get_CP_value()
    #     cp = self.hex.plus(cp,num)
    #     self.set_cp_value(cp)
        

    # def get_address_tarjet(self,value):
    #     c = Convert()       
    #     addressing = value[0]+"H"
    #     addressing = int(c.to_decimal(addressing))
    #     val = value
    #     bina = c.decimal_to_binary(addressing,4)
    #     bina = c.mask_and(bina,"1000")
    #     if bina == "1000":
    #         val = self.hex.subs(value,"8000H") 
    #         x = self.get_x_value()
    #         val = self.hex.plus(val,x)
    #         val = self.reg.filter_number(val)
    #     return val

    # def set_a_value(self,value):
    #     value = self.reg.adjust_bytes(value,6,False)
    #     value = self.hex.change_hexadecimal(value)
    #     item_text = QtGui.QTableWidgetItem(value)
    #     self.window.tableWidget_2.setItem(1,0,item_text)  
        
    # def get_a_value(self):
    #     item = self.window.tableWidget_2.item(1,0)
    #     return str(item.text())
        
    # def get_l_value(self):
    #     item = self.window.tableWidget_2.item(3,0)
    #     return str(item.text())
        
    # def set_l_value(self,value):
    #     value = self.reg.adjust_bytes(value,6,False)
    #     value = self.hex.change_hexadecimal(value)
    #     item_text = QtGui.QTableWidgetItem(value)
    #     self.window.tableWidget_2.setItem(3,0,item_text)
        
    # def get_x_value(self):
    #     item = self.window.tableWidget_2.item(2,0)
    #     return str(item.text())
    
    # def set_x_value(self,value):
    #     value = self.reg.adjust_bytes(value,6,False)
    #     value = self.hex.change_hexadecimal(value)
    #     item_text = QtGui.QTableWidgetItem(value)
    #     self.window.tableWidget_2.setItem(2,0,item_text)
        
    # def get_sw_value(self):
    #     item = self.window.tableWidget_2.item(4,0)
    #     return str(item.text())
    
    # def set_sw_value(self,value):
    #     value = self.reg.adjust_bytes(value,6,False)
    #     value = self.hex.change_hexadecimal(value)
    #     item_text = QtGui.QTableWidgetItem(value)
    #     self.window.tableWidget_2.setItem(4,0,item_text)   
        
    # def get_CP_value(self):
    #     item = self.window.tableWidget_2.item(0,0)
    #     return str(item.text())
    
    # def set_cp_value(self,cp):
    #     cp = self.reg.adjust_bytes(cp,6,False)
    #     cp = self.hex.change_hexadecimal(cp)
    #     item_text = QtGui.QTableWidgetItem(cp)
    #     self.window.tableWidget_2.setItem(0,0,item_text)
    #     self.get_next_text_instruction()
    
    # def get_next_text_instruction(self):
    #     cp = self.get_CP_value()
    #     mem = self.get_mem_value(cp)
    #     cod = mem[0:2]
    #     op = self.operations_text.get(str(cod),"FIN")
    #     self.window.label_sig.setText(op)
    
        
    # def get_row_index(self,value):
    #     index = str(value[0:-1])+"0"
    #     it = 0
    #     index = self.reg.adjust_bytes(index,6,False)
    #     num_rows = self.window.tableWidget.rowCount()
    #     while it < num_rows:
    #         val = self.window.tableWidget.item(it,0)
    #         if str(val.text()) == index:
    #             return it
    #         it += 1
    #     return 0
        

    # def get_column_index(self,value):
    #     c = Convert()        
    #     index = str(value[-1])+"H"
    #     index = c.to_decimal(index)
    #     del c 
    #     return index+1
        
    # def get_instruct(self):
    #     cp = self.get_CP_value()
    #     return self.get_mem_value(cp)
        
    # def get_mem_value(self,value):
    #     value = self.reg.filter_number(str(value))
    #     col = self.get_column_index(value)
    #     row = self.get_row_index(value)
    #     register = ""
    #     it = col
    #     cont = 0
    #     while cont < 3:
    #         item = self.window.tableWidget.item(row,it)
    #         register += str(item.text())
    #         it = (it+1)%17
    #         if it == 0:
    #             it = 1
    #             row+=1
    #         cont += 1
    #     return register
        
    # def get_count_next_actions(self):
    #     count_actions = str(self.window.textEdit_Num.toPlainText())
    #     if count_actions == "":
    #         count_actions = 1
    #     elif not count_actions.isdigit():
    #         return -1
    #     return int(count_actions)
        
    # def get_list_register(self):
    #     f = open(self.file_name)
    #     text = f.read()
    #     list = text.split("\n")
    #     list.remove("")
    #     return list

    # def load_file_name(self,file_name):
    #     self.file_name = file_name+".os"
    #     list = self.get_list_register()
    #     self.header = list[0]
    #     self.end = list[-1]
    #     self.registers = list[1:-1]
    #     self.charge_in_memory()
        
    # def charge_text(self):
    #     c = Convert()        
    #     for r in self.registers:
    #         string = r[9:]
    #         index = 0
    #         init = r[1:7]
    #         col_start = init[-1]+"H"
    #         col = int(c.to_decimal(col_start)  + 1) 
    #         res = self.hex.subs(init[:-1],self.init[:-1])
    #         dec_res = int(c.to_decimal(res))
    #         while index < len(string):
    #             byte = string[index:index+2]
    #             item = QtGui.QTableWidgetItem(byte)
    #             self.window.tableWidget.setItem(dec_res,col,item)
    #             index+=2
    #             col = (col + 1) % 17
    #             if col == 0:
    #                 col = 1
    #                 dec_res += 1
            
    # def charge_header(self):
    #     init = self.header[7:13]
    #     self.init = init
    #     length = self.header[13:]
    #     self.end_program = self.hex.plus(init,length)
    #     star_rows= length[:-1]
    #     index = init[:-1]
    #     num_rows=star_rows+"H"
    #     c = Convert()
    #     num_rows=int(c.to_decimal(num_rows))
    #     self.window.tableWidget.setRowCount(num_rows+1)
    #     it = 0
    #     while it <= num_rows:
    #         dir = index+"0H"
    #         r = Register("T")
    #         dir = r.adjust_bytes(dir,6,False)
    #         item = QtGui.QTableWidgetItem(dir)
    #         self.window.tableWidget.setItem(it,0,item)
    #         it += 1
    #         index = self.hex.plus(index,"1H")[:-1]
    
    # def charge_end_file(self):
    #     dir = self.end[1:]
    #     dir = self.reg.adjust_bytes(dir,6,False)
    #     dir = self.hex.change_hexadecimal(dir)
    #     item = QtGui.QTableWidgetItem(dir)
    #     self.window.tableWidget_2.setItem(0,0,item)
    #     self.get_next_text_instruction()
    #     it = 1
    #     while it < 5:
    #         item = QtGui.QTableWidgetItem("FFFFFFH")
    #         self.window.tableWidget_2.setItem(it,0,item)
    #         it += 1
        

    # def charge_in_memory(self):
    #     self.charge_header()
    #     self.charge_text()
    #     self.charge_end_file()
    #     self.init_empty_rows()
        
    # def init_empty_rows(self):
    #     rows_count = self.window.tableWidget.rowCount()
    #     colum_count = self.window.tableWidget.columnCount()
    #     for i in range(rows_count):
    #         for j in range(colum_count):
    #             item = self.window.tableWidget.item(i,j)                
    #             if item == None:
    #                 item_text = QtGui.QTableWidgetItem("FF")
    #                 self.window.tableWidget.setItem(i,j,item_text)