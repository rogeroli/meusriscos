# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property


class Guitarra(Node):
    modelo = ndb.StringProperty(required=True)
    marca = ndb.StringProperty(required=True)
    preco = property.SimpleCurrency(required=True)
    detalhes = ndb.StringProperty(required=True)

