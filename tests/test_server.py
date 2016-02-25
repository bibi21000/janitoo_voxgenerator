# -*- coding: utf-8 -*-

"""Unittests for Janitoo-Raspberry Pi Server.
"""
__license__ = """
    This file is part of Janitoo.

    Janitoo is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Janitoo is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Janitoo. If not, see <http://www.gnu.org/licenses/>.

"""
__author__ = 'Sébastien GALLET aka bibi21000'
__email__ = 'bibi21000@gmail.com'
__copyright__ = "Copyright © 2013-2014-2015 Sébastien GALLET aka bibi21000"

import warnings
warnings.filterwarnings("ignore")

import sys, os
import time, datetime
import unittest
import threading
import logging
from pkg_resources import iter_entry_points

from janitoo_nosetests.server import JNTTServer, JNTTServerCommon
from janitoo_nosetests.thread import JNTTThread, JNTTThreadCommon

from janitoo.utils import json_dumps, json_loads
from janitoo.utils import HADD_SEP, HADD
from janitoo.utils import TOPIC_HEARTBEAT, NETWORK_REQUESTS
from janitoo.utils import TOPIC_NODES, TOPIC_NODES_REPLY, TOPIC_NODES_REQUEST
from janitoo.utils import TOPIC_BROADCAST_REPLY, TOPIC_BROADCAST_REQUEST
from janitoo.utils import TOPIC_VALUES_USER, TOPIC_VALUES_CONFIG, TOPIC_VALUES_SYSTEM, TOPIC_VALUES_BASIC

from janitoo.server import JNTServer

class TestVoxgenSerser(JNTTServer, JNTTServerCommon):
    """Test the pi server
    """
    loglevel = logging.DEBUG
    path = '/tmp/janitoo_test'
    broker_user = 'toto'
    broker_password = 'toto'
    server_class = JNTServer
    server_conf = "tests/data/janitoo_voxgenerator.conf"
    hadds = [HADD%(151,0)]

    #~ def test_010_start_heartbeat_stop(self):
        #~ self.wipTest()
        #~ JNTTServerCommon.test_010_start_heartbeat_stop(self)

    def test_011_start_reload_stop(self):
        self.wipTest()
        JNTTServerCommon.test_011_server_start_no_error_in_log(self)

    def test_012_start_reload_threads_stop(self):
        self.wipTest()
        JNTTServerCommon.test_012_start_reload_threads_stop(self)

    def test_020_request_broadcast(self):
        self.wipTest()
        JNTTServerCommon.test_020_request_broadcast(self)

    def test_030_wait_for_all_nodes(self):
        self.wipTest()
        JNTTServerCommon.test_030_wait_for_all_nodes(self)

    def test_040_server_start_no_error_in_log(self):
        self.wipTest()
        JNTTServerCommon.test_040_server_start_no_error_in_log(self)
