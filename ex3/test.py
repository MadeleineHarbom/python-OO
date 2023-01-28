import pytest

from ex3.model import Person


def test_can_create_person_objects():
    made = Person('Madeleine', 'Harbom')
    assert made.firstname == 'Madeleine' and made.lastname == 'Harbom'


def test_cannot_create_without_lastname():
    with pytest.raises(Exception) as e:
        Person('Madeleine')
    assert e != None


def test_cannot_create_with_invalid_name():
    with pytest.raises(Exception) as e:
        Person(1)
    assert e != None

    with pytest.raises(Exception) as e:
        Person(1, "Harbom")
    assert e != None

    with pytest.raises(Exception) as e:
        Person('Madeleine', 1)
    assert e.type == TypeError

    with pytest.raises(Exception) as e:
        Person(firstname='Madeleine', lastname=1)
    assert e.type == TypeError


def test_equality():
    p1 = Person('Madeleine', 'Harbom')
    p2 = Person('Madeleine', 'Harbom')
    assert p1 == p2

    p3 = Person('Madeleine', 'Harbom', telephone_number='60653173')
    p4 = Person('Madeleine', 'Harbom', telephone_number='60653173')
    assert p3 == p4

    p5 = Person('Madeleine', 'Harbom', email='madeleine.harbom@gmail.com')
    p6 = Person('Madeleine', 'Harbom', email='madeleine.harbom@gmail.com')
    assert p5 == p6

    p7 = Person('Madeleine', 'Harbom', telephone_number='60653173', email='madeleine.harbom@gmail.com')
    p8 = Person('Madeleine', 'Harbom', telephone_number='60653173', email='madeleine.harbom@gmail.com')
    assert p7 == p8


def test_nonequiality():
    p1 = Person('Madeleine', 'Harbom')
    p2 = Person('Madeleine', 'Harbom', telephone_number='60653173')
    p3 = Person('Madeleine', 'Harbom', email='madeleine.harbom@gmail.com')
    p4 = Person('Madeleine', 'Harbom', telephone_number='60653173', email='madeleine.harbom@gmail.com')
    p5 = Person('Madeleine', 'Harbom', telephone_number='60653163', email='madeleine.harbom@gmail.com')
    p6 = Person('Madeleine', 'Harbom', telephone_number='60653173', email='made.harbom@gmail.com')
    p7 = Person('Madeleine', 'Harbom', email='made.harbom@gmail.com')
    p8 = Person('Madeleine', 'Harbom', telephone_number='60653163')
    assert p1 != p2
    assert p1 != p3
    assert p1 != p4
    assert p1 != p5
    assert p1 != p6
    assert p1 != p7
    assert p1 != p8
    assert p2 != p3
    assert p2 != p4
    assert p2 != p5
    assert p2 != p6
    assert p2 != p7
    assert p2 != p8
    assert p3 != p4
    assert p3 != p5
    assert p3 != p6
    assert p3 != p7
    assert p3 != p8
    assert p4 != p5
    assert p4 != p6
    assert p4 != p7
    assert p4 != p8
    assert p5 != p6
    assert p5 != p7
    assert p5 != p8
    assert p6 != p7
    assert p6 != p8
    assert p7 != p8


def test_repr():
    made = Person('Madeleine', 'Harbom', '60653173', 'madeleine.harbom@gmail.com')
    masked_made = Person('Madeleine', 'Harbom', '60653173', 'madeleine.harbom@gmail.com', display_mode='masked')
    repr_full = repr(made)
    repr_masked = repr(masked_made)
    assert repr_full == "Person('Madeleine', 'Harbom', telephone_number='60653173', email='madeleine.harbom@gmail.com')"
    assert repr_masked == "Person('M********', 'H*****')"

    recreated_person =eval(repr(made))
    assert type(recreated_person) is Person


def test_str():
    made = Person('Madeleine', 'Harbom', '60653173', 'madeleine.harbom@gmail.com')
    masked_made = Person('Madeleine', 'Harbom', '60653173', 'madeleine.harbom@gmail.com', display_mode='masked')
    assert str(made) == "MH"
    assert str(masked_made) == "MH"


def test_format():
    masked_made = Person('Madeleine', 'Harbom', '60653173', 'madeleine.harbom@gmail.com', display_mode='masked')
    unmasked_format = format(masked_made, "unmasked")
    masked_format = format(masked_made)
    assert unmasked_format == "Person(firstname=Madeleine, lastname=Harbom, telephone_number=60653173, email=madeleine.harbom@gmail.com)"
    assert masked_format == "Person(firstname=M********, lastname=H*****)"

