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
import os


class FooOpt():
    def init(self):
        self.user = "toto"
        self.key = "papa"


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        """
        Unset env var
        """
        if 'MAHEKI_PORT' in os.environ:
            del os.environ["MAHEKI_PORT"]
        if 'MAHEKI_PROTOCOL' in os.environ:
            del os.environ["MAHEKI_PROTOCOL"]


    def test_build_auth(self):
        #
        datas = FooOpt()
        datas.user = "foo"
        datas.key = "42"

        attend = {'username': 'foo',
                  'key': '42'}

        auth = mhk.build_auth(datas)

        self.assertEqual(attend, auth)

    def test_logfiles(self):
        datas = ['tsung.log', 'tsung0@pyrede.log',
                 'tsung-fullstats.log', 'tsung1@hypadrie.log',
                 'tsung.dump', 'osmpule.xml',
                 'match.log', 'tsung_controller@jenkins.log']
        result = mhk.logfiles(datas, "")

        attend = ['tsung0@pyrede.log', 'tsung1@hypadrie.log']

        self.assertEqual(result, attend)

    def test_logfiles_path(self):
        datas = ['tsung.log', 'tsung0@pyrede.log',
                 'tsung-fullstats.log', 'tsung1@hypadrie.log',
                 'tsung.dump', 'osmpule.xml',
                 'match.log', 'tsung_controller@jenkins.log']
        result = mhk.logfiles(datas, "/tmp")

        attend = ['/tmp/tsung0@pyrede.log', '/tmp/tsung1@hypadrie.log']

        self.assertEqual(result, attend)

    def test_logfiles_empty(self):
        datas = []
        result = mhk.logfiles(datas, "")
        attend = []
        self.assertEqual(result, attend)

    def test_arg_parse(self):
        """
        Command line options
        """
        opt = mhk.arg_parse(["foo"])
        self.assertEqual(opt.infile, None)
        self.assertEqual(opt.port, 80)

    def test_arg_parse_port(self):
        """
        Command line options
        """
        opt = mhk.arg_parse(["foo","-p","870"])
        self.assertEqual(opt.port, "870")

    def test_arg_parse_protocol(self):
        """
        Command line options
        """
        opt = mhk.arg_parse(["foo","--protocol","https"])
        self.assertEqual(opt.protocol, "https")

    def test_upload_api(self):

        data = {"value": 123,
                "datetms": 123456789,
                "name": "foo",
                "run": 1}

        result = {"value": data['value'],
                  "datetms": data['datetms'],
                  "name": data['name'],
                  "run": "/api/v1/run/{}/".format(data['run'])}

        self.assertEqual(mhk.upload_api(data), result)


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    itersuite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    runner.run(itersuite)
