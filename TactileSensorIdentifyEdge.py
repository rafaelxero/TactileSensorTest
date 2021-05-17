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

    global rh, ms, ted, log, log_svc

    rh = rtm.findRTC("SimpleFoot0")

    ms = rtm.findRTCmanager()

    ms.load("TactileInfoEdgeDetector")
    ted = ms.create("TactileInfoEdgeDetector")
    ted.setProperty("foot", "left")
    ted.setProperty("Wdin", "100000")

    ms.load("DataLogger")
    log = ms.create("DataLogger", "log")
    log_svc = narrow(log.service("service0"), "DataLoggerService")

def connectComps():

    connectPorts(rh.port("tactileInfoRawOut"), ted.port("tactileInfoRawIn"))

def activateComps():

    rtm.serializeComponents([rh, ted, log])

    rh.start()
    ted.start()
    log.start()

def setupLogger():

    log_svc.add("TimedDoubleSeq", "tactileInfoRaw")
    log_svc.add("TimedDoubleSeq", "edge")
    log_svc.add("TimedDoubleSeq", "circle")
    log_svc.add("TimedDoubleSeq", "contactPoints")
    log_svc.add("TimedDoubleSeq", "noContactPoints")
    log_svc.add("TimedDoubleSeq", "elapsedTime")

    log_svc.maxLength(10000)
    
    connectPorts(rh.port("tactileInfoRawOut"),  log.port("tactileInfoRaw"))
    connectPorts(ted.port("edgeOut"), log.port("edge"))
    connectPorts(ted.port("circleOut"), log.port("circle"))
    connectPorts(ted.port("contactPointsOut"), log.port("contactPoints"))
    connectPorts(ted.port("noContactPointsOut"), log.port("noContactPoints"))
    connectPorts(ted.port("elapsedTimeOut"), log.port("elapsedTime"))
    
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
