# 2013.08.22 22:17:31 Pacific Daylight Time
# Embedded file name: toontown.classicchars.DistributedSuperGoofy
from pandac.PandaModules import *
import DistributedCCharBase
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from toontown.classicchars import DistributedGoofySpeedway
import CharStateDatas
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
import DistributedCCharBase

class DistributedSuperGoofy(DistributedGoofySpeedway.DistributedGoofySpeedway):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedSuperGoofy')

    def __init__(self, cr):
        try:
            self.DistributedGoofySpeedway_initialized
        except:
            self.DistributedGoofySpeedway_initialized = 1
            DistributedCCharBase.DistributedCCharBase.__init__(self, cr, TTLocalizer.SuperGoofy, 'sg')
            self.fsm = ClassicFSM.ClassicFSM(self.getName(), [State.State('Off', self.enterOff, self.exitOff, ['Neutral']), State.State('Neutral', self.enterNeutral, self.exitNeutral, ['Walk']), State.State('Walk', self.enterWalk, self.exitWalk, ['Neutral'])], 'Off', 'Off')
            self.fsm.enterInitialState()
            self.nametag.setName(TTLocalizer.Goofy)

    def walkSpeed(self):
        return ToontownGlobals.SuperGoofySpeed
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\toontown\classicchars\DistributedSuperGoofy.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:17:31 Pacific Daylight Time
