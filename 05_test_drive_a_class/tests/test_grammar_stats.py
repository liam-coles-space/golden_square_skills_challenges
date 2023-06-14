from lib.grammar_stats import *

def test_check_returns_false_when_lowercase_and_no_end_punctuation():
    grammar_stats = GrammarStats()
    assert grammar_stats.check('no capital and no punctuation at the end') == False

def test_check_returns_false_when_uppercase_and_no_end_punctuation():
    grammar_stats = GrammarStats()
    assert grammar_stats.check('Capital and no punctuation at the end') == False

def test_check_returns_false_when_lowercase_and_has_end_punctuation():
    grammar_stats = GrammarStats()
    assert grammar_stats.check('no capital and has full stop at the end.') == False
    assert grammar_stats.check('no capital and has question mark at the end?') == False
    assert grammar_stats.check('no capital and has exclamation point at the end!') == False

def test_check_returns_True_when_uppercase_and_has_end_punctuation():
    grammar_stats = GrammarStats()
    assert grammar_stats.check('Capital and has full stop at the end.') == True
    assert grammar_stats.check('Capital and has question mark at the end?') == True
    assert grammar_stats.check('Capital and has exclamation point at the end!') == True

def test_check_returns_False_when_string_is_blank():
    grammar_stats = GrammarStats()
    assert grammar_stats.check('') == False

def test_percentage_good_returns_zero_when_no_texts_checked():
    grammar_stats = GrammarStats()
    assert grammar_stats.percentage_good() == 0

def test_percentage_good_returns_correct_when_0_failures_1_success():
    grammar_stats = GrammarStats()
    grammar_stats.check('Capital and has full stop at the end.')
    assert grammar_stats.percentage_good() == 100

def test_percentage_good_returns_correct_when_1_failures_1_success():
    grammar_stats = GrammarStats()
    grammar_stats.check('Capital and has full stop at the end.')
    grammar_stats.check('no capital and has full stop at the end.')
    assert grammar_stats.percentage_good() == 50

def test_percentage_good_returns_correct_when_3_failures_2_success():
    grammar_stats = GrammarStats()
    grammar_stats.check('Capital and has full stop at the end.')
    grammar_stats.check('no capital and has full stop at the end.')
    grammar_stats.check('no capital and has full stop at the end.')
    grammar_stats.check('no capital and has full stop at the end.')
    grammar_stats.check('Capital and has full stop at the end.')
    assert grammar_stats.percentage_good() == 40

