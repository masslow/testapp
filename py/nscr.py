#!/usr/bin/env python
# encoding: utf-8
 
import npyscreen

class App(npyscreen.NPSApp):
	def main(self):
	
		F = npyscreen.Form(name = "Tampella 120mm ugnies koregavimas")
		F.edit()
        
		
if __name__ == '__main__':
	Ap = App()
	Ap.run()