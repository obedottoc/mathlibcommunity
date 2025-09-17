class Length:
    @staticmethod
    def meters_to_feet(meters: float) -> float:
        """Convert Meters to Feet."""
        return meters * 3.281

    @staticmethod
    def feet_to_meters(feet: float) -> float:
        """Convert Feet to Meters."""
        return feet / 3.281

    @staticmethod
    def kilometers_to_miles(km: float) -> float:
        """Convert Kilometers to Miles."""
        return km * 0.621371

    @staticmethod
    def miles_to_kilometers(miles: float) -> float:
        """Convert Miles to Kilometers."""
        return miles / 0.621371

class Time:
    @staticmethod
    def hours_to_minutes(hours: float) -> float:
        """Convert Hours to Minutes."""
        return hours * 60

    @staticmethod
    def minutes_to_hours(minutes: float) -> float:
        """Convert Minutes to Hours."""
        return minutes / 60

    @staticmethod
    def seconds_to_minutes(seconds: float) -> float:
        """Convert Seconds to Minutes."""
        return seconds / 60

    @staticmethod
    def minutes_to_seconds(minutes: float) -> float:
        """Convert Minutes to Seconds."""
        return minutes * 60
    
class NumberSystem:
    @staticmethod
    def decimal_to_binary(number: int) -> str:
        """Convert Decimal to Binary."""
        return bin(number).replace("0b", "")

    @staticmethod
    def binary_to_decimal(binary_str: str) -> int:
        """Convert Binary to Decimal."""
        return int(binary_str, 2)

    @staticmethod
    def binary_to_hex(binary_str: str) -> str:
        """Convert Binary to Hexadecimal."""
        return hex(int(binary_str, 2)).replace("0x", "").upper()