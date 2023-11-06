#Search for coffee
 Feature: Search Target Cart
#
   Scenario: User can add product in cart
     Given Open target home page
     When Search for black mouse
     Then Click on add to cart first product
     And Click on View cart and Check out
     And Verify cart