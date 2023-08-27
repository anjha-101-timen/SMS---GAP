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
            outfile = "zpypdfqtc/spsunitest0.pdf"

            template = PdfReader("formattiveassessment.pdf", decompress=False).pages[0]
            template_obj = pagexobj(template)
            canvas = Canvas(outfile)
            xobj_name = makerl(canvas, template_obj)
            canvas.doForm(xobj_name)

            
            today = datetime.today()
            canvas.drawString(275, 385, self.data['Student'])
            canvas.save()

        except Exception as e:
            self.signals.error.emit(str(e))
            return
        self.signals.file_saved_as.emit(outfile)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.threadpool = QThreadPool()

        self.Student = QLineEdit()
        self.generate_btn = QPushButton("Student")
        self.generate_btn.pressed.connect(self.generate)
        layout = QFormLayout()

        layout.addRow("Student", self.Student)
        layout.addRow(self.generate_btn)
        self.setLayout(layout)


    def generate(self):
        self.generate_btn.setDisabled(True)
        data = {
            'Student': self.name_of_student.text(),
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
            #QMessageBox.information(self, "Finished", "PDF has been generated")




app = QApplication([])
w = Window()
w.show()
app.exec_()
