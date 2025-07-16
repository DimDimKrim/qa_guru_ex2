from selene import browser, be, have
import allure

@allure.feature('Некорректный поиск')
@allure.story('Проверка некорректного ввода данных')
def test_no_match():
    browser.element('[name="q"]').should(be.visible).type("adsdasвышгрфыш!№;%га561253!").press_enter()
    browser.element('[class="gSXOPxXJQAIpv4HDaDFd"]').should(have.text('По запросу «adsdasвышгрфыш!№;%га561253!» ничего не найдено.'))





