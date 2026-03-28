import pytest
from string_utils import StringUtils

utils = StringUtils()

def test_capitalize_skypro():
    assert utils.capitalize("skypro") == "Skypro"

def test_capitalize_hello():
    assert utils.capitalize("hello world") == "Hello world"

def test_capitalize_numbers():
    assert utils.capitalize("123") == "123"

def test_capitalize_empty():
    assert utils.capitalize("") == ""

def test_capitalize_space():
    assert utils.capitalize(" ") == " "

def test_trim_spaces():
    assert utils.trim("   skypro") == "skypro"

def test_trim_no_spaces():
    assert utils.trim("skypro") == "skypro"

def test_trim_empty():
    assert utils.trim("") == ""

def test_trim_only_spaces():
    assert utils.trim("   ") == ""

def test_trim_mixed():
    assert utils.trim("  hello world  ") == "hello world  "

def test_contains_symbol_true():
    assert utils.contains("SkyPro", "S") == True

def test_contains_symbol_false():
    assert utils.contains("SkyPro", "U") == False

def test_contains_substring():
    assert utils.contains("SkyPro", "Pro") == True

def test_contains_empty_symbol():
    assert utils.contains("SkyPro", "") == True

def test_contains_empty_string():
    assert utils.contains("", "S") == False

def test_delete_single_char():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"

def test_delete_substring():
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"

def test_delete_not_found():
    assert utils.delete_symbol("SkyPro", "z") == "SkyPro"

def test_delete_empty_string():
    assert utils.delete_symbol("", "k") == ""

def test_delete_all():
    assert utils.delete_symbol("aaaa", "a") == ""
