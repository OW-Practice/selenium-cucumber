from behave import *
from pages.add_a_list_card_page import AddAListCardPage
from faker import Faker

fake = Faker()
list_names = []
total_card_names = []


@when(u'Create list title "{input}" and validate list name')
def create_list_title_validate_list_name(context, input):
    context.list_card = AddAListCardPage(context.driver)
    value = int(input)
    for i in range(value):
        name = fake.name()
        list_names.append(name)
        context.list_card.enter_list_title(name)
        context.list_card.click_on_add_a_list_button()
        context.list_card.verify_added_list_name(name)


@when(u'Create card with list size "{list_size}" and card size "{card_size}" and enter card name')
def click_on_add_a_card_button_enter_card_name(context, list_size, card_size):
    context.list_card = AddAListCardPage(context.driver)
    lists_val = int(list_size)
    cards_val = int(card_size)
    for i in range(lists_val):
        name_of_list = list_names[i]
        context.list_card.click_on_add_a_card_button(name_of_list)
        card_names = []
        for j in range(cards_val):
            name_card = fake.name()
            card_names.append(name_card)
            context.list_card.enter_card_name(name_card)
            context.list_card.click_on_add_card_button()
        total_card_names.append(card_names)


@then(u'Validate cards based on list size "{list_size}" and card size "{card_size}"')
def validate_created_cards_under_lists(context,list_size, card_size):
    context.list_card = AddAListCardPage(context.driver)
    lists_val = int(list_size)
    cards_val = int(card_size)
    for i in range(lists_val):
        name_of_list = list_names[i]
        for j in range(cards_val):
            card = total_card_names[i][j]
            context.list_card.verify_card_name(name_of_list, card)