import pytest
from morse import decode


@pytest.mark.parametrize(
    "encoded, expected",
    [
        (
                ".... . .-.. .-.. --- --..--  .-- --- .-. .-.. -.. .-.-.-",
                "HELLO, WORLD."
        ),
        (
                "-- .. ... .... .- -- .. ... .... .- -- .. ... .... .-",
                "MISHAMISHAMISHA"
        ),
        (
                "-....- -....- -....-",
                "---"
        ),
        (
                "-.--.- -.--.- -.--.",
                "))("
        ),
        (
                "..--.. ..--.. ..--.. .-.-.-",
                "???."
        ),
        (
                ".--. .-. .. ...- . -",
                "PRIVET"
        ),
        (
            ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. "
            "--.- .-. ... - ..- ...- .-- -..- -.-- --..",
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ),
    ],
)
def test_decoder_correct_cases(encoded, expected):
    assert decode(encoded) == expected


@pytest.mark.parametrize(
    "encoded, expected",
    [
        (
                "-..-. -..-. -..-. --..-- --..-- --..-- --..--",
                "///,,,,"
        ),
        (
                ".-.-.- ..--.. -..-. -....- -.--. -.--.- --..--",
                ".?/-(),"
        ),
    ],
)
def test_decoder_expect_wrong_answers(encoded, expected):
    assert decode(encoded) != expected
