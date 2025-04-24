
class Television:
    """A class to simulate a television set with power, mute, volume, and channel controls."""

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 50
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 7

    def __init__(self) -> None:
        """Initialize the TV with default settings (off, unmuted, minimum volume and channel)."""
        self._status: bool = False
        self._muted: bool = False
        self._volume: int = Television.MIN_VOLUME
        self._channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """Toggle the power status of the TV."""
        self._status = not self._status

    def mute(self) -> None:
        """Toggle the mute status of the TV."""
        if self._status:
            self._muted = not self._muted

    def channel_up(self) -> None:
        """Increase the TV channel or loop back to minimum if at max."""
        if self._status:
            self._channel = (self._channel + 1) if self._channel < Television.MAX_CHANNEL else Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """Decrease the TV channel or loop back to max if at minimum."""
        if self._status:
            self._channel = (self._channel - 1) if self._channel > Television.MIN_CHANNEL else Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """Increase the volume or do nothing if at max. Unmute if muted."""
        if self._status:
            if self._muted:
                self._muted = False
            if self._volume < Television.MAX_VOLUME:
                self._volume += 1

    def volume_down(self) -> None:
        """Decrease the volume or do nothing if at min. Unmute if muted."""
        if self._status:
            if self._muted:
                self._muted = False
                self._volume = Television.MIN_VOLUME
            if self._volume > Television.MIN_VOLUME:
                self._volume -= 1
    def get_status(self) -> bool:
        """Return the power status of the TV."""
        if self._status:
            return f"The TV is on"
        else:
            return f"The TV is off"
    def get_muted(self)->bool:
        """Return the mute status of the TV."""
        if self._status:
            if self._muted:
                return f"The TV is muted"
            else:
                return f"The TV is not muted"
        else:
            return f"TV is off"
    def get_volume(self) -> int:
        """Return the current volume of the TV."""
        if self._status:
            return f"TV volume is {self._volume}"
        else:
            return f"TV is off"
    def get_channel(self) -> int:
        """Return the current channel of the TV."""
        if self._status:
            return f"TV channel is {self._channel}"
        else:
            return f"TV is off"
    def __str__(self) -> str:
        """Return a string representation of the TV's current state."""
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"
