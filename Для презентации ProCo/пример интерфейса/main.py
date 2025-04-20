from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.utils import get_color_from_hex

class PortfolioApp(App):
    def build(self):
        Window.minimum_width = dp(800)
        Window.minimum_height = dp(600)

        root = FloatLayout()

        # Левая колонка (Портфолио)
        left_col = BoxLayout(
            orientation='vertical',
            size_hint=(0.3, 0.8),
            pos_hint={'x': 0.05, 'top': 0.9},
            spacing=10
        )

        for _ in range(5):
            item = BoxLayout(
                orientation='vertical',
                size_hint_y=None,
                height=dp(100),
                spacing=5
            )
            item.add_widget(Label(
                text='Портфолио',
                font_size=dp(24),
                bold=True
            ))
            item.add_widget(Label(
                text='Е',
                font_size=dp(48)),
                bold=True
            )
            left_col.add_widget(item)

        # Центральная колонка (Информация)
        center_col = BoxLayout(
            orientation='vertical',
            size_hint=(0.3, 0.8),
            pos_hint={'x': 0.35, 'top': 0.9},
            spacing=10
        )

        info = [
            'Имя фамилия', 'Отчество',
            'Номер телефона', 'Почта',
            'Дата рождения'
        ]
        for text in info:
            center_col.add_widget(Label(
                text=text,
                font_size=dp(18)),
                halign='left',
                size_hint_y=None,
                height=dp(40)
            )

        # Правая колонка (Теги и контакты)
        right_col = BoxLayout(
            orientation='vertical',
            size_hint=(0.25, 0.8),
            pos_hint={'right': 0.95, 'top': 0.9},
            spacing=20
        )

        tags = BoxLayout(
            orientation='vertical',
            spacing=10
        )
        for i in range(1, 4):
            tags.add_widget(Label(
                text=f'[b]Тег {i}[/b]',
                markup=True,
                font_size=dp(16)),
                halign='left'
            )

        contacts = BoxLayout(
            orientation='vertical',
            spacing=10
        )
        contacts.add_widget(Label(text='telegram', font_size=dp(16)))
        contacts.add_widget(Label(text='WhatsApp', font_size=dp(16)))
        contacts.add_widget(Label(
            text='Описание',
            font_size=dp(14)),
            color=get_color_from_hex('#666666')
        )

        right_col.add_widget(tags)
        right_col.add_widget(contacts)

        root.add_widget(left_col)
        root.add_widget(center_col)
        root.add_widget(right_col)

        return root

if __name__ == '__main__':
    PortfolioApp().run()
