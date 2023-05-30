from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
import BaseModel
import readcsv
import MailchimpProcessorApp
from LEADUtils import LEADPrinter

# Display Pixles

class MainApp(MDApp):
	def build(self):

		# Define Screen
		screen = Screen()

		leadPrinter = LEADPrinter()
		leads = []
		leads = leadPrinter.datatabledata()
		
		print('\n===== before =====\n')
		#bank.show_accounts(show_history=True)

		

		print('\n===== after =====\n')
		#bank.show_accounts(show_history=True)

		# Define Table
		table = MDDataTable(
			pos_hint = {'center_x': 0.5, 'center_y': 0.5},
			size_hint =(0.9, 0.6),
			check = True,
			column_data = [
				("FirstName", dp(40)),
				("LastName", dp(25)),
				("PhoneNumber", dp(25)),
				("Email", dp(25)),
				#("Amount", dp(25))
			],
			row_data = leads


			)
		
		# Bind the table
		table.bind(on_check_press=self.checked)
		table.bind(on_row_press=self.row_checked)

		self.theme_cls.theme_style = "Light"
		self.theme_cls.primary_palette = "BlueGray"
		#return Builder.load_file('table.kv')
		# Add table widget to screen
		screen.add_widget(table)
		return screen
	
	# Function for check presses
	def checked(self, instance_table, current_row):
		print(instance_table, current_row)
	# Function for row presses
	def row_checked(self, instance_table, instance_row):
		print(instance_table, instance_row)

	
#bt = BankTransfer.Bank()
#print("*"*30)

MainApp().run()