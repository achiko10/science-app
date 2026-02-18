from typing import Any, Dict, List
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.text import LabelBase
from kivy.core.window import Window

# ფონტის რეგისტრცია პროექტის საქაღალდიდან
try:
    LabelBase.register(name="Sylfaen", fn_regular="font.ttf")
except:
    pass

Window.size = (400, 700)

class MainMenu(Screen):
    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        layout.add_widget(Label(text="სამეცნიერო პორტალი", font_name="Sylfaen", font_size='28sp', bold=True))
        
        btn_lib = Button(text="ბიბლიოთეკა", font_name="Sylfaen", size_hint_y=0.2, background_normal='', background_color=(0.1, 0.4, 0.7, 1))
        btn_lib.bind(on_release=lambda x: setattr(self.manager, 'current', 'library')) # type: ignore
        
        btn_quiz = Button(text="სამეცნიერო ქვიზი", font_name="Sylfaen", size_hint_y=0.2, background_normal='', background_color=(0.1, 0.6, 0.3, 1))
        btn_quiz.bind(on_release=lambda x: setattr(self.manager, 'current', 'quiz')) # type: ignore
        
        layout.add_widget(btn_lib)
        layout.add_widget(btn_quiz)
        self.add_widget(layout)

class LibraryScreen(Screen):
    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)
        self.main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        nav = BoxLayout(size_hint_y=None, height=60, spacing=10)
        back = Button(text="<", size_hint_x=0.2, background_color=(0.7, 0.2, 0.2, 1), background_normal='')
        back.bind(on_release=lambda x: setattr(self.manager, 'current', 'menu')) # type: ignore
        nav.add_widget(back)
        self.title_label = Label(text="მეცნიერების დარგები", font_name="Sylfaen", font_size='20sp')
        nav.add_widget(self.title_label)
        self.main_layout.add_widget(nav)
        self.scroll = ScrollView()
        self.grid = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter('height')) # type: ignore
        self.data: Dict[str, List[str]] = {
            "ფიზიკა": ["კვანტური მექანიკა", "ფარდობითობა", "თერმოდინამიკა", "ბირთვული ფიზიკა"],
            "ბიოლოგია": ["გენეტიკა", "მოლეკულური ბიოლოგია", "ევოლუცია", "ეკოლოგია"],
            "ქიმია": ["ორგანული ქიმია", "ბიოქიმია", "არაორგანული ქიმია", "ანალიზური ქიმია"],
            "ასტრონომია": ["შავი ხვრელები", "მზის სისტემა", "გალაქტიკები", "კოსმოლოგია"],
            "მათემატიკა": ["ალგებრა", "გეომეტრია", "ანალიზი", "ალბათობა"],
            "მედიცინა": ["ანატომია", "ნეიროლოგია", "ვირუსოლოგია", "ფსიქიატრია"],
            "ტექნოლოგია": ["AI", "რობოტიკა", "ბლოკჩეინი", "კიბერუსაფრთხოება"],
            "ფსიქოლოგია": ["კოგნიტური", "სოციალური", "ბავშვის ფსიქოლოგია"],
            "გეოლოგია": ["ტექტონიკა", "მინერალოგია", "ვულკანოლოგია"],
            "არქეოლოგია": ["ეგვიპტოლოგია", "ანთროპოლოგია", "უძველესი კულტურა"]
        }
        self.show_categories()
        self.scroll.add_widget(self.grid)
        self.main_layout.add_widget(self.scroll)
        self.add_widget(self.main_layout)

    def show_categories(self):
        self.grid.clear_widgets()
        for cat in self.data.keys():
            btn = Button(text=cat, font_name="Sylfaen", size_hint_y=None, height=70, background_normal='', background_color=(0.2, 0.2, 0.25, 1))
            btn.bind(on_release=lambda x, c=cat: self.show_sub(c)) # type: ignore
            self.grid.add_widget(btn)

    def show_sub(self, cat):
        self.grid.clear_widgets()
        back = Button(text=".. უკან", font_name="Sylfaen", size_hint_y=None, height=60, background_color=(0.4, 0.4, 0.4, 1), background_normal='')
        back.bind(on_release=lambda x: self.show_categories()) # type: ignore
        self.grid.add_widget(back)
        for sub in self.data[cat]:
            self.grid.add_widget(Button(text=sub, font_name="Sylfaen", size_hint_y=None, height=65, background_normal='', background_color=(0.3, 0.4, 0.5, 1)))

class QuizScreen(Screen):
    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        self.questions = [
            ("რა არის წყლის ფორმულა?", ["H2O", "CO2", "O2"], 0),
            ("ვინ აღმოაჩინა გრავიტაცია?", ["ნიუტონმა", "აინშტაინმა", "ტესლამ"], 0),
            ("რომელი პლანეტაა მზესთან ახლოს?", ["მერკური", "ვენერა", "მარსი"], 0),
            ("რა არის უჯრედის ენერგია?", ["მიტოქონდრია", "ბირთვი", "რიბოსომა"], 0),
            ("რა არის სინათლის სიჩქარე?", ["300k კმ/წმ", "150k კმ/წმ", "500k კმ/წმ"], 0),
            ("რამდენი ატომია O2-ში?", ["2", "1", "3"], 0),
            ("ვინ შექმნა პერიოდულობა?", ["მენდელეევმა", "კიურიმ", "ნობელმა"], 0),
            ("დედამიწის თანამგზავრი?", ["მთვარე", "მზე", "მარსი"], 0),
            ("ცხოველების მეცნიერება?", ["ზოოლოგია", "ბოტანიკა", "გეოლოგია"], 0),
            ("ატომის დადებითი ნაწილაკი?", ["პროტონი", "ნეიტრონი", "ელექტრონი"], 0)
        ]
        self.current_q = 0
        self.score = 0
        self.label = Label(text="", font_name="Sylfaen", font_size='22sp', size_hint_y=0.4)
        self.layout.add_widget(self.label)
        self.btns = []
        for i in range(3):
            b = Button(text="", font_name="Sylfaen", size_hint_y=None, height=60, background_normal='', background_color=(0.1, 0.5, 0.5, 1))
            b.bind(on_release=self.check) # type: ignore
            self.btns.append(b)
            self.layout.add_widget(b)
        self.add_widget(self.layout)
        self.update()

    def update(self):
        if self.current_q < 10:
            q, opts, _ = self.questions[self.current_q]
            self.label.text = f"კითხვა {self.current_q+1}/10\n\n{q}"
            for i in range(3): self.btns[i].text = opts[i]
        else:
            self.label.text = f"თამაში მორჩა!\nქულა: {self.score}/10"
            for b in self.btns: self.layout.remove_widget(b)
            home = Button(text="მთავარი", font_name="Sylfaen", size_hint_y=None, height=60, background_color=(0.1, 0.4, 0.8, 1), background_normal='')
            home.bind(on_release=lambda x: setattr(self.manager, 'current', 'menu')) # type: ignore
            self.layout.add_widget(home)

    def check(self, inst):
        if inst.text == self.questions[self.current_q][1][self.questions[self.current_q][2]]:
            self.score += 1
        self.current_q += 1
        self.update()

class ScienceApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu(name='menu'))
        sm.add_widget(LibraryScreen(name='library'))
        sm.add_widget(QuizScreen(name='quiz'))
        return sm

if __name__ == "__main__":

    ScienceApp().run()
