Feature: User functions
  
  Scenario: User logs in as reviewer
    Given User is at main page
    When he clicks on "Log in"
    And fills correctly Name with password
    And clicks on "Log in"
    Then he should log in

  
  Scenario: User searches for private Use Case
    Given the User is at main page
    When he tries to open header "Use Cases"
    Then the Use Case in the list should not be visible
    
    
  Scenario: User wants to log out
    Given User wants to log out
    When he clicks on "its Reviewer"
    And clicks on "Log out"
    Then he should be logged out
