class HomePage:
    def __init__(self, page):
        self.page = page
        self.search_input = "input[name='q']"

    def open(self):
        self.page.goto("https://openlibrary.org")

    def search(self, text: str):
        self.page.fill(self.search_input, text)
        self.page.press(self.search_input, "Enter")
