from time import sleep
from pathlib import Path
from selene import browser, have, be, by


def test_send_practice_form():
    browser.open('/automation-practice-form')
    # browser.driver.execute_script("$('#fixedban').remove()")
    # browser.driver.execute_script("$('footer').remove()")

    # Inputs
    name = 'Bob'
    surname = 'Dylan'
    email = 'BobbyD123@gmail.com'
    phone_number = '1135485499'
    day, month, year = '16', 'July', '2007'
    subject = 'Maths'
    file_name = 'attachment.txt'
    address = '433 Barry Village Suite 631'
    state, city = 'NCR', 'Delhi'

    # Filling
    browser.element('#firstName').should(be.blank).type(name)
    browser.element('#lastName').should(be.blank).type(surname)
    browser.element('#userEmail').should(be.blank).type(email)
    browser.element('#gender-radio-1 + label').click()
    browser.element('#userNumber').should(be.blank).type(phone_number)

    #
    browser.element("input[type='file']").send_keys(f"{Path(__file__).parent.parent}\\resource\\{file_name}")

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__header').element('.react-datepicker__month-select').element(by.text(month)).click()
    browser.element('.react-datepicker__header').element('.react-datepicker__year-select').element(by.text(year)).click()
    browser.element('.react-datepicker__month > div:nth-child(3)').element(by.text(day)).click()
    browser.element('#subjectsInput').type(subject[:2])
    sleep(0.2)
    browser.element(by.text(subject)).click()
    browser.element('#hobbies-checkbox-3 + label').click()
    browser.element('#currentAddress').should(be.blank).type(address)
    browser.element('#state').click().element(by.text(state)).click()
    browser.element('#city').click().element(by.text(city)).click()
    browser.element('#submit').click()

    #  Assertions
    browser.element('.table-responsive > table > tbody > tr:nth-child(1) > td:nth-child(2)').should(have.exact_text(f'{name} {surname}'))
    browser.element('.table-responsive > table > tbody > tr:nth-child(2) > td:nth-child(2)').should(have.exact_text(email))
    browser.element('.table-responsive > table > tbody > tr:nth-child(3) > td:nth-child(2)').should(have.exact_text('Male'))
    browser.element('.table-responsive > table > tbody > tr:nth-child(4) > td:nth-child(2)').should(have.exact_text(phone_number))
    browser.element('.table-responsive > table > tbody > tr:nth-child(5) > td:nth-child(2)').should(have.exact_text(f'{day} {month},{year}'))
    browser.element('.table-responsive > table > tbody > tr:nth-child(6) > td:nth-child(2)').should(have.exact_text(subject))
    browser.element('.table-responsive > table > tbody > tr:nth-child(7) > td:nth-child(2)').should(have.exact_text('Music'))
    browser.element('.table-responsive > table > tbody > tr:nth-child(8) > td:nth-child(2)').should(have.exact_text(f'{file_name}'))
    browser.element('.table-responsive > table > tbody > tr:nth-child(9) > td:nth-child(2)').should(have.exact_text(address))
    browser.element('.table-responsive > table > tbody > tr:nth-child(10) > td:nth-child(2)').should(have.exact_text(f'{state} {city}'))

