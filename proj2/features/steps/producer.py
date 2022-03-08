from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


SLEEP_TIME = 2
ErrList = []

@given(u'admin wants to log in')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S")
    context.driver.set_window_size(1848, 1016)
    context.driver.find_element(By.ID, "personaltools-login").click()


@when(u'admin fills name and password and enters')
def step_impl(context):
    context.driver.find_element(By.ID, "__ac_name").click()
    context.driver.find_element(By.ID, "__ac_name").send_keys("admin")
    context.driver.find_element(By.ID, "__ac_password").send_keys("admin")
    context.driver.find_element(By.CSS_SELECTOR, ".pattern-modal-buttons > #buttons-login").click()


@then(u'he should be logged in')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/front-page")
    context.driver.find_element(By.CSS_SELECTOR, "#portal-logo > img").click()

@given(u'admin is logged in')
def step_impl(context):
    pass

@when(u'admin clicks "Add new"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#portal-logo > img").click()
    time.sleep(SLEEP_TIME)
    context.driver.find_element(By.CSS_SELECTOR, "#plone-contentmenu-factories .plone-toolbar-title").click()


@when(u'clicks on Use Case')
def step_impl(context):
    context.driver.find_element(By.ID, "use_case").click()


@when(u'fills the Use Case form')
def step_impl(context):
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys("Case")
    context.driver.switch_to.frame(0)
    context.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script(
        "if(arguments[0].contentEditable === 'true') {arguments[0].innerText = 'Description'}", element)
    context.driver.switch_to.default_content()


@when(u'clicks on "Save" button')
def step_impl(context):
    context.driver.find_element(By.ID, "form-buttons-save").click()
    time.sleep(SLEEP_TIME)


@then(u'new Use Case should be created')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/case/view")


@given(u'a new Use Case has been created')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/case/view")


@when(u'admin clicks on the private Use Case')
def step_impl(context):
    pass


@when(u'clicks on "State"')
def step_impl(context):
    time.sleep(SLEEP_TIME)
    context.driver.find_element(By.CSS_SELECTOR, ".plone-toolbar-state-title").click()


@when(u'clicks on "Publish"')
def step_impl(context):
    context.driver.find_element(By.ID, "workflow-transition-publish").click()
    time.sleep(SLEEP_TIME)


@then(u'the Use Case should be publicly visible')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/case")


@given(u'admin is logged in ')
def step_impl(context):
    pass


@when(u'clicks on Tool')
def step_impl(context):
    context.driver.find_element(By.ID, "tool").click()


@when(u'fills the Tool form')
def step_impl(context):
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").click()
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").send_keys("Tool")
    context.driver.find_element(By.ID, "form-widgets-tool_purpose").click()
    context.driver.execute_script("window.scrollTo(0,404)")
    context.driver.find_element(By.ID, "form-widgets-tool_purpose").send_keys("Tool Purpose")
    context.driver.switch_to.frame(3)
    context.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script(
        "if(arguments[0].contentEditable === 'true') {arguments[0].innerText = 'Tool Description'}", element)
    context.driver.switch_to.default_content()
    context.driver.switch_to.frame(2)
    context.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script(
        "if(arguments[0].contentEditable === 'true') {arguments[0].innerText = 'Tool Strengths'}", element)
    context.driver.switch_to.default_content()
    context.driver.switch_to.frame(1)
    context.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script(
        "if(arguments[0].contentEditable === 'true') {arguments[0].innerText = 'Tool Limitations'}", element)
    context.driver.switch_to.default_content()


@then(u'new Tool should be created')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/tool/view")


@given(u'a new Tool has been created')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/tool/view")


@when(u'admin clicks on the private Tool')
def step_impl(context):
    pass


@then(u'the Tool should be publicly visible')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/tool")


@when(u'clicks on Method')
def step_impl(context):
    context.driver.find_element(By.ID, "method").click()


@when(u'fills the Method form')
def step_impl(context):
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys("method")
    context.driver.find_element(By.ID, "form-widgets-method_purpose").click()
    context.driver.find_element(By.ID, "form-widgets-method_purpose").send_keys("method")
    context.driver.switch_to.frame(3)
    context.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = 'method'}",
                               element)
    context.driver.switch_to.default_content()
    context.driver.switch_to.frame(2)
    context.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = 'method'}",
                               element)
    context.driver.switch_to.default_content()
    context.driver.switch_to.frame(1)
    context.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = context.driver.find_element(By.ID, "tinymce")
    context.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = 'method'}",
                               element)
    context.driver.switch_to.default_content()


@then(u'new Method should be created')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/method/view")


@given(u'a new Method has been created')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/method/view")


@when(u'admin clicks on the private Method')
def step_impl(context):
    pass



@then(u'the Method should be publicly visible')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/method")


@when(u'clicks on Test Case')
def step_impl(context):
    context.driver.find_element(By.ID, "test_case").click()


@when(u'fills the Test Case form')
def step_impl(context):
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys("Test")
    context.driver.find_element(By.ID, "form-widgets-test_case_id").click()
    context.driver.find_element(By.ID, "form-widgets-test_case_id").send_keys("1")



@then(u'new Test Case should be created')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/test/view")


@given(u'a new Test Case has been created')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/test/view")


@when(u'admin clicks on the private Test Case')
def step_impl(context):
    pass


@then(u'the Test Case should be publicly visible')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/test")


@when(u'clicks on Requirement')
def step_impl(context):
    context.driver.find_element(By.ID, "requirement").click()


@when(u'fills the Requirement form')
def step_impl(context):
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").click()
    context.driver.find_element(By.ID, "form-widgets-IDublinCore-title").send_keys("Requirement")



@then(u'new Requirement should be created')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/requirement/view")


@given(u'a new Requirement has been created')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/requirement/view")


@when(u'admin clicks on the private Requirement')
def step_impl(context):
    pass


@then(u'the Requirement should be publicly visible')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/requirement")


@when(u'clicks on Evaluation Scenario')
def step_impl(context):
    context.driver.find_element(By.ID, "evaluation_scenario").click()


@when(u'fills the Evaluation Scenario form')
def step_impl(context):
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").click()
    context.driver.find_element(By.ID, "form-widgets-IBasic-title").send_keys("Scenario")
    context.driver.find_element(By.ID, "form-widgets-evaluation_secnario_id").click()
    context.driver.find_element(By.ID, "form-widgets-evaluation_secnario_id").send_keys("33")
    context.driver.find_element(By.ID, "form-widgets-evaluation_scenario_textual_description").click()
    context.driver.find_element(By.ID, "form-widgets-evaluation_scenario_textual_description").send_keys("Description")


@then(u'new Evaluation Scenario should be created')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/scenario/view")


@given(u'a new Evaluation Scenario has been created')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/scenario/view")


@when(u'admin clicks on the private Evaluation Scenario')
def step_impl(context):
    pass


@then(u'the Evaluation Scenario should be publicly visible')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/scenario")









@given(u'the admin is in the form for creating a Method')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#portal-logo > img").click()
    time.sleep(SLEEP_TIME)
    context.driver.get("http://localhost:8080/VALU3S/method/edit")


@when(u'he clicks "Relations"')
def step_impl(context):
    context.driver.find_element(By.ID, "autotoc-item-autotoc-2").click()


@when(u'adds the path to Methods')
def step_impl(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, "#formfield-form-widgets-tools .path-wrapper .glyphicon").click()
        time.sleep(SLEEP_TIME)
        context.driver.find_element(By.CSS_SELECTOR, ".pattern-relateditems-result-title").click()
        time.sleep(SLEEP_TIME)
        context.driver.find_element(By.CSS_SELECTOR,
                             "#formfield-form-widgets-test_case_or_verification_and_validation_activity .path-wrapper .glyphicon").click()
        time.sleep(SLEEP_TIME)
        context.driver.find_element(By.CSS_SELECTOR, ".pattern-relateditems-result-title").click()
    except:
        context.driver.get("http://localhost:8080/VALU3S/method/edit")
        ErrList.append("adds the path to Methods")


@when(u'clicks on "Safe" button')
def step_impl(context):
    context.driver.find_element(By.ID, "form-buttons-save").click()
    time.sleep(SLEEP_TIME)


@then(u'a relation in Method should be created')
def step_impl(context):
    pass


@given(u'the admin is in the form for creating a Tool')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#portal-logo > img").click()
    time.sleep(SLEEP_TIME)
    context.driver.get("http://localhost:8080/VALU3S/tool/edit")


@when(u'adds the path to Tests')
def step_impl(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR,
                             "#formfield-form-widgets-test_case_or_verification_and_validation_activity .path-wrapper .glyphicon").click()
        time.sleep(SLEEP_TIME)
        context.driver.find_element(By.CSS_SELECTOR, ".pattern-relateditems-result-title").click()
    except:
        context.driver.get("http://localhost:8080/VALU3S/tool/edit")


@then(u'a relation in Tool should be created')
def step_impl(context):
    pass


@given(u'the admin is in the form for creating a Use Case')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#portal-logo > img").click()
    time.sleep(SLEEP_TIME)
    context.driver.get("http://localhost:8080/VALU3S/case/edit")


@when(u'he clicks "Use Case Evaluation Scenarios"')
def step_impl(context):
    context.driver.find_element(By.ID, "autotoc-item-autotoc-1").click()


@when(u'adds the path to Evaluation Scenario')
def step_impl(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR,
                             "#formfield-form-widgets-evaluation_scenario .path-wrapper .glyphicon").click()
        time.sleep(SLEEP_TIME)
        context.driver.find_element(By.ID, "s2id_autogen2").send_keys("/scenario")
        time.sleep(SLEEP_TIME)
        time.sleep(SLEEP_TIME)
        context.driver.find_element(By.CSS_SELECTOR, "#select2-result-label-95 .pattern-relateditems-result-info").click()
    except:
        context.driver.get("http://localhost:8080/VALU3S/case/edit")
        ErrList.append("adds the path to Evaluation Scenario")


@then(u'a relation in Use Case should be created')
def step_impl(context):
    pass


@given(u'the admin is in the form for creating a Requirement')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#portal-logo > img").click()
    time.sleep(SLEEP_TIME)
    context.driver.get("http://localhost:8080/VALU3S/requirement/edit")


@when(u'he clicks "Requirement Test Cases"')
def step_impl(context):
    context.driver.find_element(By.ID, "autotoc-item-autotoc-1").click()


@when(u'adds the path to Test Case')
def step_impl(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, ".glyphicon-home").click()
        time.sleep(SLEEP_TIME)
        context.driver.find_element(By.CSS_SELECTOR, "#select2-result-label-20 .pattern-relateditems-result-info").click()
    except:
        context.driver.get("http://localhost:8080/VALU3S/requirement/edit")
        ErrList.append("adds the path to Test Case")


@then(u'a relation in Requirements should be created')
def step_impl(context):
    pass


@given(u'the admin is in the form for creating a Evaluation Scenario')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#portal-logo > img").click()
    time.sleep(SLEEP_TIME)
    context.driver.get("http://localhost:8080/VALU3S/scenario/edit")


@when(u'he clicks "Evaluation Scenario Requirements"')
def step_impl(context):
    context.driver.find_element(By.ID, "autotoc-item-autotoc-1").click()


@when(u'adds the path to Requirement')
def step_impl(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR,
                             "#formfield-form-widgets-evaluation_scenario_requirements_list .path-wrapper .glyphicon").click()
        time.sleep(SLEEP_TIME)
        context.driver.find_element(By.CSS_SELECTOR, ".pattern-relateditems-result-info > .contenttype-requirement").click()
    except:
        context.driver.get("http://localhost:8080/VALU3S/scenario/edit")
        ErrList.append("adds the path to Evaluation Scenario")


@then(u'a relation in Evaluation Scenarios should be created')
def step_impl(context):
    pass



@given(u'admin wants to log out')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S/front-page")
    time.sleep(SLEEP_TIME)
    context.driver.find_element(By.CSS_SELECTOR, "#portal-logo > img").click()
    time.sleep(SLEEP_TIME)


@when(u'admin clicks on "admin"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#portal-personaltools span:nth-child(2)").click()
    time.sleep(SLEEP_TIME)



@when(u'clicks on "Logout"')
def step_impl(context):
    context.driver.find_element(By.ID, "personaltools-logout").click()
    time.sleep(SLEEP_TIME)


@then(u'he should be logged out')
def step_impl(context):
    context.driver.get("http://localhost:8080/VALU3S")


