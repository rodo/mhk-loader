Maheki loader
=============

mhk_loader.py reads a tsung.log files and upload datas to Maheki using
it's API. By default mhk_loader use 5 threads to speed up upload

Tsung scenario must be configured with loglevel="notice"

<tsung loglevel="notice" dumptraffic="false" version="1.0">


Maheki project
==============

See https://gitorious.org/maheki

Usage
=====

$ mhk_loader.py -i TSUNGLOG_DIR -u USERNAME -k APIKEY -s MAHEKI_HOST -b BENCH_ID

Environement variables
=======================

You can set some of environnement variables instead of using option
on command line :

* -u : MAHEKI_USER

* -k : MAHEKI_APIKEY

* -s : MAHEKI_HOST

* port (-p) : MAHEKI_PORT, default 80

* protocol (--protocol) : MAHEKI_PROTOCOL, default "http"

Pypi package
============

mhk_loader is available as a pypi package 

* https://pypi.python.org/pypi/mhk_loader/

Tests
=====

To run test using nose and coverage

$ nosetests tests.py --with-coverage --cover-package=mhk_loader

[![Build Status](https://travis-ci.org/rodo/mhk-loader.png?branch=master)](https://travis-ci.org/rodo/mhk-loader)
