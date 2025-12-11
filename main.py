from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import random
import json
import os

DATA_FILE = 'jokes.json'

def load_jokes():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return ["مرة اثنين على الدراجة..", "مرة واحد نسي مفاتيحه.."]

def save_joke(joke):
    jokes = load_jokes()
    jokes.append(joke)
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(jokes, f, ensure_ascii=False, indent=2)

class JokesUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.label = Label(text='اضغط عرض نكتة', size_hint_y=0.6)
        self.add_widget(self.label)

        btn_box = BoxLayout(size_hint_y=0.2)
        btn_show = Button(text='عرض نكتة')
        btn_add = Button(text='إضافة نكتة')
        btn_box.add_widget(btn_show)
        btn_box.add_widget(btn_add)
        self.add_widget(btn_box)

        self.input = TextInput(hint_text='اكتب نكتة هنا', size_hint_y=0.2, multiline=True)
        self.add_widget(self.input)

        btn_show.bind(on_release=self.show_joke)
        btn_add.bind(on_release=self.add_joke)

    def show_joke(self, *args):
        jokes = load_jokes()
        self.label.text = random.choice(jokes)

    def add_joke(self, *args):
        text = self.input.text.strip()
        if text:
            save_joke(text)
            self.input.text = ''
            self.label.text = 'تم إضافة النكتة'

class JokesApp(App):
    def build(self):
        return JokesUI()

if __name__ == '__main__':
    JokesApp().run()
