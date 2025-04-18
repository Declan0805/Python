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
