"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi81um4dadc9vm36240-a.oregon-postgres.render.com",
        database="postgresql_luh0",
        user="postgresql_luh0_user",
        password="inhlX593e27VDf8i8u2VKpFjXy4kW7zR")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes