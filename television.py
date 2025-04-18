class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Status and muted are boolean values.
        Volume and Channel are integer values defaulted to the MIN_VOLUME
        and MIN_CHANNEL values
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int =Television.MIN_VOLUME
        self.__channel: int =Television.MIN_CHANNEL
    """
    Power and mute functions toggle the status and muted boolean variables
    The TV must be on for the mute function to work
    """
    def power(self) -> None:
        self.__status = not self.__status
    def mute(self) -> None:
        #Checks if tv is on first
        if self.__status:
            self.__muted = not self.__muted
    """
    Channel and volume functions change the channel and volume integer variables
    """
    def channel_up(self) -> None:
        #First checks if the TV is on, then checks if it is less than the max channel

        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                #If the channel is greater than the max_Channel it loops back down to the minimum channel
                self.__channel = Television.MIN_CHANNEL
    def channel_down(self) -> None:
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                #If the channel is less than the minimum value it reverts it back to the max channel value
                self.__channel = Television.MAX_CHANNEL
    def volume_up(self) -> None:
        if self.__status:
            if self.__muted:
                #If tv is muted it unmutes the tv
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                #If volume is less than max it increases the volume
                self.__volume += 1

    def volume_down(self) -> None:
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                #If volume is greater than min volume it decreases volume by 1
                self.__volume -= 1
    def __str__(self) -> str:
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"