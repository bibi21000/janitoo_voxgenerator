# -*- coding: utf-8 -*-
"""The Raspberry nxp thread

http://www.framboise314.fr/jai-teste-pour-vous-la-carte-explore-nfc-delement-14-12/

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
__copyright__ = "Copyright © 2013-2014-2015-2016 Sébastien GALLET aka bibi21000"

import logging
logger = logging.getLogger(__name__)
import os, sys
import threading

from janitoo.thread import JNTBusThread, BaseThread
from janitoo.options import get_option_autostart
from janitoo.utils import HADD
from janitoo.node import JNTNode
from janitoo.value import JNTValue
from janitoo.component import JNTComponent
from janitoo.bus import JNTBus
try:
    import voxgenerator
except:
    logger.exception('Can"t import voxgenerator')

##############################################################
#Check that we are in sync with the official command classes
#Must be implemented for non-regression
from janitoo.classes import COMMAND_DESC

COMMAND_WEB_CONTROLLER = 0x1030
COMMAND_WEB_RESOURCE = 0x1031
COMMAND_DOC_RESOURCE = 0x1032

assert(COMMAND_DESC[COMMAND_WEB_CONTROLLER] == 'COMMAND_WEB_CONTROLLER')
assert(COMMAND_DESC[COMMAND_WEB_RESOURCE] == 'COMMAND_WEB_RESOURCE')
assert(COMMAND_DESC[COMMAND_DOC_RESOURCE] == 'COMMAND_DOC_RESOURCE')
##############################################################

def make_listener(**kwargs):
    return ListenerComponent(**kwargs)

class VoxgenBus(JNTBus):
    """A bus to manage NXP
    """
    def __init__(self, **kwargs):
        """
        :param kwargs: parameters transmitted to :py:class:`smbus.SMBus` initializer
        """
        JNTBus.__init__(self, **kwargs)
        self.lock =  threading.Lock()
        #~ self.mifare = None

    def check_heartbeat(self):
        """Check that the component is 'available'
        """
        #~ print "it's me %s : %s" % (self.values['upsname'].data, self._ups_stats_last)
        #~ if self.mifare is not None:
            #~ return True
        return False

    def start(self, mqttc, trigger_thread_reload_cb=None):
        """Start the bus
        """
        JNTBus.start(self, mqttc, trigger_thread_reload_cb)
        #~ try:
            #~ self.mifare = nxppy.Mifare()
        #~ except:
            #~ logger.exception("Exception when starting NXP bus")

    def stop(self):
        """Stop the bus
        """
        #~ try:
            #~ self.mifare = None
        #~ except:
            #~ logger.exception("Exception when stopping NXP bus")
        JNTBus.stop(self)

class ListenerComponent(JNTComponent):
    """ A resource """

    def __init__(self, **kwargs):
        """
        """
        self._inputs = {}
        oid = kwargs.pop('oid', 'voxgen.listener')
        product_name = kwargs.pop('product_name', "Voxgenerator listener")
        name = kwargs.pop('name', "Voxgenerator listener")
        JNTComponent.__init__(self, oid=oid, name=name, product_name=product_name, **kwargs)

    def start(self, mqttc):
        """Start the component.

        """
        JNTComponent.start(self, mqttc)
        configs = len(self.values["add"].get_index_configs())
        for config in range(configs):
            try:
                pass
            except:
                logger.exception("Exception when starting NXP Reader component")
        return True

    def stop(self):
        """Stop the component.

        """
        JNTComponent.stop(self)
        return True

    def loop(self, stopevent):
        """loop
        Need to de threaded as acquire can be a long operation
        """
        pass
