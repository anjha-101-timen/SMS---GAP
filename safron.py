
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QMessageBox, QHeaderView, QTableWidgetItem, QPushButton, QLineEdit, QApplication, QFormLayout, QWidget, QTextEdit, QMessageBox, QSpinBox
from PyQt5 import uic
from PyQt5.QtCore import QObject, QRunnable, QThreadPool, pyqtSignal, pyqtSlot
from reportlab.pdfgen.canvas import Canvas

import os
import textwrap
from datetime import datetime
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
import sys
import pymysql
import mysql.connector as c
import mysql.connector as c0


con = c.connect(host = 'localhost', user = 'root', password = '!sps10ANJ=', database = 'dbofsaffron')
crs = con.cursor()
''' if con.is_connected():
    print("Successfully Connected .....")
else:
    print("Connectivity Problem .....") '''


con0 = c0.connect(host = 'localhost', user = 'root', password = '!sps10ANJ=', database = 'dbofsaffron')
crs0 = con0.cursor()
''' if con0.is_connected():
    print("Successfully Connected .....")
else:
    print("Connectivity Problem .....") '''





class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()
		uic.loadUi("safronz.ui", self)
		self.tabWidget.setCurrentIndex(0)
		self.tabWidget.tabBar().setVisible(False)
		
		self.log_in_btn.clicked.connect(self.login)


		self.show()


	def login(self):
	    un = self.un_entry.text()
	    pw = self.pw_entry.text()

	    if(un == 'ANJ' and pw == 'ANJ'):
	    	
	    	self.tabWidget.tabBar().setVisible(True)
	    	self.tabWidget.setCurrentIndex(1)


	    	self.log_in_btn.setVisible(False)
	    	self.user_name.setVisible(False)
	    	self.pass_word.setVisible(False)
	    	self.un_entry.setVisible(False)
	    	self.pw_entry.setVisible(False)
	    	self.kindly_enter_details.setVisible(False)
	    	self.administrator_login_nameplate.setVisible(False)

	    	self.DBConnect()
	    	self.DBConnect0()
	    	self.Table_Student_Changes()
	    	self.Table_Marks_Changes()
	    	self.Get_Student_Data()
	    	self.Marks_FA_Data()
	    	
	    	self.Handle_Student_Settings()
	    	self.Handle_Student_Marks()


	    else:
	    	self.kindly_enter_details.setText("Invalid Login Details, Please Try Again!")


		
       


	def Table_Student_Changes(self):
		header = self.tableWidget_student.horizontalHeader()
		header.setSectionResizeMode(0,QHeaderView.ResizeToContents)
		header.setSectionResizeMode(1,QHeaderView.ResizeToContents)
		header.setSectionResizeMode(2,QHeaderView.ResizeToContents)
		header.setSectionResizeMode(3,QHeaderView.ResizeToContents)
		header.setSectionResizeMode(4,QHeaderView.ResizeToContents)
		header.setSectionResizeMode(5,QHeaderView.ResizeToContents)
		header.setSectionResizeMode(6,QHeaderView.ResizeToContents)
		header.setSectionResizeMode(7,QHeaderView.ResizeToContents)
		header.setSectionResizeMode(8,QHeaderView.ResizeToContents)
		header.setSectionResizeMode(9,QHeaderView.ResizeToContents)


	def Clear_valuec(self):
		self.student_id_zcaj.clear()
		self.student_name_zcaj.clear()
		self.date_of_birth_zcaj.clear()
		self.class_zcaj.clear()
		self.section_zcaj.clear()
		self.roll_number_zcaj.clear()
		self.father_name_zcaj.clear()
		self.mother_name_zcaj.clear()
		self.address_zcaj.clear()
		self.telephone_zcaj.clear()


	def Clear_valuer(self):
		self.student_id_zraj.clear()
		self.student_name_zraj.clear()
		self.date_of_birth_zraj.clear()
		self.class_zraj.clear()
		self.section_zraj.clear()
		self.roll_number_zraj.clear()
		self.father_name_zraj.clear()
		self.mother_name_zraj.clear()
		self.address_zraj.clear()
		self.telephone_zraj.clear()


	def Clear_valueu(self):
		self.student_id_zuaj.clear()
		self.student_name_zuaj.clear()
		self.date_of_birth_zuaj.clear()
		self.class_zuaj.clear()
		self.section_zuaj.clear()
		self.roll_number_zuaj.clear()
		self.father_name_zuaj.clear()
		self.mother_name_zuaj.clear()
		self.address_zuaj.clear()
		self.telephone_zuaj.clear()


	def Clear_valued(self):
		self.student_id_zdaj.clear()
		self.student_name_zdaj.clear()
		self.date_of_birth_zdaj.clear()
		self.class_zdaj.clear()
		self.section_zdaj.clear()
		self.roll_number_zdaj.clear()
		self.father_name_zdaj.clear()
		self.mother_name_zdaj.clear()
		self.address_zdaj.clear()
		self.telephone_zdaj.clear()

	def Table_Marks_Changes(self): 
		header = self.tableWidget_marks_crud.horizontalHeader()
		header.setSectionResizeMode(0,QHeaderView.ResizeToContents)
		header.setSectionResizeMode(1,QHeaderView.ResizeToContents)
		header.setSectionResizeMode(2,QHeaderView.ResizeToContents)
		header.setSectionResizeMode(3,QHeaderView.ResizeToContents)
		header.setSectionResizeMode(4,QHeaderView.ResizeToContents)
		header.setSectionResizeMode(5,QHeaderView.ResizeToContents)
		header.setSectionResizeMode(6,QHeaderView.ResizeToContents)
		header.setSectionResizeMode(7,QHeaderView.ResizeToContents)
		header.setSectionResizeMode(8,QHeaderView.ResizeToContents)
		

	def Clear_marks_valueco(self):
		self.student_id_cfa.clear()
		self.english_cfa.clear()
		self.hindi_cfa.clear()
		self.sanskrit_cfa.clear()
		self.mathematics_cfa.clear()
		self.science_cfa.clear()
		self.social_science_cfa.clear()
		self.computer_cfa.clear()
		self.general_knowlegde_cfa.clear()

	def Clear_marks_valuero(self):
		self.student_id_rfa.clear()
		self.english_rfa.clear()
		self.hindi_rfa.clear()
		self.sanskrit_rfa.clear()
		self.mathematics_rfa.clear()
		self.science_rfa.clear()
		self.social_science_rfa.clear()
		self.computer_rfa.clear()
		self.general_knowlegde_rfa.clear()

	def Clear_marks_valueuo(self):
		self.student_id_ufa.clear()
		self.english_ufa.clear()
		self.hindi_ufa.clear()
		self.sanskrit_ufa.clear()
		self.mathematics_ufa.clear()
		self.science_ufa.clear()
		self.social_science_ufa.clear()
		self.computer_ufa.clear()
		self.general_knowlegde_ufa.clear()

	def Clear_marks_valuedo(self):
		self.student_id_dfa.clear()
		self.english_dfa.clear()
		self.hindi_dfa.clear()
		self.sanskrit_dfa.clear()
		self.mathematics_dfa.clear()
		self.science_dfa.clear()
		self.social_science_dfa.clear()
		self.computer_dfa.clear()
		self.general_knowlegde_dfa.clear()

    		
	def DBConnect(self):
	    self.con = c.connect(host = 'localhost', user = 'root', password = '!sps10ANJ=', database = 'dbofsaffron')
	    self.crs = self.con.cursor()
	    

	def Get_Student_Data(self):
	    cmd = """ USE dbofsaffron """
	    self.crs.execute(cmd)
	    cmd = """ SELECT StudentID, StudentName, DateOfBirth, Class, Section, RollNo, FatherName, MotherName, Address, Telephone FROM StudentOfSPS """
	    self.crs.execute(cmd)
	    result = self.crs.fetchall()
	    
	    self.tableWidget_student.setRowCount(0)
	    for row_num, row_data in enumerate(result):
	        self.tableWidget_student.insertRow(row_num)
	        
	        for column_num, column_data in enumerate(row_data):
	            self.tableWidget_student.setItem(row_num,column_num, QTableWidgetItem(str(column_data)))       
	            
	    self.crs.execute(""" SELECT StudentID FROM StudentOfSPS """)
	    result = self.crs.fetchall()
	    self.student_combo_r.clear()
	    self.student_combo_u.clear()
	    self.student_combo_d.clear()
	    self.student_combo_r.addItem("---Student ID---")
	    self.student_combo_u.addItem("---Student ID---")
	    self.student_combo_d.addItem("---Student ID---")

	    for r in result:
	    	self.student_combo_r.addItem(r[0])
	    	self.student_combo_u.addItem(r[0])
	    	self.student_combo_d.addItem(r[0])
	    	   


	

	      
	def Handle_Student_Settings(self):
		self.btn_create_e1.clicked.connect(self.Create_Student_Details)
		self.btn_create_e1.clicked.connect(self.Get_Student_Data)
		self.btn_read_e1.clicked.connect(self.Read_Student_Details)
		self.btn_update_e0.clicked.connect(self.Update_Student_Report_Details)
		self.btn_update_e1.clicked.connect(self.Update_Student_Details)
		self.btn_delete_e0.clicked.connect(self.Delete_Student_Report_Details)
		self.btn_delete_e1.clicked.connect(self.Delete_Student_Details)
				
	def Create_Student_Details(self):
		vl_student_id_c = self.student_id_zcaj.text()
		vl_student_name_c = self.student_name_zcaj.text()
		vl_date_of_birth_c = self.date_of_birth_zcaj.text()
		vl_class_c = self.class_zcaj.text()
		vl_section_c = self.section_zcaj.text()
		vl_roll_number_c = self.roll_number_zcaj.text()
		vl_father_name_c = self.father_name_zcaj.text()
		vl_mother_name_c = self.mother_name_zcaj.text()
		vl_address_c = self.address_zcaj.text()
		vl_telephone_c = self.telephone_zcaj.text()

		sqlc = """ INSERT INTO StudentOfSPS(StudentID, StudentName, DateOfBirth, Class, Section, RollNo, FatherName, MotherName, Address, Telephone) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
		valc = (vl_student_id_c, vl_student_name_c, vl_date_of_birth_c, vl_class_c, vl_section_c, vl_roll_number_c, vl_father_name_c, vl_mother_name_c, vl_address_c, vl_telephone_c)
		self.crs.execute(sqlc, valc)
		self.con.commit()
		self.Clear_valuec()


	def Read_Student_Details(self):
		try:
		    student_val_r = self.student_combo_r.currentText()
		    sqlr = """ SELECT StudentID, StudentName, DateOfBirth, Class, Section, RollNo, FatherName, MotherName, Address, Telephone FROM StudentOfSPS WHERE StudentID = %s  """
		    valr = (student_val_r,)
		    self.crs.execute(sqlr, valr)
		    resultr = self.crs.fetchall()

		    zr1 = resultr[0][0]
		    zr2 = resultr[0][1]
		    zr3 = resultr[0][2]
		    zr4 = resultr[0][3]
		    zr5 = resultr[0][4]
		    zr6 = resultr[0][5]
		    zr7 = resultr[0][6]
		    zr8 = resultr[0][7]
		    zr9 = resultr[0][8]
		    zr10 = resultr[0][9]

		    self.student_id_zraj.setText(str(zr1))
		    self.student_name_zraj.setText(str(zr2))
		    self.date_of_birth_zraj.setText(str(zr3))
		    self.class_zraj.setText(str(zr4))
		    self.section_zraj.setText(str(zr5))
		    self.roll_number_zraj.setText(str(zr6))
		    self.father_name_zraj.setText(str(zr7))
		    self.mother_name_zraj.setText(str(zr8))
		    self.address_zraj.setText(str(zr9))
		    self.telephone_zraj.setText(str(zr10))

		except:
		    self.Clear_valuer()        
		    pass
		

	def Update_Student_Report_Details(self):
		try:
		    student_val_u = self.student_combo_u.currentText()
		    sqlu0 = """ SELECT StudentID, StudentName, DateOfBirth, Class, Section, RollNo, FatherName, MotherName, Address, Telephone FROM StudentOfSPS WHERE StudentID = %s  """
		    valu0 = (student_val_u,)
		    self.crs.execute(sqlu0, valu0)
		    resultu0 = self.crs.fetchall()
		
		    zu1 = resultu0[0][0]
		    zu2 = resultu0[0][1]
		    zu3 = resultu0[0][2]
		    zu4 = resultu0[0][3]
		    zu5 = resultu0[0][4]
		    zu6 = resultu0[0][5]
		    zu7 = resultu0[0][6]
		    zu8 = resultu0[0][7]
		    zu9 = resultu0[0][8]
		    zu10 = resultu0[0][9]

		    self.student_id_zuaj.setText(str(zu1))
		    self.student_name_zuaj.setText(str(zu2))
		    self.date_of_birth_zuaj.setText(str(zu3))
		    self.class_zuaj.setText(str(zu4))
		    self.section_zuaj.setText(str(zu5))
		    self.roll_number_zuaj.setText(str(zu6))
		    self.father_name_zuaj.setText(str(zu7))
		    self.mother_name_zuaj.setText(str(zu8))
		    self.address_zuaj.setText(str(zu9))
		    self.telephone_zuaj.setText(str(zu10))

		except:
		    self.Clear_valueu()        
		    pass


	def Update_Student_Details(self):
		vl_student_id_u = self.student_id_zuaj.text()
		vl_student_name_u = self.student_name_zuaj.text()
		vl_date_of_birth_u = self.date_of_birth_zuaj.text()
		vl_class_u = self.class_zuaj.text()
		vl_section_u = self.section_zuaj.text()
		vl_roll_number_u = self.roll_number_zuaj.text()
		vl_father_name_u = self.father_name_zuaj.text()
		vl_mother_name_u = self.mother_name_zuaj.text()
		vl_address_u = self.address_zuaj.text()
		vl_telephone_u = self.telephone_zuaj.text()

		sqlu1 = """ UPDATE StudentOfSPS SET StudentName=%s, DateOfBirth=%s, Class=%s, Section=%s, RollNo=%s, FatherName=%s, MotherName=%s, Address=%s, Telephone=%s WHERE StudentID =%s """
		valu1 = (vl_student_name_u, vl_date_of_birth_u, vl_class_u, vl_section_u, vl_roll_number_u, vl_father_name_u, vl_mother_name_u, vl_address_u, vl_telephone_u, vl_student_id_u)
		self.crs.execute(sqlu1, valu1)
		self.con.commit()
		self.Clear_valueu()
		self.Get_Student_Data()


	def Delete_Student_Report_Details(self):
		try:
		    student_val_d = self.student_combo_d.currentText()
		    sqld = """ SELECT StudentID, StudentName, DateOfBirth, Class, Section, RollNo, FatherName, MotherName, Address, Telephone FROM StudentOfSPS WHERE StudentID = %s  """
		    vald = (student_val_d,)
		    self.crs.execute(sqld, vald)
		    resultd = self.crs.fetchall()
		
		    zd1 = resultd[0][0]
		    zd2 = resultd[0][1]
		    zd3 = resultd[0][2]
		    zd4 = resultd[0][3]
		    zd5 = resultd[0][4]
		    zd6 = resultd[0][5]
		    zd7 = resultd[0][6]
		    zd8 = resultd[0][7]
		    zd9 = resultd[0][8]
		    zd10 = resultd[0][9]

		    self.student_id_zdaj.setText(str(zd1))
		    self.student_name_zdaj.setText(str(zd2))
		    self.date_of_birth_zdaj.setText(str(zd3))
		    self.class_zdaj.setText(str(zd4))
		    self.section_zdaj.setText(str(zd5))
		    self.roll_number_zdaj.setText(str(zd6))
		    self.father_name_zdaj.setText(str(zd7))
		    self.mother_name_zdaj.setText(str(zd8))
		    self.address_zdaj.setText(str(zd9))
		    self.telephone_zdaj.setText(str(zd10))

		except:
		    self.Clear_valued()        
		    pass	


	def Delete_Student_Details(self):
		vl_student_id_d = str(self.student_id_zdaj.text())
		cmdd = """ DELETE FROM StudentOfSPS WHERE StudentID=%s """
		self.crs.execute(cmdd, (vl_student_id_d,))
		self.con.commit()
		self.Clear_valued()
		self.Get_Student_Data()


	def DBConnect0(self):
		self.con0 = c0.connect(host = 'localhost', user = 'root', password = '!sps10ANJ=', database = 'dbofsaffron')
		self.crs0 = self.con0.cursor()

	def Marks_FA_Data(self):
		cmd0 = """ USE dbofsaffron """
		self.crs0.execute(cmd0)
		cmd0 = """ SELECT StudentID010, English, Hindi, Sanskrit, Mathematics, Science, SocialScience, Computer, GeneralKnowledge FROM FormativeAssessment00100SPS """
		self.crs0.execute(cmd0)
		result0 = self.crs0.fetchall()
		self.tableWidget_marks_crud.setRowCount(0)
		for row_num0, row_data0 in enumerate(result0):
			self.tableWidget_marks_crud.insertRow(row_num0)
			for column_num0, column_data0 in enumerate(row_data0):
				self.tableWidget_marks_crud.setItem(row_num0,column_num0, QTableWidgetItem(str(column_data0)))       
		self.crs0.execute(""" SELECT StudentID010 FROM FormativeAssessment00100SPS """)
		result0 = self.crs0.fetchall()
		self.fa_rfa.clear()
		self.fa_ufa.clear()
		self.fa_dfa.clear()
		self.fa_rfa.addItem("---Student ID---")
		self.fa_ufa.addItem("---Student ID---")
		self.fa_dfa.addItem("---Student ID---")
		for r in result0:
			self.fa_rfa.addItem(r[0])
			self.fa_ufa.addItem(r[0])
			self.fa_dfa.addItem(r[0])

	def Handle_Student_Marks(self):
		self.btn_create_fa1.clicked.connect(self.Create_Student_Marks_Details)
		self.btn_create_fa1.clicked.connect(self.Marks_FA_Data)
		self.btn_create_fa0.clicked.connect(self.Create_Student_Marks_Details)
		self.btn_create_fa0.clicked.connect(self.Marks_FA_Data)
		self.btn_read_fa1.clicked.connect(self.Read_Student_Marks_Details)
		self.btn_read_fa0.clicked.connect(self.Read_Student_Marks_Details)
		self.btn_update_fa1.clicked.connect(self.Update_Student_Marks_Report_Details)
		self.btn_update_fa0.clicked.connect(self.Update_Student_Marks_Details)
		self.btn_delete_fa1.clicked.connect(self.Delete_Student_Marks_Report_Details)
		self.btn_delete_fa0.clicked.connect(self.Delete_Student_Marks_Details)

	def Create_Student_Marks_Details(self):
		studentidco = self.student_id_cfa.text()
		englishco = self.english_cfa.text()
		hindico = self.hindi_cfa.text()
		sanskritco = self.sanskrit_cfa.text()
		mathsco = self.mathematics_cfa.text()
		scienceco = self.science_cfa.text()
		socialscienceco = self.social_science_cfa.text()
		computerco = self.computer_cfa.text()
		generalknowlegdeco = self.general_knowlegde_cfa.text()
		sqlco = """ INSERT INTO FormativeAssessment00100SPS(StudentID010, English, Hindi, Sanskrit, Mathematics, Science, SocialScience, Computer, GeneralKnowledge) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s) """
		valco = (studentidco, englishco, hindico, sanskritco, mathsco, scienceco, socialscienceco, computerco, generalknowlegdeco)
		self.crs0.execute(sqlco, valco)
		self.con0.commit()
		self.Clear_marks_valueco()

	def Read_Student_Marks_Details(self):
		try:
			student_marks_vl_ro = self.fa_rfa.currentText()
			sqlro = """ SELECT StudentID010, English, Hindi, Sanskrit, Mathematics, Science, SocialScience, Computer, GeneralKnowledge FROM FormativeAssessment00100SPS WHERE StudentID010 = %s  """
			valro = (student_marks_vl_ro,)
			self.crs0.execute(sqlro, valro)
			resultro = self.crs0.fetchall()
			zro1 = resultro[0][0]
			zro2 = resultro[0][1]
			zro3 = resultro[0][2]
			zro4 = resultro[0][3]
			zro5 = resultro[0][4]
			zro6 = resultro[0][5]
			zro7 = resultro[0][6]
			zro8 = resultro[0][7]
			zro9 = resultro[0][8]
			self.student_id_rfa.setText(str(zro1))
			self.english_rfa.setText(str(zro2))
			self.hindi_rfa.setText(str(zro3))
			self.sanskrit_rfa.setText(str(zro4))
			self.mathematics_rfa.setText(str(zro5))
			self.science_rfa.setText(str(zro6))
			self.social_science_rfa.setText(str(zro7))
			self.computer_rfa.setText(str(zro8))
			self.general_knowlegde_rfa.setText(str(zro9))
		except:
			self.Clear_marks_valuero()
			pass
	def Update_Student_Marks_Report_Details(self):
		try:
			student_marks_vl_uo = self.fa_ufa.currentText()
			sqluo= """ SELECT StudentID010, English, Hindi, Sanskrit, Mathematics, Science, SocialScience, Computer, GeneralKnowledge FROM FormativeAssessment00100SPS WHERE StudentID010 = %s  """
			valuo = (student_marks_vl_uo,)
			self.crs0.execute(sqluo, valuo)
			resultuo = self.crs0.fetchall()
			zuo1 = resultuo[0][0]
			zuo2 = resultuo[0][1]
			zuo3 = resultuo[0][2]
			zuo4 = resultuo[0][3]
			zuo5 = resultuo[0][4]
			zuo6 = resultuo[0][5]
			zuo7 = resultuo[0][6]
			zuo8 = resultuo[0][7]
			zuo9 = resultuo[0][8]
			self.student_id_ufa.setText(str(zuo1))
			self.english_ufa.setText(str(zuo2))
			self.hindi_ufa.setText(str(zuo3))
			self.sanskrit_ufa.setText(str(zuo4))
			self.mathematics_ufa.setText(str(zuo5))
			self.science_ufa.setText(str(zuo6))
			self.social_science_ufa.setText(str(zuo7))
			self.computer_ufa.setText(str(zuo8))
			self.general_knowlegde_ufa.setText(str(zuo9))
		except:
			self.Clear_marks_valueuo()
			pass
	def Update_Student_Marks_Details(self):
		studentiduo = self.student_id_ufa.text()
		englishuo = self.english_ufa.text()
		hindiuo = self.hindi_ufa.text()
		sanskrituo = self.sanskrit_ufa.text()
		mathsuo = self.mathematics_ufa.text()
		scienceuo = self.science_ufa.text()
		socialscienceuo = self.social_science_ufa.text()
		computeruo = self.computer_ufa.text()
		generalknowlegdeuo = self.general_knowlegde_ufa.text()
		sqluo0 = """ UPDATE FormativeAssessment00100SPS SET English=%s, Hindi=%s, Sanskrit=%s, Mathematics=%s, Science=%s, SocialScience=%s, Computer=%s, GeneralKnowledge=%s WHERE StudentID010 =%s """
		valuo0 = (englishuo, hindiuo, sanskrituo, mathsuo, scienceuo, socialscienceuo, computeruo, generalknowlegdeuo, studentiduo)
		self.crs0.execute(sqluo0, valuo0)
		self.con0.commit()
		self.Clear_marks_valueuo()
		self.Marks_FA_Data()

	def Delete_Student_Marks_Report_Details(self):
		try:
			student_val_do = self.fa_dfa.currentText()
			sqldo = """ SELECT StudentID010, English, Hindi, Sanskrit, Mathematics, Science, SocialScience, Computer, GeneralKnowledge FROM FormativeAssessment00100SPS WHERE StudentID010 = %s  """
			valdo = (student_val_do,)
			self.crs0.execute(sqldo, valdo)
			resultdo = self.crs0.fetchall()
			zdo1 = resultdo[0][0]
			zdo2 = resultdo[0][1]
			zdo3 = resultdo[0][2]
			zdo4 = resultdo[0][3]
			zdo5 = resultdo[0][4]
			zdo6 = resultdo[0][5]
			zdo7 = resultdo[0][6]
			zdo8 = resultdo[0][7]
			zdo9 = resultdo[0][8]
			self.student_id_dfa.setText(str(zdo1))
			self.english_dfa.setText(str(zdo2))
			self.hindi_dfa.setText(str(zdo3))
			self.sanskrit_dfa.setText(str(zdo4))
			self.mathematics_dfa.setText(str(zdo5))
			self.science_dfa.setText(str(zdo6))
			self.social_science_dfa.setText(str(zdo7))
			self.computer_dfa.setText(str(zdo8))
			self.general_knowlegde_dfa.setText(str(zdo9))
		except:
			self.Clear_marks_valuedo()
			pass    
	def Delete_Student_Marks_Details(self):
		vl_student_id_do = str(self.student_id_dfa.text())
		cmddo = """ DELETE FROM FormativeAssessment00100SPS WHERE StudentID010=%s """
		self.crs0.execute(cmddo, (vl_student_id_do,))
		self.con0.commit()
		self.Clear_marks_valuedo()
		self.Marks_FA_Data()


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()		
