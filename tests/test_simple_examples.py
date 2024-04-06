import hypothesis
import pytest

import src.simple_examples


# even with pytest.mark.parametrize, these tests are limited in what they can do
def test_a_non_property_based_test():
    assert src.simple_examples.is_ascii('a')

def test_another_non_property_based_test():
    assert not src.simple_examples.is_ascii('π')

# here's where property based testing can come in
@hypothesis.given(hypothesis.strategies.characters(min_codepoint=0, max_codepoint=127))
def test_is_ascii_is_true_for_ascii(ascii_char):
    assert src.simple_examples.is_ascii(ascii_char)

# here's where property based testing can come in
@hypothesis.given(hypothesis.strategies.characters(min_codepoint=128))
def test_is_ascii_is_false_for_non_ascii(ascii_char):
    assert not src.simple_examples.is_ascii(ascii_char)

# while hypothesis doesn't assist in writing edge case tests,
# spending time thinking about properties instead of specific test examples
# frees up time to think about edge case tests like this one
# perhaps after writing a test like this and having it fail,
# a developer will refactor the original code to make error handling more explicit
# additionally, for failing tests hypothesis will search for minimal failing examples
# to better aid with debugging
@hypothesis.given(hypothesis.strategies.text())
def test_is_ascii_doesnt_crash(s):
    _ = src.simple_examples.is_ascii(s)