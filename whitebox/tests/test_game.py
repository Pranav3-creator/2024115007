import pytest
from game import Game
from player import Player
from bank import Bank
from dice import Dice


# ----------------------------
# BASIC VALIDATION TESTS
# ----------------------------

def test_minimum_players():
    with pytest.raises(ValueError):
        Game(["A"])  # less than 2 players


def test_player_initial_balance():
    p = Player("A")
    assert p.balance == 1500


# ----------------------------
# BANK TESTS
# ----------------------------

def test_bank_negative_collect():
    b = Bank()
    with pytest.raises(ValueError):
        b.collect(-100)


def test_bank_overpay():
    b = Bank()
    with pytest.raises(ValueError):
        b.pay_out(999999)


# ----------------------------
# PLAYER TESTS
# ----------------------------

def test_player_negative_deduct():
    p = Player("A")
    with pytest.raises(ValueError):
        p.deduct_money(2000)


# ----------------------------
# DICE TESTS
# ----------------------------

def test_dice_range():
    d = Dice()
    for _ in range(100):
        val = d.roll()
        assert 2 <= val <= 12


# ----------------------------
# GAME LOGIC TESTS
# ----------------------------

def test_turn_rotation():
    g = Game(["A", "B"])
    first = g.current_player()
    g.advance_turn()
    second = g.current_player()
    assert first != second


def test_winner_logic():
    g = Game(["A", "B"])
    g.players[0].balance = 1000
    g.players[1].balance = 2000

    winner = g.find_winner()
    assert winner == g.players[1]


# ----------------------------
# PROPERTY GROUP TEST
# ----------------------------

from property import PropertyGroup, Property

def test_property_group_all_owned():
    group = PropertyGroup("Test", "red")
    p1 = Player("A")

    prop1 = Property("P1", 1, 100, 10, group)
    prop2 = Property("P2", 2, 100, 10, group)

    prop1.owner = p1
    prop2.owner = p1

    assert group.all_owned_by(p1) == True