#Search for coffee
 Feature: Search Target Cart
#
   Scenario: User can add product in cart
     Given Open target home page
     When Search for mug
     Then Add a mug into cart
    And Click on the cart
     And Verify cart item 1