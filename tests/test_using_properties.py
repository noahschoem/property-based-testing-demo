import hypothesis
import pytest

# this example uses expected properties of the algorithm to test the algorithm's behavior
# in this example, we are testing various implementations of the Levenshtein distance between two strings
# see https://en.wikipedia.org/wiki/Levenshtein_distance
# here, we can even write the tests before implementing the actual function

import src.using_properties

# we can use parametrization to avoid having to write the same test code
# for each different implementation of the levenshtein distance function.
# Only the real Levenshtein function will pass all tests; the others will have different test case failures
@pytest.mark.parametrize(
    "levenshtein_function",
    [
        src.using_properties.levenshtein_stub,
        src.using_properties.levenshtein_off_by_one,
        src.using_properties.levenshtein
     ]
)
class TestLevenshteinFunctions():
    
    @hypothesis.given(hypothesis.strategies.text(max_size=0), hypothesis.strategies.text())
    def test_base_case_a_empty(self, levenshtein_function, a, b):
        assert levenshtein_function(a, b) == len(b)
    
    @hypothesis.given(hypothesis.strategies.text(), hypothesis.strategies.text(max_size=0))
    def test_base_case_b_empty(self, levenshtein_function, a, b):
        assert levenshtein_function(a, b) == len(a)
    
    # the first inductive case tests what happens if two strings start with the same character
    @hypothesis.given(hypothesis.strategies.characters(), hypothesis.strategies.text(), hypothesis.strategies.text())
    def test_inductive_step_same_starting_character(self, levenshtein_function, c, x, y):
        a = f"{c}{x}"
        b = f"{c}{y}"
        assert levenshtein_function(a, b) == levenshtein_function(x, y)
    
    # the second inductive case tests what happens if two strings start with different characters
    # one option would be to simply ignore/pass the test if you generate the same character twice
    # but this approach demonstrates an example of composite strategies
    @hypothesis.strategies.composite
    def two_different_characters(draw):
        char_generator_one = hypothesis.strategies.characters()
        char_one = draw(char_generator_one)
        char_generator_two = hypothesis.strategies.characters(exclude_characters=[char_one])
        char_two = draw(char_generator_two)
        return char_one, char_two
    
    @hypothesis.given(two_different_characters(), hypothesis.strategies.text(), hypothesis.strategies.text())
    def test_inductive_step_different_starting_character(self, levenshtein_function, start_chars, x, y):
        c, d = start_chars
        a = f"{c}{x}"
        b = f"{d}{y}"
        assert levenshtein_function(a, b) == 1 + min(
            levenshtein_function(x, b),
            levenshtein_function(a, y),
            levenshtein_function(x, y)
        )

