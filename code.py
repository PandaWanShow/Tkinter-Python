"""..."""
import os
import sys
from PySide2 import QtWidgets, QtGui
from tkinter import *

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
	def __init__(self, icon, parent=None, master=None):
		self.master = master
		QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
		self.setToolTip(f"Tooltip Name")
		menu = QtWidgets.QMenu(parent)
		open_app = menu.addAction("Open Program")
		open_app.triggered.connect(self.openApp)
		menu.addSeparator()
		
		exit_ = menu.addAction("Exit")
		exit_.triggered.connect(self.leave)
		menu.addSeparator()
		self.setContextMenu(menu)
		self.activated.connect(self.onTrayIconActivated)

		pass
	def leave(self):
		sys.exit()
	def onTrayIconActivated(self,reason):
		pass
	def openApp(self):
		self.hide()
		self.master.deiconify()
		pass

class Application:
	def __init__(self, master=None):
		super(Application, self).__init__()
		#Configs
		self.master = master
		self.tray_icon = SystemTrayIcon(QtGui.QIcon("icon.png"), self.w, self.master)#icon png
		self.app = QtWidgets.QApplication(sys.argv)
		self.w = QtWidgets.QWidget()
		self.master.protocol('WM_DELETE_WINDOW', self.exit_function)
		#TKinter Stuff Stuff





	def exit_function(self):
		self.master.withdraw()
		self.tray_icon.show()

def main():
	root = Tk()
	Application(root)
	root.mainloop()



if __name__=='__main__':
	main()
