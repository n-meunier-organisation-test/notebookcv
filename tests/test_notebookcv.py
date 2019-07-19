"""Tests for `notebookc` package."""
import pytest
from notebookcv.notebookcv import notebookcv


def test_convert(capsys):
    """Correct my_name argument prints"""
    notebookcv.convert("Jill")
    captured = capsys.readouterr()
    assert "Jill" in captured.out


def test_convert_int(capsys):
    """Verify if input an integer"""
    notebookcv.convert(3)
    captured = capsys.readouterr()
    assert "3" in captured.out


def test_convert_list(capsys):
    """Verify if input a list"""
    notebookcv.convert(['a', 'b'])
    captured = capsys.readouterr()
    assert "a" in captured.out


def test_convert_dict(capsys):
    """Verify if input a dict"""
    notebookcv.convert({'name': 'test'})
    captured = capsys.readouterr()
    assert "test" in captured.out
