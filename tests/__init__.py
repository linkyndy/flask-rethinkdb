from unittest import TestCase
import rethinkdb as r
from rethinkdb.errors import RqlDriverError

from flask import Flask
from flask_rethinkdb import RethinkDB


class InitTests(TestCase):

    def test_one(self):
        app = Flask(__name__)
        db = RethinkDB(app)

        with app.test_request_context():
            try:
                # Make sure RethinkDB is turned on!
                r.db_list().run(db.conn)
            except RqlDriverError as e:
                self.fail(e)

    def test_two(self):
        app = Flask(__name__)
        db = RethinkDB()
        db.init_app(app)

        with app.test_request_context():
            try:
                # Make sure RethinkDB is turned on!
                r.db_list().run(db.conn)
            except RqlDriverError as e:
                self.fail(e)
