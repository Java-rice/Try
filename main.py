#Required Libraries
#Required Libraries
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

Builder.load_file('layout.kv')

#Screens
#Screens
class LogoScreen(Screen):
	pass


#MAIN APPLICATION
class YourExpense(MDApp):
	def build(self):
		global sc_manager
		sc_manager = ScreenManager()
		sc_manager.add_widget(LogoScreen(name="Logo_Page"))
		return sc_manager



#MAIN FUNCTION
if __name__ == '__main__':

	#WINDOW SIZE
	Window.size = (360, 640)

	#RUN THE MAIN APPLICATION
	YourExpense().run()