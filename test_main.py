from selene import browser, be, have


def test_no_match():
    browser.element('[name="text"]').should(be.visible).type("trhurtmgerwumgrtuijmhtyiujmiougmetriohmrt").press_enter()
    browser.element('.misspell__message, .serp-404__title').should(have.text('Ничего не нашли'))



