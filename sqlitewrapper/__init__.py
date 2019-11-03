import anosql
import functools
import inspect
import sqlite3


class SQLiteWrapper:
    def __init__(self, filename=":memory:", sqlhelpers=object):
        self.filename = filename
        self.sqlhelpers = sqlhelpers
        self.queries = {}

    def __enter__(self):
        self.conn = sqlite3.connect(self.filename)

        # Load functions
        functions = inspect.getmembers(self.sqlhelpers, inspect.isfunction)
        for name, function in functions:
            parameters = inspect.signature(function).parameters
            self.conn.create_function(name, len(parameters), function)

        # Load queries
        queries = anosql.from_path("sql", "sqlite3")
        for query in queries.available_queries:
            function = getattr(queries, query)
            setattr(self, query, functools.partial(function, self.conn))
            self.queries[query] = set()
            for match in anosql.patterns.var_pattern.finditer(function.sql):
                var_name = match.group("var_name")
                if var_name:
                    self.queries[query].add(var_name)

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.commit()
        self.conn.close()
