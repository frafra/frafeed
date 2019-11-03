#!/usr/bin/env python3

from sqlitewrapper import SQLiteWrapper
import argparse
import bs4
import datetime
import feedparser
import json


class SQLHelpers:
    @staticmethod
    def feed(url):
        return json.dumps(feedparser.parse(url))

    @staticmethod
    def parsed2date(parsed):
        return str(datetime.datetime(*eval(parsed)[:6]))

    @staticmethod
    def html2text(html):
        return bs4.BeautifulSoup(html, "html.parser").text


def parse_args():
    parser = argparse.ArgumentParser(description="FraFeed")
    parser.add_argument("--filename", default="feed.db")
    subparsers = parser.add_subparsers(title="command", dest="command")
    subparsers.required = True
    with SQLiteWrapper() as feed:
        for query, variables in feed.queries.items():
            if query.endswith("_cursor"):
                continue
            subparser = subparsers.add_parser(query)
            for variable in variables:
                subparser.add_argument(variable)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    with SQLiteWrapper(args.filename, SQLHelpers) as feed:
        feed.create_tables()
        results = getattr(feed, str(args.command))(**vars(args))
        print(json.dumps(results, indent=4, ensure_ascii=False))
