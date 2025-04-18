
import pytest
from television import Television

def test_if_television():
    tv = Television()
    assert tv.__status == False
    assert tv.__muted == False
    assert tv.__volume == Television.MIN_VOLUME
    assert tv.__channel == Television.MIN_CHANNEL