#! /usr/bin/env python3

import re
import argparse
import pyperclip


def strip_commas(user_string: str) -> str:
    return re.sub(r',', '', user_string)


def get_glink(pat_num: str) -> str:
    google_prefix = "https://patents.google.com/patent/US"

    return f"{google_prefix}{pat_num}"


def get_plink(pat_num: str) -> str:
    uspto_prefix = "http://patft1.uspto.gov/netacgi/nph-Parser?patentnumber="

    return f"{uspto_prefix}{pat_num}"


def get_excel_hyperlink(pat_num: str, link: str) -> str:
    return f'=HYPERLINK("{link}", "{pat_num}")'


def main():
    parser = argparse.ArgumentParser(description='Linkify some patent numbers.')
    parser.add_argument('source', nargs='?', help="linkify patents at the source")
    parser.add_argument('-g', '--google', action='store_true', help="link to Google patents")
    args = parser.parse_args()
    print(args)  # debug

    # set whether to convert to PTO or Google links
    if args.google:
        linkify = get_glink
    else:
        linkify = get_plink

    if args.source is None:
        clean_text = strip_commas(pyperclip.paste()).strip()  # remove whitespace and commas
        patent_link = linkify(clean_text)
        pyperclip.copy(patent_link)

    # TODO: elif args.source is a path
        # linkify excel sheet
    # TODO: elif args.source is a link
        # linkify Google sheet


if __name__ == '__main__':
    main()
