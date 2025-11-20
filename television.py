class Television:
    MIN_VOLUME : int = 0
    MAX_VOLUME : int = 2
    MIN_CHANNEL : int = 0
    MAX_CHANNEL : int = 3

    def __init__(self) -> None:
        """
        Creates a television object.

        Default values are:
        tv is off, muted, set to minimum volume (0), and minimum channel (0).
        """

        self.__status: bool = False
        self.__muted: bool = False
        self.__volume : int = self.MIN_VOLUME
        self.__channel : int = self.MIN_CHANNEL

    def power(self) -> None:
        """
        Sets the television power on / off.
        """

        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        """
        Mute / unmutes the television.
        """

        if self.__status == True:
            if self.__muted == False:
                self.__muted = True
            else:
                self.__muted = False

    def channel_up(self) -> None:
        """
        Increase the television channel
        """

        if self.__status == True:
            if self.__channel < self.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = self.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Decrease the television channel
        """

        if self.__status == True:
            if self.__channel > self.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increase the television volume
        """

        if self.__status == True:
            self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decrease the television volume
        """

        if self.__status == True:
            self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        returns a string of televisions current status
        :return: sting showing the current power status, channel, and volume.
        """
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = 0"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"