from project import (
    caesar_encrypt,
    shift_upper,
    shift_lower,
    caesar_decrypt,
    brute_force_caesar,
)


def test_caesar_encrypt():
    assert caesar_encrypt("abc", 3) == "def"
    assert caesar_encrypt("xyz", 3) == "abc"
    assert caesar_encrypt("Hello, World!", 5) == "Mjqqt, Btwqi!"
    assert caesar_encrypt("Python 3.8", 2) == "Ravjqp 3.8"
    assert caesar_encrypt("Caesar Cipher", 4) == "Geiwev Gmtliv"
    assert caesar_encrypt("12345", 3) == "12345"
    assert caesar_encrypt(" ", 3) == " "
    assert caesar_encrypt("!@#$%^&*", 3) == "!@#$%^&*"
    assert caesar_encrypt("abc4ljh", 3) == "def4omk"


def test_shift_upper():
    assert shift_upper("A", 3) == ord("D")
    assert shift_upper("Z", 3) == ord("C")
    assert shift_upper("G", 2) == ord("I")
    assert shift_upper("X", 5) == ord("C")
    assert shift_upper("M", 10) == ord("W")
    assert shift_upper("A", 26) == ord("A")
    assert shift_upper("Z", 26) == ord("Z")
    assert shift_upper("A", 0) == ord("A")


def test_shift_lower():
    assert shift_lower("a", 3) == ord("d")
    assert shift_lower("z", 3) == ord("c")
    assert shift_lower("g", 2) == ord("i")
    assert shift_lower("x", 5) == ord("c")
    assert shift_lower("m", 10) == ord("w")
    assert shift_lower("a", 26) == ord("a")
    assert shift_lower("z", 26) == ord("z")
    assert shift_lower("a", 0) == ord("a")


def test_caesar_decrypt():
    assert caesar_decrypt("def", 3) == "abc"
    assert caesar_decrypt("abc", 3) == "xyz"
    assert caesar_decrypt("Mjqqt, Btwqi!", 5) == "Hello, World!"
    assert caesar_decrypt("Ravjqp 3.8", 2) == "Python 3.8"
    assert caesar_decrypt("Geiwev Gmtliv", 4) == "Caesar Cipher"
    assert caesar_decrypt("12345", 3) == "12345"
    assert caesar_decrypt(" ", 3) == " "
    assert caesar_decrypt("!@#$%^&*", 3) == "!@#$%^&*"
    assert caesar_decrypt("def4omk", 3) == "abc4ljh"


def test_caesar_brute_force():
    # Convert the generator to a list for comparison.
    assert list(brute_force_caesar("def")) == [
        "Shift 1: cde",
        "Shift 2: bcd",
        "Shift 3: abc",
        "Shift 4: zab",
        "Shift 5: yza",
        "Shift 6: xyz",
        "Shift 7: wxy",
        "Shift 8: vwx",
        "Shift 9: uvw",
        "Shift 10: tuv",
        "Shift 11: stu",
        "Shift 12: rst",
        "Shift 13: qrs",
        "Shift 14: pqr",
        "Shift 15: opq",
        "Shift 16: nop",
        "Shift 17: mno",
        "Shift 18: lmn",
        "Shift 19: klm",
        "Shift 20: jkl",
        "Shift 21: ijk",
        "Shift 22: hij",
        "Shift 23: ghi",
        "Shift 24: fgh",
        "Shift 25: efg",
    ]

    assert list(brute_force_caesar("Mjqqt, Btwqi!")) == [
        "Shift 1: Lipps, Asvph!",
        "Shift 2: Khoor, Zruog!",
        "Shift 3: Jgnnq, Yqtnf!",
        "Shift 4: Ifmmp, Xpsme!",
        "Shift 5: Hello, World!",
        "Shift 6: Gdkkn, Vnqkc!",
        "Shift 7: Fcjjm, Umpjb!",
        "Shift 8: Ebiil, Tloia!",
        "Shift 9: Dahhk, Sknhz!",
        "Shift 10: Czggj, Rjmgy!",
        "Shift 11: Byffi, Qilfx!",
        "Shift 12: Axeeh, Phkew!",
        "Shift 13: Zwddg, Ogjdv!",
        "Shift 14: Yvccf, Nficu!",
        "Shift 15: Xubbe, Mehbt!",
        "Shift 16: Wtaad, Ldgas!",
        "Shift 17: Vszzc, Kcfzr!",
        "Shift 18: Uryyb, Jbeyq!",
        "Shift 19: Tqxxa, Iadxp!",
        "Shift 20: Spwwz, Hzcwo!",
        "Shift 21: Rovvy, Gybvn!",
        "Shift 22: Qnuux, Fxaum!",
        "Shift 23: Pmttw, Ewztl!",
        "Shift 24: Olssv, Dvysk!",
        "Shift 25: Nkrru, Cuxrj!",
    ]