#using material design widget with kivy
"""
Project name: IIhem Project
Requirements: kivy and kivymd, Python3
"""
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.gridlayout import MDGridLayout
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.datatables import MDDataTable

Builder.load_file("kv/home.kv")
Builder.load_file("kv/user.kv")
class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
class HomeScreen(Screen):
	pass
class UserScreen(Screen):
    def on_enter(self, *args):
        layout = AnchorLayout()
        self.data_tables = MDDataTable(
            size_hint=(0.7, 0.6),
            use_pagination=True,
            check=True,
            column_data=[
                ("No.", dp(30)),
                ("Status", dp(30)),
                ("Signal Name", dp(60), self.sort_on_signal),
                ("Severity", dp(30)),
                ("Stage", dp(30)),
                ("Schedule", dp(30), self.sort_on_schedule),
                ("Team Lead", dp(30), self.sort_on_team),
            ],
            row_data=[
                (
                    "1",
                    ("alert", [255 / 256, 165 / 256, 0, 1], "No Signal"),
                    "Astrid: NE shared managed",
                    "Medium",
                    "Triaged",
                    "0:33",
                    "Chase Nguyen",
                ),
                (
                    "2",
                    ("alert-circle", [1, 0, 0, 1], "Offline"),
                    "Cosmo: prod shared ares",
                    "Huge",
                    "Triaged",
                    "0:39",
                    "Brie Furman",
                ),
                (
                    "3",
                    (
                        "checkbox-marked-circle",
                        [39 / 256, 174 / 256, 96 / 256, 1],
                        "Online",
                    ),
                    "Phoenix: prod shared lyra-lists",
                    "Minor",
                    "Not Triaged",
                    "3:12",
                    "Jeremy lake",
                ),
                (
                    "4",
                    (
                        "checkbox-marked-circle",
                        [39 / 256, 174 / 256, 96 / 256, 1],
                        "Online",
                    ),
                    "Sirius: NW prod shared locations",
                    "Negligible",
                    "Triaged",
                    "13:18",
                    "Angelica Howards",
                ),
                (
                    "5",
                    (
                        "checkbox-marked-circle",
                        [39 / 256, 174 / 256, 96 / 256, 1],
                        "Online",
                    ),
                    "Sirius: prod independent account",
                    "Negligible",
                    "Triaged",
                    "22:06",
                    "Diane Okuma",
                ),
            ],
            sorted_on="Schedule",
            sorted_order="ASC",
            elevation=2,
        )
        self.data_tables.bind(on_row_press=self.on_row_press)
        self.data_tables.bind(on_check_press=self.on_check_press)
        layout.add_widget(self.data_tables)
        lb = MDLabel(
			text="[b]Manage users[/b]",
			size_hint=(1,None),
			markup=True,
			halign="justify",
			font_size="20sp",
            font_style='H5',
			size=("20sp","20sp"))
        self.ids.box.add_widget(lb)
        self.ids.box.add_widget(layout)

    def on_row_press(self, instance_table, instance_row):
        """Called when a table row is clicked."""
        print(instance_table, instance_row)
    def on_check_press(self, instance_table, current_row):
        """Called when the check box in the table row is checked."""
        print(instance_table, current_row)
    def sort_on_signal(self, data):
        return sorted(data, key=lambda l: l[2])
    def sort_on_schedule(self, data):
        return sorted(
            data,
            key=lambda l: sum(
                [int(l[-2].split(":")[0]) * 60, int(l[-2].split(":")[1])]
            ),
        )
    def sort_on_team(self, data):
        return sorted(data, key=lambda l: l[-1])

class ScreenManagement(ScreenManager):
	pass
class Bulgin(MDGridLayout):
	def get_widget_of_id(self, *args):
		return self.ids[args[0]]
class MainApp(MDApp):
	def build(self):
		mainscreen = Builder.load_file("kv/main.kv")
		return mainscreen
	def on_start(self):
		"""
		you can comment this line to have a modal navlayout
		"""
		app.root.ids.nav_drawer.type = "standard"
if __name__ == "__main__":
	app = MainApp()
	app.run()
