import pytest
from registration import Registration
from crew import Crew
from inventory import Inventory
from race import Race
from results import Results
from mission import Mission


def test_register_and_race():
    reg = Registration()
    race = Race()

    member = reg.register("A", "driver")
    car = {"name": "Car1", "damaged": False}

    assert race.create_race(member, car) == True


def test_invalid_driver():
    reg = Registration()
    race = Race()

    member = reg.register("A", "mechanic")
    car = {"name": "Car1", "damaged": False}

    with pytest.raises(ValueError):
        race.create_race(member, car)


def test_race_updates_inventory():
    inv = Inventory()
    results = Results()

    inv.cash = 100
    results.record_result(inv, 50)

    assert inv.cash == 150


def test_mission_role_validation():
    mission = Mission()
    crew = [{"role": "driver"}]

    with pytest.raises(ValueError):
        mission.assign_mission(crew, ["mechanic"])


def test_mission_success():
    mission = Mission()
    crew = [{"role": "driver"}, {"role": "mechanic"}]

    assert mission.assign_mission(crew, ["driver", "mechanic"]) == True