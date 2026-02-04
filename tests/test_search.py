import pytest
from pages.home_page import HomePage
from pages.results_page import ResultsPage


@pytest.mark.smoke
def test_search_book_by_title(page):
    home = HomePage(page)
    results = ResultsPage(page)

    home.open()
    home.search("Harry Potter")

    results.wait_for_results()
    assert results.results_count() > 0


@pytest.mark.regression
def test_search_with_no_results(page):
    home = HomePage(page)
    results = ResultsPage(page)

    home.open()
    home.search("asdasdasdqweqwe")

    assert results.results_count() == 0


@pytest.mark.regression
def test_search_with_empty_inputs(page):
    home = HomePage(page)
    results = ResultsPage(page)

    home.open()
    home.search("   ")

    assert results.results_count() == 0
