from PyQt5.QtWidgets import QPushButton, QLineEdit, QApplication, QFormLayout, QWidget, QTextEdit, QMessageBox, QSpinBox
from PyQt5.QtCore import QObject, QRunnable, QThreadPool, pyqtSignal, pyqtSlot
from reportlab.pdfgen.canvas import Canvas
import os
import textwrap
from datetime import datetime
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl




class WorkerSignals(QObject):
    error = pyqtSignal(str)
    file_saved_as = pyqtSignal(str)


class Generator(QRunnable):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.signals = WorkerSignals()


    @pyqtSlot()
    def run(self):
        try:
            outfile = "zpypdfqtc/spsterm0.pdf"

            template = PdfReader("summativeassessment.pdf", decompress=False).pages[0]
            template_obj = pagexobj(template)
            canvas = Canvas(outfile)
            xobj_name = makerl(canvas, template_obj)
            canvas.doForm(xobj_name)

            
            today = datetime.today()
            canvas.drawString(410, 400, today.strftime('%F'))
            canvas.drawString(275, 385, self.data['name_of_student'])
            canvas.drawString(220, 360, self.data['date_of_birth'])
            canvas.drawString(150, 335, self.data['claass'])
            canvas.drawString(180, 309, self.data['section'])
            canvas.drawString(180, 284, self.data['roll_number'])
            canvas.drawString(222, 257, self.data['father_number'])
            canvas.drawString(230, 234, self.data['mother_number'])
            canvas.drawString(180, 206, self.data['address'])       
            canvas.drawString(200, 155, self.data['telephone'])
            canvas.drawString(260, 130, self.data['parent_signature'])
            
            canvas.save()

        except Exception as e:
            self.signals.error.emit(str(e))
            return
        self.signals.file_saved_as.emit(outfile)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.threadpool = QThreadPool()

        self.name_of_student = QLineEdit()
        self.date_of_birth = QLineEdit()
        self.claass = QLineEdit()
        self.section = QLineEdit()
        self.roll_number = QLineEdit()
        self.father_number = QLineEdit()
        self.mother_number = QLineEdit()
        self.address = QLineEdit()
        self.telephone = QLineEdit()
        self.parent_signature = QLineEdit()
        self.generate_btn = QPushButton("Generate PDF")
        self.generate_btn.pressed.connect(self.generate)
        layout = QFormLayout()

        layout.addRow("Name Of Student", self.name_of_student)
        layout.addRow("Date Of Birth", self.date_of_birth)
        layout.addRow("Class", self.claass)
        layout.addRow("Section", self.section)
        layout.addRow("Roll.No", self.roll_number)
        layout.addRow("Father Name", self.father_number)
        layout.addRow("Mother Name", self.mother_number)
        layout.addRow("Address", self.address)
        layout.addRow("Telephone", self.telephone)
        layout.addRow("Parent Signature", self.parent_signature)

        layout.addRow(self.generate_btn)
        self.setLayout(layout)


    def generate(self):
        self.generate_btn.setDisabled(True)
        data = {
            'name_of_student': self.name_of_student.text(),
            'date_of_birth': self.date_of_birth.text(),
            'claass': self.claass.text(),
            'section': self.section.text(),
            'roll_number': self.roll_number.text(),
            'father_number': self.father_number.text(),
            'mother_number': self.mother_number.text(),
            'address': self.address.text(),
            'telephone': self.telephone.text(),
            'parent_signature': self.parent_signature.text(),
        }
        g = Generator(data)
        g.signals.file_saved_as.connect(self.generated)
        g.signals.error.connect(print)  
        self.threadpool.start(g)


    def generated(self, outfile):
        self.generate_btn.setDisabled(False)
        try:
            os.startfile(outfile)
        except Exception:
            QMessageBox.information(self, "Finished", "PDF has been generated")




app = QApplication([])
w = Window()
w.show()
app.exec_()
