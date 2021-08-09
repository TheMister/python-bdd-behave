Feature: Add New Movie

Scenario Outline: Title, Release Date, and Rating Fields are Valid or Blank
   Given I am logged in and on the add new movie page
   When I enter a <fieldstatus> title 
   And I enter a <fieldstatus> rating
   And I enter a <fieldstatus> release date
   And I click on submit
    Then I will see an upload <result> message

    Examples:
        | fieldstatus  | result  |
        | valid        | success |
        | blank        | failure |    

Scenario: Title Field Validation over 200
   Given I am logged in and on the add new movie page
   When I enter a title with over 200 chars
   And I click on submit
    Then I will see an error for title with over 200 chars

Scenario: Release Date Field Validation under 1/10/2015
   Given I am logged in and on the add new movie page
   When I enter a release date greater than 1/10/2015
   And I click on submit
    Then I will see an error for release date under than 1/10/2015
    
Scenario: Rating Field Validation over 5
   Given I am logged in and on the add new movie page
   When I enter a title with over 200 chars
   And I click on submit
    Then I will see an error for title with over 200 chars