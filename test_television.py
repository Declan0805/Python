

import pytest
from television import Television

def test_if_television():
    tv = Television()
    assert tv.get_status() == False
    assert tv.get_muted() == False
    assert tv.get_volume() == Television.MIN_VOLUME
    assert tv.get_channel() == Television.MIN_CHANNEL

def test_power():
    tv = Television()
    tv.power()
    assert tv.get_status() == True
    tv.power()
    assert tv.get_status() == False
def test_mute():
    tv = Television()
    tv.power()
    tv.mute()
    assert tv.get_muted() == True
    tv.mute()
    assert tv.get_muted() == False
def test_channelup():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert tv.get_channel() == Television.MIN_CHANNEL + 1

    while tv.get_channel() < Television.MAX_CHANNEL:
        tv.channel_up()
    tv.channel_up()
    assert tv.get_channel() == Television.MIN_CHANNEL
def test_channeldown():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert tv.get_channel() == Television.MAX_CHANNEL
    while tv.get_channel() > Television.MIN_CHANNEL:
        tv.channel_down()
    assert tv.get_channel() == Television.MIN_CHANNEL
    tv.channel_down()
    assert tv.get_channel() == Television.MAX_CHANNEL
def test_volumeup():
    tv = Television()
    tv.power()
    assert tv.get_muted() == False
    tv.volume_up()
    assert tv.get_volume() == Television.MIN_VOLUME + 1
    while tv.get_volume() < Television.MAX_VOLUME:
        tv.volume_up()
    assert tv.get_volume() == Television.MAX_VOLUME
    tv.volume_up()
    assert tv.get_volume() == Television.MAX_VOLUME
def test_volumedown():
    tv = Television()
    tv.power()
    assert tv.get_muted() == False
    tv.volume_down()
    assert tv.get_volume() == Television.MIN_VOLUME
    while tv.get_volume() < Television.MAX_VOLUME:
        tv.volume_up()
    assert tv.get_volume() == Television.MAX_VOLUME
    while tv.get_volume() > Television.MIN_VOLUME:
        tv.volume_down()
    assert tv.get_volume() == Television.MIN_VOLUME