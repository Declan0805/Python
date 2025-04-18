class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self, status, muted, volume, channel):
        self.__status = status
        self.__muted = muted
        self.__volume = volume
        self.__channel = channel