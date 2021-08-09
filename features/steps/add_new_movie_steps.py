from behave import *
from behave.step_registry import setup_step_decorators
from selenium import webdriver

@given(u'I am logged in and on the add new movie page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am logged in and on the add new movie page')

@when(u'I enter a valid title')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter a valid title')


@when(u'I enter a valid rating')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter a valid rating')


@when(u'I enter a valid release date')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter a valid release date')


@when(u'I click on submit')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on submit')


@then(u'I will see an upload success message')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I will see an upload success message')


@when(u'I enter a blank title')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter a blank title')


@when(u'I enter a blank rating')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter a blank rating')


@when(u'I enter a blank release date')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter a blank release date')


@then(u'I will see an upload failure message')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I will see an upload failure message')


@when(u'I enter a title with over 200 chars')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter a title with over 200 chars')


@then(u'I will see an error for title with over 200 chars')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I will see an error for title with over 200 chars')


@when(u'I enter a release date greater than 1/10/2015')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter a release date greater than 1/10/2015')

@then(u'I will see an error for release date under than 1/10/2015')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I will see an error for release date under than 1/10/2015')