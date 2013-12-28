from unittest import TestCase
import rethinkdb as r
from rethinkdb.errors import RqlDriverError, RqlRuntimeError

from flask import Flask
from flask_rethinkdb import RethinkDB


class InitTests(TestCase):

    def test_connection_one(self):
        app = Flask(__name__)
        db = RethinkDB(app)

        with app.test_request_context():
            try:
                # Make sure RethinkDB is turned on!
                r.table_create('table').run(db.conn)
            except (RqlDriverError, RqlRuntimeError) as e:
                self.fail(e)
            else:
                # Do some cleanup
                r.table_drop('table').run(db.conn)

    def test_connection_two(self):
        app = Flask(__name__)
        db = RethinkDB()
        db.init_app(app)

        with app.test_request_context():
            try:
                # Make sure RethinkDB is turned on!
                r.table_create('table').run(db.conn)
            except (RqlDriverError, RqlRuntimeError) as e:
                self.fail(e)
            else:
                # Do some cleanup
                r.table_drop('table').run(db.conn)

    def test_connection_with_database(self):
        app = Flask(__name__)
        db = RethinkDB(app, db='test')

        with app.test_request_context():
            try:
                # Make sure RethinkDB is turned on!
                r.table_create('table').run(db.conn)
            except (RqlDriverError, RqlRuntimeError) as e:
                self.fail(e)
            else:
                # Do some cleanup
                r.table_drop('table').run(db.conn)

    def test_connection_with_inexisting_database(self):
        app = Flask(__name__)
        db = RethinkDB(app, db='doesnotexist')

        with app.test_request_context():
            try:
                # Make sure RethinkDB is turned on!
                # Specifying an inexisting database should raise an exception
                r.table_create('table').run(db.conn)
            except (RqlDriverError, RqlRuntimeError):
                pass
            else:
                # Do some cleanup
                r.table_drop('table').run(db.conn)
                self.fail("Should have raised a RqlDriverError")
