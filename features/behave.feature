Feature: New Customer

  Scenario: Create New Customer
   Given form to create new customer
    When add customer to database
    Then Customer is stored in database
