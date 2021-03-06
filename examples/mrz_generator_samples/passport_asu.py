#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from mrz.generator.td3 import PassportCodeGenerator, dictionary
from examples.functions.functions import open_image


print(PassportCodeGenerator(
        "P",
        "ASU",
        "محمود",
        "عبدالرحيم",
        "A2222222",
        "ASU",
        "710821",
        "F",
        "041204",
        "1000146819",
        dictionary.arabic(),
        force=True))

open_image("passports", "ICAO_Example2.png")
