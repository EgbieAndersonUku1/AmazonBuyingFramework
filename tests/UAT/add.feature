Feature: In order to use Amazon the user must login

  Scenario: Login to amazon successful
    Given the user has the correct credentials and successfully logs in
    When the users adds book to 'Experiences of Test Automation: Case Studies of Software Test Automation' to cart
    When the users adds book to 'Agile Testing: A Practical Guide for Testers and Agile Teams' to cart
    When the users adds book to 'Selenium WebDriver 3 Practical Guide' to the cart
    When the users selects the 'Save For Later' option for 'Experiences of Test Automation'
    When the users selects the 'Delete' option for 'Agile Testing'
    When then increases the quantity of the basket for 'Selenium WebDriver 3 Practical Guide' by 3 copies
    When the user marks 'Selenium WebDriver 3' as a gift
    Then the user deletes all copies of 'Selenium WebDriver 3' from the cart


