Feature: Producers functions

  Scenario: Admin Log In
    Given admin wants to log in
    When admin fills name and password and enters
    Then he should be logged in 
    
  
  
  Scenario: Create Use Case
    Given admin is logged in 
    When admin clicks "Add new"
    And clicks on Use Case
    And fills the Use Case form
    And clicks on "Save" button
    Then new Use Case should be created
    
    
  Scenario: Publish Use Case
    Given a new Use Case has been created
    When admin clicks on the private Use Case
    And clicks on "State"
    And clicks on "Publish"
    Then the Use Case should be publicly visible
    
  
  Scenario: Create Tool
    Given admin is logged in 
    When admin clicks "Add new"
    And clicks on Tool
    And fills the Tool form
    And clicks on "Save" button
    Then new Tool should be created
    

  Scenario: Publish Tool
    Given a new Tool has been created
    When admin clicks on the private Tool
    And clicks on "State"
    And clicks on "Publish"
    Then the Tool should be publicly visible
    
  
  Scenario: Create Method
    Given admin is logged in 
    When admin clicks "Add new"
    And clicks on Method
    And fills the Method form
    And clicks on "Save" button
    Then new Method should be created
    
    
  Scenario: Publish Method
    Given a new Method has been created
    When admin clicks on the private Method
    And clicks on "State"
    And clicks on "Publish"
    Then the Method should be publicly visible

  
  Scenario: Create Test Case
    Given admin is logged in 
    When admin clicks "Add new"
    And clicks on Test Case
    And fills the Test Case form
    And clicks on "Save" button
    Then new Test Case should be created
    
    
  Scenario: Publish Test Case
    Given a new Test Case has been created
    When admin clicks on the private Test Case
    And clicks on "State"
    And clicks on "Publish"
    Then the Test Case should be publicly visible
   
  
  Scenario: Create Requirement
    Given admin is logged in 
    When admin clicks "Add new"
    And clicks on Requirement
    And fills the Requirement form
    And clicks on "Save" button
    Then new Requirement should be created
  
  
  Scenario: Publish Requirement
    Given a new Requirement has been created
    When admin clicks on the private Requirement
    And clicks on "State"
    And clicks on "Publish"
    Then the Requirement should be publicly visible
    
  
  Scenario: Create Evaluation Scenario
    Given admin is logged in 
    When admin clicks "Add new"
    And clicks on Evaluation Scenario
    And fills the Evaluation Scenario form
    And clicks on "Save" button
    Then new Evaluation Scenario should be created
    
    
  Scenario: Publish Evaluation Scenario
    Given a new Evaluation Scenario has been created
    When admin clicks on the private Evaluation Scenario
    And clicks on "State"
    And clicks on "Publish"
    Then the Evaluation Scenario should be publicly visible
     
     
  Scenario: Create relation in Method
    Given the admin is in the form for creating a Method
    When he clicks "Relations"
    And adds the path to Methods
    And clicks on "Safe" button
    Then a relation in Method should be created


  Scenario: Create relation in Tool
    Given the admin is in the form for creating a Tool
    When he clicks "Relations"
    And adds the path to Tests
    And clicks on "Safe" button
    Then a relation in Tool should be created
 
 
  Scenario: Create relation in Use Case
    Given the admin is in the form for creating a Use Case
    When he clicks "Use Case Evaluation Scenarios"
    And adds the path to Evaluation Scenario
    And clicks on "Safe" button
    Then a relation in Use Case should be created
    

  Scenario: Create relation in Requirements
    Given the admin is in the form for creating a Requirement
    When he clicks "Requirement Test Cases"
    And adds the path to Test Case
    And clicks on "Safe" button
    Then a relation in Requirements should be created
    
    
  Scenario: Create relation in Evaluation Scenarios
    Given the admin is in the form for creating a Evaluation Scenario
    When he clicks "Evaluation Scenario Requirements"
    And adds the path to Requirement
    And clicks on "Safe" button
    Then a relation in Evaluation Scenarios should be created
    
  
  
  Scenario: Admin Log Out
    Given admin wants to log out
    When admin clicks on "admin"
    And clicks on "Logout"
    Then he should be logged out
