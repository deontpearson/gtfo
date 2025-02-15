#! /usr/bin/env python3

import argparse
import sys

from gtfo.gtfobins import get_bins, gtfobins, list_bins
from gtfo.lolbas import get_exe, list_exe, lolbas
from gtfo.utils import colors

GTFOURL = "https://gtfobins.github.io/"
LOLURL = "https://lolbas-project.github.io/"


def givelink(name: str) -> None:
    """Show the link of the give binary or exe

    Arguments:
        name {str} -- Name of the file to give URL of
    """
    exes = get_exe()
    if name in exes.keys():
        url = colors(LOLURL + "/lolbas/{}".format(exes[name]), 94)
    elif name in get_bins():
        url = colors(GTFOURL + "/gtfobins/{}".format(name), 94)
    else:
        print(colors("[!] Couldn't find any bin/exe with name {}".format(name), 91))
        sys.exit(0)
    name = colors(name, 93, True)

    print(
        "--> {n} \t{dash}>\t {link}".format(
            n=name,
            dash=colors(
                "-" * 20,
                93,
            ),
            link=url,
        )
    )


def signal_handler() -> None:
    print(colors("\n\nYou pressed Ctrl+C!", 91))
    sys.exit(0)


def run() -> None:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-b", "--bins", help="Search binaries on GTFOBins")
    group.add_argument("-e", "--exe", help="Search Windows exe on LOLBAS")
    group.add_argument("-w", "--link", help="gtfobins link to the page")
    group.add_argument(
        "-ls", "--list", help="list all the available binaries", choices=["bins", "exe"]
    )

    args = parser.parse_args()

    if args.exe:
        lolbas(args.exe)

    if args.link:
        givelink(args.link)

    if args.bins:
        gtfobins(args.bins)

    if args.list == "exe":
        list_exe()
    elif args.list == "bins":
        list_bins()
