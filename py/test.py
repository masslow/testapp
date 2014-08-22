import npyscreen
class MainForm(npyscreen.FormBaseNew):
	
	def while_waiting(self):

		if self.veduokle.get_value() == [0]:
			self.tarp.value = 'Tarpas'
		if self.veduokle.get_value() == [1]:
			self.tarp.value = 'Frontas'
				
		self.display()
		
	def create(self):
		self.koordx = self.add(npyscreen.TitleText, name = 'X:', relx = 19, rely = 2, width=12, begin_entry_at=5)
		self.koordy = self.add(npyscreen.TitleText, name = 'Y:', relx = 19, rely = 3, width=12, begin_entry_at=5)
		self.rodatstumas = self.add(npyscreen.TitleText, name = 'Atstumas iki taikinio:', rely = 6, relx = 6, value = 3999, editable=False, begin_entry_at= 25)
		self.rodkoord = self.add(npyscreen.TitleText, name = 'Taikinio koordinates:', rely = 6, relx = 57, value = "1500   1233", editable=False, begin_entry_at= 24)
		self.stebx = self.add(npyscreen.TitleText, name = 'X:', relx = 62, rely = 2, width = 12, begin_entry_at=5)
		self.steby = self.add(npyscreen.TitleText, name = 'Y:', relx = 62, rely = 3, width = 12, begin_entry_at=5)
		self.kryptis = self.add(npyscreen.TitleText, name = 'Kryptis:', relx = 80, rely= 2, max_width=11, width = 11, begin_entry_at=12)
		self.atstumas = self.add(npyscreen.TitleText, name = 'Atstumas:', relx = 80, rely = 3, max_width=11, width = 12, begin_entry_at = 12)
		self.mina =  self.add(npyscreen.TitleSelectOne, max_height=4, value = [0], name="Mina", values = ["Skeveldrine","Apsvieciamoji", "Dumine"], scroll_exit=True, rely = 15, relx =4, begin_entry_at=12, max_width = 32)
		self.veduokle = self.add(npyscreen.TitleSelectOne, max_height=2, value = [0], name="Veduokle", values = ["Sutelkta","Isskleista"], scroll_exit=True, rely = 20, relx =4, begin_entry_at=12, max_width = 32)
		self.uztaisas = self.add(npyscreen.TitleSelectOne, max_height=9, value = [3], name="Uztaisas", values = ["Pirmas 800-1825m", "Antras 1000-2475m", "Trecias 1300-3275m", "Ketvirtas 1500-4000m", "Penktas 1800-4500m", "Sestas 2100-5200m", "Septintas 2300-5750m", "Astuntas 2500-6300m"], scroll_exit=True, rely = 24, relx =4, begin_entry_at=12, max_width = 40)
		self.tarp = self.add(npyscreen.TitleText, name = 'Tarpas', relx = 4, rely = 34, max_width=32, begin_entry_at = 17)
		self.koord = self.add(npyscreen.FixedText, value='Koordinates', relx = 4, max_width=14, rely =2, editable=False)
		self.steb = self.add(npyscreen.FixedText, value= 'Sekykla', relx = 50, rely = 2, max_width=12, editable=False)
		self.duomenys = self.add(npyscreen.BoxBasic, name = "Duomenys", values = ['testing'], rely = 10, relx = 50, max_width = 50, editable = False)
		
class MyApplication(npyscreen.NPSAppManaged):
	
	keypress_timeout_default = 3
	def onStart(self):
		N = self.addForm('MAIN', MainForm, name= 'Tampella 120mm')	
		N.edit()
	
	
	
if __name__ == '__main__':
	App = MyApplication().run()