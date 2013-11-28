#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2013 Rodolphe Quiédeville <rodolphe@quiedeville.org>
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

"""
tsung2graphite.py reads tsung's log in json format, export datas to graphite
server.
Your tsung scenario must begin with option backend="json" to force 
tsung dumping log data in json format instead of tsung native format :

<tsung loglevel="notice" dumptraffic="false" version="1.0" backend="json">

"""
import random
import unittest
import mhk_loader as mhk
import json
import tempfile

class FooOpt():
    def init(self):
        self.user = "toto"
        self.key = "papa"

class TestSequenceFunctions(unittest.TestCase):


    def test_build_auth(self):
        #
        datas = FooOpt()
        datas.user = "foo"
        datas.key = "42"

        attend = {'username': 'foo',
                  'key': '42'}

        auth = mhk.build_auth(datas)

        self.assertEqual(attend, auth)

    def test_is_logfile(self):
        self.assertTrue(mhk.is_logfile('tsung1@pyrede.log'))
        self.assertTrue(mhk.is_logfile('tsung2@hypadrie.log'))
        self.assertTrue(mhk.is_logfile('tsung_foo_0@pyrede.log'))
        self.assertFalse(mhk.is_logfile('tsung_controller@jenkins.log'))
        self.assertFalse(mhk.is_logfile('tsung.dump'))
        self.assertFalse(mhk.is_logfile('tsung-fullstats.log'))
        self.assertFalse(mhk.is_logfile('tsung.log'))


if __name__ == '__main__':
    unittest.main()
