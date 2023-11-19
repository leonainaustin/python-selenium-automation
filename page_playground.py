class Page:

    def open_url(self):
        print('Opening url')

    def click(self):
        print('Clicking..')

    def input(self, text):
        print(f'Inputing text {text}...')

class Login (Page):

    def login(selfself, email, pw):
        print(f'Logging in as {email}, {pw}')

page = Page()
page.open_url()
login_page = Login()
login_page.open_url()
login_page.login('test@example.com', '12345')