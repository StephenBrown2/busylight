"""
"""

from typing import List, Tuple, Type, TypeVar

from busylight.lights import Light, HIDLight, SerialLight

LightType = Type[Light]
LightTypes = List[LightType]


ABSTRACT_LIGHT_SUBCLASSES: LightTypes = [Light, HIDLight, SerialLight]
PHYSICAL_LIGHT_SUBCLASSES: LightTypes = Light.subclasses()
ALL_LIGHT_SUBCLASSES: LightTypes = ABSTRACT_LIGHT_SUBCLASSES + PHYSICAL_LIGHT_SUBCLASSES

BOGUS_DEVICE_ID: Tuple[int, int] = (0xFFFF, 0xFFFF)

HID_LIGHTS = [
    {
        "vendor_id": 0x20A0,
        "product_id": 0x41E5,
        "path": b"/fake/path",
        "product_string": "BlinkStick",
        "serial_number": "BS032974-3.0",
        "release_number": 0x0200,
    },
    {
        "vendor_id": 0x2C0D,
        "product_id": 0x0001,
        "path": b"/fake/path",
        "product_string": "Blynclight",
    },
    {
        "vendor_id": 0x2C0D,
        "product_id": 0x000C,
        "path": b"/fake/path",
        "product_string": "Blynclight",
    },
    {
        "vendor_id": 0x0E53,
        "product_id": 0x2516,
        "path": b"/fake/path",
        "product_string": "Blynclight",
    },
    {
        "vendor_id": 0x2C0D,
        "product_id": 0x000A,
        "path": b"/fake/path",
        "product_string": "Blynclight Mini",
    },
    {
        "vendor_id": 0x0E53,
        "product_id": 0x2517,
        "path": b"/fake/path",
        "product_string": "Blynclight Mini",
    },
    {
        "vendor_id": 0x2C0D,
        "product_id": 0x0010,
        "path": b"/fake/path",
        "product_string": "Blynclight Plus",
    },
    {
        "vendor_id": 0x047F,
        "product_id": 0xD005,
        "path": b"/fake/path",
        "product_string": "Status Indicator",
    },
    {
        "vendor_id": 0x04D8,
        "product_id": 0xF848,
        "path": b"/fake/path",
        "product_string": "Busylight Alpha",
    },
    {
        "vendor_id": 0x27BB,
        "product_id": 0x3BCA,
        "path": b"/fake/path",
        "product_string": "Busylight Alpha",
    },
    {
        "vendor_id": 0x27BB,
        "product_id": 0x3BCD,
        "path": b"/fake/path",
        "product_string": "Busylight Omega",
    },
    {
        "vendor_id": 0x27BB,
        "product_id": 0x3BCF,
        "path": b"/fake/path",
        "product_string": "Busylight Omega",
    },
    {
        "vendor_id": 0x04D8,
        "product_id": 0xF372,
        "path": b"/fake/path",
        "product_string": "Flag",
    },
    {
        "vendor_id": 0x04D8,
        "product_id": 0xF372,
        "path": b"/fake/path",
        "product_string": "Mute",
    },
    {
        "vendor_id": 0x04D8,
        "product_id": 0xF372,
        "path": b"/fake/path",
        "product_string": "Orb",
    },
    {
        "vendor_id": 0x16C0,
        "product_id": 0x27DB,
        "path": b"/fake/path",
        "product_string": "MuteMe Original",
    },
    {
        "vendor_id": 0x20A0,
        "product_id": 0x42DA,
        "path": b"/fake/path",
        "product_string": "MuteMe Original",
    },
    {
        "vendor_id": 0x20A0,
        "product_id": 0x42DB,
        "path": b"/fake/path",
        "product_string": "MuteMe Mini",
    },
    {
        "vendor_id": 0x27B8,
        "product_id": 0x01ED,
        "path": b"/fake/path",
        "product_string": "Blink(1)",
    },
]

SERIAL_LIGHTS = [
    {
        "vendor_id": 0x2047,
        "product_id": 0x03DF,
        "path": b"/path",
        "product_string": "fit-statUSB",
    },
    {
        "vendor_id": 0x10C4,
        "product_id": 0xEA60,
        "path": b"/path",
        "product_string": "MuteSync Button",
    },
]

ALL_LIGHTS = HID_LIGHTS + SERIAL_LIGHTS


class MockDevice:
    def __init__(self, *args, **kwargs) -> None:
        self.path = ""

    def open(*args) -> None:
        pass

    def open_path(self, *args, **kwargs) -> None:
        pass

    def read(self, *args, **kwargs) -> bytes:
        return bytes([0] * 8)

    def write(self, *args, **kwargs) -> int:
        pass

    def send_feature_report(self, *args, **kwargs) -> int:
        pass

    def get_feature_report(self, *args, **kwargs) -> List[int]:
        return [0]
