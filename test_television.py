import pytest
from television import *

class Test:

    def setup_method(self):
        self.tv_1 = Television()

    def teardown_method(self):
        del self.tv_1

    def test__init__(self):
        assert str(self.tv_1) == 'Power = False, Channel = 0, Volume = 0'

    def test_power(self):
        #tv on
        self.tv_1.power()
        assert str(self.tv_1) == 'Power = True, Channel = 0, Volume = 0'

        #tv off
        self.tv_1.power()
        assert str(self.tv_1) == 'Power = False, Channel = 0, Volume = 0'

    def test_mute(self):
        #tv on, volume increased 1, muted
        self.tv_1.power()
        self.tv_1.volume_up()
        self.tv_1.mute()
        assert str(self.tv_1) == 'Power = True, Channel = 0, Volume = 0'

        #tv on, unmuted
        self.tv_1.mute()
        assert str(self.tv_1) == 'Power = True, Channel = 0, Volume = 1'

        #tv off, muted
        self.tv_1.power()
        self.tv_1.mute()
        assert str(self.tv_1) == 'Power = False, Channel = 0, Volume = 1'

        #tv off, unmuted
        self.tv_1.mute()
        assert str(self.tv_1) == 'Power = False, Channel = 0, Volume = 1'

    def test_channel_up(self):
        #tv off, channel increased
        self.tv_1.channel_up()
        assert str(self.tv_1) == 'Power = False, Channel = 0, Volume = 0'

        #tv on, channel increased
        self.tv_1.power()
        self.tv_1.channel_up()
        assert str(self.tv_1) == 'Power = True, Channel = 1, Volume = 0'

        #tv on, channel increased past max
        self.tv_1.channel_up()
        self.tv_1.channel_up()
        self.tv_1.channel_up()
        assert str(self.tv_1) == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        #tv off, channel decreased
        self.tv_1.channel_down()
        assert str(self.tv_1) == 'Power = False, Channel = 0, Volume = 0'

        #tv on, channel decreased past min
        self.tv_1.power()
        self.tv_1.channel_down()
        assert str(self.tv_1) == 'Power = True, Channel = 3, Volume = 0'

    def test_volume_up(self):
        #tv off, volume increased
        self.tv_1.volume_up()
        assert str(self.tv_1) == 'Power = False, Channel = 0, Volume = 0'

        #tv on, volume increased
        self.tv_1.power()
        self.tv_1.volume_up()
        assert str(self.tv_1) == 'Power = True, Channel = 0, Volume = 1'

        #tv on, muted, volume increased
        self.tv_1.mute()
        self.tv_1.volume_up()
        assert str(self.tv_1) == 'Power = True, Channel = 0, Volume = 2'

        #tv on, volume increased past max
        self.tv_1.volume_up()
        assert str(self.tv_1) == 'Power = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        # tv off, volume decreased
        self.tv_1.volume_down()
        assert str(self.tv_1) == 'Power = False, Channel = 0, Volume = 0'

        #tv on, while volume is at max, decrease volume
        self.tv_1.power()
        self.tv_1.volume_up()
        self.tv_1.volume_up()
        self.tv_1.volume_down()
        assert str(self.tv_1) == 'Power = True, Channel = 0, Volume = 1'

        #tv on, tv muted, volume decreased
        self.tv_1.mute()
        self.tv_1.volume_down()
        assert str(self.tv_1) == 'Power = True, Channel = 0, Volume = 0'

        #tv on, volume decreased past min
        self.tv_1.volume_down()
        assert str(self.tv_1) == 'Power = True, Channel = 0, Volume = 0'