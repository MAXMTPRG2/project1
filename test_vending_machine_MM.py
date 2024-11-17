# Max Molnar S/N 100746162
# TPRG 2131 CRN 02 -Project 1
# Nov 10, 2024

# test_vending_machine_MM.py

# This program is strictly my own work. Any material
# beyond course learning materials that is taken from
# the Web or other sources is properly cited, giving
# credit to the original author(s).

# Adapted from code provided by
# Professor Phil Jarvis

# This is a pytest file to test the vending_machine.py state machine file.

# This file tests the event of adding a coin, ensuring it is the corresct amount in pennies,
# and that the return event is in the CountChangeState and returns the correct amount for
# each coin.
from vending_machine_MM import VendingMachine, WaitingState, AddCoinsState, DeliverProductState, CountChangeState

def test_VendingMachine():
    # new machine object
    vending = VendingMachine()

    # Add the states - ORG
    # vending.add_state(WaitingState())
    # vending.add_state(CoinsState())
    # vending.add_state(DispenseState())
    # vending.add_state(ChangeState())

    # My revisions
    vending.add_state(WaitingState())
    vending.add_state(AddCoinsState())
    vending.add_state(DeliverProductState())
    vending.add_state(CountChangeState())


    # Reset state is "waiting for first coin"
    vending.go_to_state('waiting')
    assert vending.state.name == 'waiting'

    # test that the first coin causes a transition to 'coins'
    vending.event = '200' # a twonie
    vending.update()
    assert vending.state.name == 'add_coins'
    assert vending.amount == 200 # pennies, was .total
    
    # test the return value of the first coin
    vending.event = "RETURN"
    vending.update()
    assert vending.change_due == 200
    assert vending.state.name == 'count_change'
   
    # Reset state is "waiting for first coin"
    vending.go_to_state('waiting')
    assert vending.state.name == 'waiting'
    
    vending.event = '100' # a loonie
    vending.update()
    assert vending.state.name == 'add_coins'
    assert vending.amount == 100 # pennies, was .total
    
    # test return value for second coin
    vending.event = "RETURN"
    vending.update()
    assert vending.change_due == 100
    assert vending.state.name == 'count_change'
    
    # Reset state is "waiting for first coin"
    vending.go_to_state('waiting')
    assert vending.state.name == 'waiting'
    
    vending.event = '25' # a quarter
    vending.update()
    assert vending.state.name == 'add_coins'
    assert vending.amount == 25 # pennies, was .total
    
    # test return value for thrid coin
    vending.event = "RETURN"
    vending.update()
    assert vending.change_due == 25
    assert vending.state.name == 'count_change'
    
    # Reset state is "waiting for first coin"
    vending.go_to_state('waiting')
    assert vending.state.name == 'waiting'
    
    vending.event = '10' # a dime
    vending.update()
    assert vending.state.name == 'add_coins'
    assert vending.amount == 10 # pennies, was .total
    
    # test return value for fourth coin
    vending.event = "RETURN"
    vending.update()
    assert vending.change_due == 10
    assert vending.state.name == 'count_change'
    
    # Reset state is "waiting for first coin"
    vending.go_to_state('waiting')
    assert vending.state.name == 'waiting'
    
    vending.event = '5' # a nickel
    vending.update()
    assert vending.state.name == 'add_coins'
    assert vending.amount == 5 # pennies, was .total
    
    # test return value for a nickel
    vending.event = "RETURN"
    vending.update()
    assert vending.change_due == 5
    assert vending.state.name == 'count_change'