class ResultsPage:
    def __init__(self, page):
        self.page = page
        self.result_items = ".searchResultItem"

    def wait_for_results(self):
        self.page.wait_for_selector(self.result_items)

    def results_count(self) -> int:
        return self.page.locator(self.result_items).count()

    def has_results(self) -> bool:
        return self.result_count() > 0

        