#!/usr/bin/env python3

from distutils.core import setup
import BitTornado

setup(
    name="bittornado",
    version=BitTornado.version,
    author="Chris Markiewicz, Bram Cohen, John Hoffman, Uoti Arpala et. al.",
    author_email="<effigies@gmail.com>",
    url="https://github.com/effigies/BitTornado",
    description="John Hoffman's fork of the original bittorrent",
    license="MIT",

    packages=["BitTornado",
              "BitTornado.Application",
              "BitTornado.Client",
              "BitTornado.Meta",
              "BitTornado.Network",
              "BitTornado.Storage",
              "BitTornado.Tracker"],

    scripts=["btdownloadheadless.py", "bttrack.py", "btmakemetafile.py",
             "btlaunchmany.py", "btcompletedir.py", "btdownloadcurses.py",
             "btlaunchmanycurses.py", "btmakemetafile.py", "btreannounce.py",
             "btrename.py", "btshowmetainfo.py",
             "btcopyannounce.py", "btsethttpseeds.py"]
)
