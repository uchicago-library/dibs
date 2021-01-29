'''
database.py: object definitions for the database

This uses Peewee (http://docs.peewee-orm.com/en/latest/), a small ORM that
allows writing database code entirely in terms of Python objects without
having to know much about SQL.
'''

from decouple import config
from peewee import SqliteDatabase, Model
from peewee import CharField, TextField, IntegerField, SmallIntegerField
from peewee import ForeignKeyField, AutoField, DateTimeField, BooleanField


# Database object schemas
# .............................................................................

_db = SqliteDatabase(config('DATABASE_FILE', default='dibs.db'))

class BaseModel(Model):
    class Meta:
        database = _db


# Each item available for loaning out gets a separate Item object in the
# database.  We may allow more than one simultaneous loan of a given item, so
# that's why there's a num_copies field to represent how many copies of the
# thing we're allowed to loan.  The duration is set per-item because we could
# very well allow some items to be loaned out for longer periods than others.
# Duration is in terms of hours right now.
#
# The TIND Id is not strictly necessary for our purposes, but it's here to
# make it easier for administrators to jump from the list page to the record
# in TIND.

class Item(BaseModel):
    itemid     = AutoField()            # Auto-increment primary key.
    barcode    = CharField(unique = True)
    tind_id    = CharField()
    title      = TextField()
    author     = TextField()
    year       = CharField()
    edition    = CharField()
    thumbnail  = TextField()            # URL to an image.
    num_copies = SmallIntegerField()
    duration   = SmallIntegerField()    # Assumed to be hours.
    ready      = BooleanField(default = False)


# Loans are currently stored in terms of a combination of item + user identity.
# A user can have multiple items out; they just get represented as separate
# Loan object instances. Similarly, an Item can be loaned to multiple people,
# if there are multiple copies of the item.
#
# Loans periods could be represented as start + duration, but since we'll need
# to test against the end of a loan repeatedly, it's easier to store the end
# time here.

class Loan(BaseModel):
    loanid  = AutoField()
    item    = ForeignKeyField(Item, column_name = 'itemid', backref = 'loanref')
    user    = TextField()               # Login, probably someone@caltech.edu
    started = DateTimeField()           # When did the patron start the loan?
    endtime = DateTimeField()           # When does the loan end?


# Our policy is that users can't immediately check out the same item; they
# must instead wait a certain amount of time.  This next object is used to
# help remember recent loans.

class Recent(BaseModel):
    recentid = AutoField()
    item     = ForeignKeyField(Item, column_name = 'itemid', backref = 'loanref')
    user     = TextField()               # Login, probably someone@caltech.edu
    nexttime = DateTimeField()           # When can they loan it again?
