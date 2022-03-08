Feature: Producers functions

  #1
  Scenario: Create <category>
    When admin clicks "Add new"
    And clicks on <category>
    And fills the form
    And clicks on "Save" button
    Then new <category> should be created
    Example:
      | category            |
      | Use Case            |
      | Tool                |
      | Method              |
      | Test Case           |
      | Requirement         |
      | Evaluation Scenario |

 #2
  Scenario: Publish <category>
    Given a new <category> has been created
    When admin clicks on the private <category>
    And clicks on "State"
    And clicks on "Publish"
    Then the <category> should be publicly visible
    Example:
      | category            |
      | Use Case            |
      | Tool                |
      | Method              |
      | Test Case           |
      | Requirement         |
      | Evaluation Scenario |

  #3
  Scenario: Send Back <category>
    Given a <category> has been published
    When admin clicks on the <category>
    And clicks on "State"
    And clicks on "Send Back"
    Then the <category> should be private
    Example:
      | category            |
      | Use Case            |
      | Tool                |
      | Method              |
      | Test Case           |
      | Requirement         |
      | Evaluation Scenario |

  #4
  Scenario: Retract <category>
    Given a <category> has been published
    When admin clicks on the <category>
    And clicks on "State"
    And clicks on "Retract"
    Then the <category> should be private
    Example:
      | category            |
      | Use Case            |
      | Tool                |
      | Method              |
      | Test Case           |
      | Requirement         |
      | Evaluation Scenario |

  #5
  Scenario: Submit for publication <category>
    Given a <category> is private
    When admin clicks on the <category>
    And clicks on "State"
    And clicks on "Submit for publication"
    Then the <category> should be in pending for review
    Example:
      | category            |
      | Use Case            |
      | Tool                |
      | Method              |
      | Test Case           |
      | Requirement         |
      | Evaluation Scenario |

  #6
  Scenario: Edit <category>
    Given the admin had clicked on a <category>
    When he clicks on "Edit"
    And edits the form
    And clicks on "Save" button
    Then the <category> should be edited
    Example:
      | category            |
      | Use Case            |
      | Tool                |
      | Method              |
      | Test Case           |
      | Requirement         |
      | Evaluation Scenario |

  #7
  Scenario: Delete <category>
    Given the admin had clicked on a <category>
    When he clicks on "Actions"
    And clicks on "Delete"
    And clicks on "Delete" button
    Then the <category> should be removed
    Example:
      | category            |
      | Use Case            |
      | Tool                |
      | Method              |
      | Test Case           |
      | Requirement         |
      | Evaluation Scenario |

  #8
  Scenario: Create relation in Method
    Given the admin is in the form for creating a Method
    When he clicks "Relations"
    And adds the path to <relation>
    And clicks on "Safe" button
    Then a relation in Method should be created
    Example:
      | relation                                          |
      | Methods                                           |
      | Tools                                             |
      | Part Method                                       |
      | Test Case or Verification and Validation activity |

  #9
  Scenario: Edit relation in Method
    Given the admin is in the form for Editing a Method
    When he clicks "Relations"
    And edits the path to <relation>
    And clicks on "Safe" button
    Then a relation in Method should be edited
    Example:
      | relation                                          |
      | Methods                                           |
      | Tools                                             |
      | Part Method                                       |
      | Test Case or Verification and Validation activity |

  #10
  Scenario: Delete relation in Method
    Given the admin is in the form for Editing a Method
    When he clicks "Relations"
    And removes the path to <relation>
    And clicks on "Safe" button
    Then a relation in Method should be removed
    Example:
      | relation                                          |
      | Methods                                           |
      | Tools                                             |
      | Part Method                                       |
      | Test Case or Verification and Validation activity |

  #11
  Scenario: Create relation in Tool
    Given the admin is in the form for creating a Tool
    When he clicks "Relations"
    And adds the path to <relation>
    And clicks on "Safe" button
    Then a relation in Tool should be created
    Example:
      | relation                                          |
      | Methods                                           |
      | Test Case or Verification and Validation activity |

  #12
  Scenario: Edit relation in Tool
    Given the admin is in the form for Editing a Tool
    When he clicks "Relations"
    And edits the path to <relation>
    And clicks on "Safe" button
    Then a relation in Tool should be edited
    Example:
      | relation                                          |
      | Methods                                           |
      | Test Case or Verification and Validation activity |

  #13
  Scenario: Delete relation in Tool
    Given the admin is in the form for Editing a Tool
    When he clicks "Relations"
    And removes the path to <relation>
    And clicks on "Safe" button
    Then a relation in Tool should be removed
    Example:
      | relation                                          |
      | Methods                                           |
      | Test Case or Verification and Validation activity |


  #14
  Scenario: Create relation in Use Case
    Given the admin is in the form for creating a Use Case
    When he clicks "Use Case Evaluation Scenarios"
    And adds the path to <relation>
    And clicks on "Safe" button
    Then a relation in Use Case should be created
    Example:
      | relation            |
      | Evaluation Scenario |

  #15
  Scenario: Edit relation in Use Case
    Given the admin is in the form for Editing a Use Case
    When he clicks "Use Case Evaluation Scenarios"
    And edits the path to <relation>
    And clicks on "Safe" button
    Then a relation in Use Case should be edited
    Example:
      | relation            |
      | Evaluation Scenario |

  #16
  Scenario: Delete relation in Use Case
    Given the admin is in the form for Editing a Use Case
    When he clicks "Use Case Evaluation Scenarios"
    And removes the path to <relation>
    And clicks on "Safe" button
    Then a relation in Use Case should be removed
    Example:
      | relation            |
      | Evaluation Scenario |

  #17
  Scenario: Create relation in Requirements
    Given the admin is in the form for creating a Requirement
    When he clicks "Requirement Test Cases"
    And adds the path to <relation>
    And clicks on "Safe" button
    Then a relation in Requirements should be created
    Example:
      | relation  |
      | Test Case |

  #18
  Scenario: Edit relation in Requirements
    Given the admin is in the form for Editing a Requirements
    When he clicks "Requirement Test Cases"
    And edits the path to <relation>
    And clicks on "Safe" button
    Then a relation in Requirements should be edited
    Example:
      | relation  |
      | Test Case |

  #19
  Scenario: Delete relation in Requirements
    Given the admin is in the form for Editing a Requirements
    When he clicks "Requirement Test Cases"
    And removes the path to <relation>
    And clicks on "Safe" button
    Then a relation in Requirements should be removed
    Example:
      | relation  |
      | Test Case |

  #20
  Scenario: Create relation in Evaluation Scenarios
    Given the admin is in the form for creating a Evaluation Scenario
    When he clicks "Evaluation Scenario Requirements"
    And adds the path to <relation>
    And clicks on "Safe" button
    Then a relation in Evaluation Scenarios should be created
    Example:
      | relation    |
      | Requirement |

  #21
  Scenario: Edit relation in Evaluation Scenarios
    Given the admin is in the form for Editing a Evaluation Scenarios
    When he clicks "Evaluation Scenario Requirements"
    And edits the path to <relation>
    And clicks on "Safe" button
    Then a relation in Evaluation Scenarios should be edited
    Example:
    | relation    |
    | Requirement |

  #22
  Scenario: Delete relation in Evaluation Scenarios
    Given the admin is in the form for Editing a Evaluation Scenarios
    When he clicks "Evaluation Scenario Requirements"
    And removes the path to <relation>
    And clicks on "Safe" button
    Then a relation in Evaluation Scenarios should be removed
    Example:
    | relation    |
    | Requirement |
