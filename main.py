
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivymd.uix.button import MDFlatButton
#=================================================

from kivy.uix.screenmanager import NoTransition

from kivy.clock import mainthread, Clock

#=================================================

import mysql.connector as mycon

import threading
import time
import random
import urllib.request
from kivmob import KivMob, TestIds

#=================================================

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
#=================================================


Builder.load_file("./UI/home.kv")
Builder.load_file("./UI/geeta.kv")
Builder.load_file("./UI/main.kv")


class geetaScreen(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.removable = []

		self.posLast = []

		self.firstOpen = ["Aa¨vq - 010"]

		# self.ids.trnbtn.on_press = lambda: self.translation()
		# self.widget = False

		self.ids.connecting.ads = KivMob("ca-app-pub-5298450838824386/6805873151")
		self.ids.connecting.ads.new_banner("ca-app-pub-5298450838824386/6805873151", top_pos=True)
		self.ids.connecting.ads.request_banner()
		self.ids.connecting.ads.show_banner()

		logThread = threading.Thread(target=self.logDB)
		logThread.start()
		self.colorDef = Clock.schedule_interval(self.colorfulDef, 0.04)
		self.color_i = 0
		try:
			self.ids.loading.text_color = "#"+hex(random.randrange(0, 2**24))[2:]
		except:
			pass
		self.startUp = True

	def colorfulDef(self, *args):
		if self.startUp:
			texts = ['L', 'o', 'a', 'd', 'i', 'n', 'g', ' ', 'P', 'l', 'e', 'a', 's', 'e', ' ', 'W', 'a', 'i', 't', '.', '.', '.', '.', '.', '.', '.'] #26
			try:
				self.ids.loading.text = self.ids.loading.text + texts[int(self.color_i)]
			except:
				pass
			self.color_i +=1

			if self.color_i >= 50:
				self.ids.loading.text = ''
				try:
					self.ids.loading.text_color = "#"+hex(random.randrange(0, 2**24))[2:]
				except:
					pass
				self.color_i = 0
		else:
			texts = ['P', 'l', 'e', 'a', 's', 'e', ' ', 'c', 'h', 'e', 'c', 'k', ' ', 'y', 'o', 'u', 'r', ' ', 'i', 'n', 't', 'e', 'r', 'n', 'e', 't', ' ', 'c', 'o', 'n', 'n', 'e', 'c', 't', 'i', 'o', 'n', '.', '.'] #38
			try:
				self.ids.loading.text = self.ids.loading.text + texts[int(self.color_i)]
			except:
				pass
			self.color_i +=1

			if self.color_i >= 60:
				self.ids.loading.text = ''
				try:
					self.ids.loading.text_color = "#"+hex(random.randrange(0, 2**24))[2:]
				except:
					pass
				self.color_i = 0


		pass


	def logDB(self):
		try:
			self.mydb = mycon.connect(host="www.db4free.net", user="sh1de_geeta_x", password="Geeta#@0987", database="sh1de_geeta_x")
			self.mainSteam()
		except Exception as e:
			print(e)
			self.ids.loading.text = "Internet Not Connected"
			self.colorDef.cancel()

	@mainthread

	def logDB2(self, x):
		self.add_widget(self.ids.connecting)
		try:
			self.mydb = mycon.connect(host="www.db4free.net", user="sh1de_geeta_x", password="Geeta#@0987", database="sh1de_geeta_x")
			self.logVerify(x)
		except Exception as e:
			self.ids.loading.text = "Checking Internet Connection"
			self.logVerify(x)
			time.sleep(3)
	@mainthread

	def mainSteam(self):
		self.chaptersName = ["mskq-welv` †hvM", "Kg©wRÁvmv", "kÎæwebvk ‡cªiYv", "hÁKg© ¯úóxKiY", "hÁ‡fv³v gnvcyiæl¯’ g‡nk¦i",
							"Af¨vm ‡hvM", "mgMª †eva", "Aÿi eªþ‡hvM", "ivRwe`¨v RvM„wZ", "wef~wZ eY©b", "wek¦iƒc `k©b †hvM",
							"fw³‡hvM", "‡ÿÎ-‡ÿÎÁ wefvM †hvM", "¸YÎq wefvM †hvM", "cyiæ‡lvËg †hvM", "‰`evmyi m¤ú`& wefvM †hvM",
							"Iu Zrmr I kª×vÎq wefvM †hvM", "mbœvm †hvM", ]

		self.chapters = ["Aa¨vq - 01=46", "Aa¨vq - 02=72", "Aa¨vq - 03=43", "Aa¨vq - 04=42", "Aa¨vq - 05=29", "Aa¨vq - 06=47",
						"Aa¨vq - 07=30", "Aa¨vq - 08=28", "Aa¨vq - 09=34", "Aa¨vq - 10=42", "Aa¨vq - 11=55", "Aa¨vq - 12=20",
						"Aa¨vq - 13=35", "Aa¨vq - 14=27", "Aa¨vq - 15=20", "Aa¨vq - 16=24", "Aa¨vq - 17=28", "Aa¨vq - 18=78"]

		for i in self.chapters:
			btn = MDFlatButton(text=str(i.partition("=")[0]), size_hint_y=None, height=40, ripple_scale=0,
								md_bg_color=[1, 1, 1, 0.02], size_hint=[1, None], theme_text_color="Custom",
								text_color="#00b9fc", font_size="26dp", font_name="./Fonts/DestinyMJ-Bold.ttf",
								on_press=lambda event, x=str(i): self.chapterButtons(x))
			self.ids[str(i)] = btn

			self.ids.chapterAdd.add_widget(btn)
		
		self.chapterButtons("Aa¨vq - 01=46")

		self.color("Aa¨vq - 01_1")

		self.colorDef.cancel()
		self.ids.loading.text = ""
		self.startUp = False

	def chapterButtons(self, x):
		self.num = str(x.partition(" ")[2])[2:4]
		 # Chapter Name Header
		self.ids.displayText.text = self.chaptersName[int(x[8:10]) - 1]

		# Chapter Buttons Colors
		for i in self.chapters:
			self.ids[i].md_bg_color = [1, 1, 1, 0.02]
			self.ids[i].text_color = "#00b9fc"
		# Button Colors
		self.ids[x].md_bg_color = [0 / 255, 187 / 255, 255 / 255, 0.8]
		self.ids[x].text_color = "#000000"

		# remove all buttons for new creations
		try:
			for i in self.removable:
				self.ids.slok_add.remove_widget(self.ids[i])
		except:
			pass

		# Clean Values of removables
		self.removable = []

		# Slokas Number generate and id assign
		for i in range(int(x.partition("=")[2])):
			btn = MDFlatButton(text=str(i + 1), size_hint_y=None, height=40, ripple_scale=0,
								md_bg_color=[1, 1, 1, 0.02], size_hint=[1, None], theme_text_color="Custom",
								text_color="#00b9fc", font_size="24dp", font_name="./Fonts/DestinyMJ-Bold.ttf",
								on_press=lambda event, x=f'{x.partition("=")[0]}_{str(i+1)}': self.color(x))

			self.ids[f'{x.partition("=")[0]}_{str(i+1)}'] = btn

			self.ids.slok_add.add_widget(btn)

			self.removable.append(f'{x.partition("=")[0]}_{str(i+1)}')

		if x.partition("=")[0] in self.posLast:
			try:
				self.color(str(self.firstOpen[0]))

				val = str(str(self.firstOpen[0]).partition(
					" ")[2]).partition(" ")[2]

				val2 = str(self.firstOpen[0]).partition("_")[2]
				val3 = str(
					self.chapters[int(val.partition("_")[0]) - 1]).partition("=")[2]

				val4 = float(1) - float(float(val2) / float(val3))
				if val4 >= float(0.940000):
					self.ids.top.scroll_y = 1
				elif val4 <= float(0.150000):
					self.ids.top.scroll_y = 0
				else:
					self.ids.top.scroll_y = val4
			except:
				pass
		else:
			self.ids.top.scroll_y = 1

	def color(self, x):
		try:
			self.remove_widget(self.ids.connecting)
		except Exception as e:
			print(e)
		# Button Colors Removing
		for i in self.removable:
			self.ids[i].md_bg_color = [1, 1, 1, 0.02]
			self.ids[i].text_color = "#00b9fc"

		# Button Colors
		self.ids[x].md_bg_color = [0 / 255, 187 / 255, 255 / 255, 0.8]
		self.ids[x].text_color = "#000000"

		if self.firstOpen == x:
			pass
		else:
			self.firstOpen = []
			self.posLast = []
			self.firstOpen.append(x)
			self.posLast.append(x.partition("_")[0])

		dispnum = str(x.partition("-")[2])
		dispnum1 = dispnum.partition("_")[0]
		dispnum2 = str("0" + dispnum.partition("_")[2])[-2:]
		self.ids.displayNumber.text = f'{dispnum1}~{dispnum2}'

		verifyThread = threading.Thread(target=self.logVerify, args=(x,))
		verifyThread.start()

	def check_internet_connection(self):
		try:
			urllib.request.urlopen("https://www.google.com")
			return True
		except urllib.error.URLError:
			return False

	def logVerify(self, x):
		y = x
		self.values = str(y)
		if self.check_internet_connection():
			try:
				self.mycursor = self.mydb.cursor()
				self.mycursor.execute("select * from geeta_X where chapterDB='"+ x.partition("_")[0] +"'")
				self.result1 = self.mycursor.fetchone()
				self.displaySlokas(x)
				self.colorDef.cancel()
			except Exception as e:
				pass
		else:
			self.displaySlokas("Error")
			self.colorDef()

	@mainthread

	def displaySlokas(self, x):
		if x == "Error":
			try:
				self.add_widget(self.ids.connecting)
				self.remove_widget(self.ids.mainNavigation)
				self.ids.loading.text = ""
			except:
				pass
			verifyThread1 = threading.Thread(target=self.logVerify, args=(self.values,))
			verifyThread1.start()
		else:
			try:
				self.remove_widget(self.ids.connecting)
			except:
				pass
			try:
				self.add_widget(self.ids.mainNavigation)
			except:
				pass
			print(self.result1)
			btnList = ["evsjv", "sanskrit"]
			for i in btnList:
				try:
					self.ids.dspl.remove_widget(self.ids[str(i)])
				except:
					pass
			for i in btnList:
				lbl = MDLabel(text='`„l&U¡v Zy cvÐevbxKs e~¨ps `y‡h©vab¯Í`v|\nAvPvh©gycm½g¨ ivRv ePbgeªexr|', size_hint=[1, 1], halign="center", theme_text_color="Custom")
				self.ids[str(i)] = lbl
				self.ids["evsjv"].font_name="./Fonts/DestinyMJ-Bold.ttf"
				self.ids["evsjv"].font_size = "24dp"
				self.ids["evsjv"].text_color = [255/255, 255/255, 0, 0.9]


			self.ids.dspl.add_widget(self.ids["evsjv"])

			# self.ids.mainText.text = self.result1[3]
			print(self.ids.mainText.height)
			if int(self.ids.mainText.height) <=355:
				self.ids.textScroll.do_scroll_y = False
			else:
				self.ids.textScroll.do_scroll_y = True



class ContentNavigationDrawer(MDBoxLayout):
	pass


class mainScreen(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.removable = []

		self.books = ["Ramayana", "Mahabharata",
					  "Bhagwat Geeta", "Bhagwat Geeta1", "Bhagwat Geeta2"]

		# if len(self.books) >=7:
		# 	self.ids.sv.do_scroll_y = True
		# else:
		# 	self.ids.sv.do_scroll_y = False

		for i in self.books:
			btn = MDFlatButton(text=str(i), size_hint=[1, 1], md_bg_color=[1, 1, 1, 0.02],
								ripple_scale=0, on_press=lambda event, x=str(i): self.color(x))
			self.ids[str(i)] = btn

			# self.ids[str(i)].height = 64

			self.ids.mainLayout.add_widget(btn)

			self.removable.append(str(i))

		print(self.ids[str(i)].height)
		print(self.ids[str(i)].width)

	def color(self, x):
		# Button Colors Removing
		for i in self.removable:
			self.ids[i].md_bg_color = [1, 1, 1, 0.02]
			self.ids[i].text_color = "#00b9fc"

		# Button Colors
		self.ids[x].md_bg_color = [0 / 255, 187 / 255, 255 / 255, 0.8]
		self.ids[x].text_color = "#000000"


class homeScreen(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)


class MainApp(MDApp):
	def build(self):
		self.title = "Sanatan - The Truth"
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "DeepOrange"

		self.manager = ScreenManager()
		self.manager.add_widget(homeScreen(name="home"))
		self.manager.add_widget(mainScreen(name="main"))
		self.manager.add_widget(geetaScreen(name="geeta"))

		Window.size = (360, 640)
		self.manager.transition = NoTransition()
		self.manager.current = "geeta"
		return self.manager


if __name__ == "__main__":
	MainApp().run()
