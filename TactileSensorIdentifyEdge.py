#!/usr/bin/python

import rtm
from rtm import *
rtm.nsport  = 2809
rtm.mgrport = 2810
rtm.nshost = "localhost"

import OpenHRP
from OpenHRP import *

import cnoid.Corba
orb = cnoid.Corba.getORB()
rtm.orb = orb
nsloc = "corbaloc:iiop:%s:%d/NameService" % (rtm.nshost, rtm.nsport)
print nsloc
rtm.rootnc = orb.string_to_object(nsloc)._narrow(CosNaming.NamingContext)

from cnoid.grxui import *


##################


def createComps():

    global rh, ms, tp, log, log_svc

    rh = rtm.findRTC("SimpleFoot0")

    ms = rtm.findRTCmanager()

    ms.load("TactileInfoProcessor")
    tp = ms.create("TactileInfoProcessor")

    ms.load("DataLogger")
    log = ms.create("DataLogger", "log")
    log_svc = narrow(log.service("service0"), "DataLoggerService")

def connectComps():

    connectPorts(rh.port("tactileInfoRawOut"), tp.port("tactileInfoRawIn"))

def activateComps():

    rtm.serializeComponents([rh, tp, log])

    rh.start()
    tp.start()
    log.start()

def setupLogger():

    log_svc.add("TimedDoubleSeq", "tactileInfoRaw")
    log_svc.add("TimedDoubleSeq", "tactileInfoProc")

    connectPorts(rh.port("tactileInfoRawOut"),  log.port("tactileInfoRaw"))
    connectPorts(tp.port("tactileInfoProcOut"), log.port("tactileInfoProc"))
    
def init():
    
    print "creating components"
    createComps()

    print "connecting components"
    connectComps()

    print "activating components"
    activateComps()

    print "setting up logger"
    setupLogger()
    
    print "initialized successfully"


##################


MenuList = [
    ['--------- Utility ---------', '#label',
     'Save log',                    'log_svc.save("RTCLog/TactileSensorTest")']
    ]


##################


init()

waitInputMenu(MenuList)
