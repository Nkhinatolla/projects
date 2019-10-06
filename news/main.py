import sys, re, urllib.request as urlreq,  html2text
import newsform 
from PyQt5 import QtCore, QtGui, QtWidgets
class MyWin(QtWidgets.QMainWindow):
	def __init__ (self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = newsform.Ui_MainWindow()
		self.ui.setupUi(self)
		self.newsurl=[]
		self.Parse()
		self.ui.pushButton.clicked.connect(self.AllNews)
	def Parse(self):
		s ='https://russian.rt.com'
		doc=urlreq.urlopen(s).read().decode('utf-8', errors='ignore')
		doc=doc.replace('\n', '')
		zagolovki=re.findall('<a class="link link_color" href="(.+?)"', doc)
		f = open("site", "w", encoding="utf-8") # html code в виде с string
		f.write(doc)
		f.close()
		for x in zagolovki: 
			print(x) # ссылки
			self.newsurl.append(x.split('">')[0])
			self.ui.listWidget.addItem(x.split('">')[1].strip())
					
	def AllNews(self):
		n=self.ui.listWidget.currentRow()
		u='http://russian.rt.com'+self.newsurl[n]
		doc=urlreq.urlopen(u).read().decode('utf-8', errors='ignore')
		h=html2text.HTML2Text()
		h.ignore_links=True
		h.body_width=False
		h.ignore_images=True
		doc=h.handle(doc)
		mas=doc,split('\n')
		stroka=''
		for x in mas:
			if(len(x)>120):
				stroka=stroka+x+'\n\n'
		self.ui.textEdit.setText(stroka)

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	myapp = MyWin()
	myapp.show()
	sys.exit(app.exec_()) 

