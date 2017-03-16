# 2013.08.22 22:19:18 Pacific Daylight Time
# Embedded file name: toontown.coghq.MoleFieldBase
import random
HILL_MOLE = 0
HILL_BOMB = 1
HILL_WHACKED = 2
HILL_COGWHACKED = 3

class MoleFieldBase():
    __module__ = __name__
    WHACKED = 1
    MoveUpTimeMax = 1
    MoveUpTimeMultiplier = 0.95
    MoveUpTimeMin = 0.5
    StayUpTimeMax = 7
    StayUpTimeMultiplier = 0.95
    StayUpTimeMin = 3
    MoveDownTimeMax = 1
    MoveDownTimeMultiplier = 0.95
    MoveDownTimeMin = 0.5
    TimeBetweenPopupMax = 1.5
    TimeBetweenPopupMultiplier = 0.95
    TimeBetweenPopupMin = 0.25
    DamageOnFailure = 20

    def getRng(self):
        return random.Random(self.entId * self.level.doId)

    def scheduleMoles(self):
        self.schedule = []
        totalTime = 0
        curMoveUpTime = self.MoveUpTimeMax
        curMoveDownTime = self.MoveDownTimeMax
        curTimeBetweenPopup = self.TimeBetweenPopupMax
        curStayUpTime = self.StayUpTimeMax
        curTime = 3
        eligibleMoles = range(self.numMoles)
        self.getRng().shuffle(eligibleMoles)
        usedMoles = []
        self.notify.debug('eligibleMoles=%s' % eligibleMoles)
        self.endingTime = 0
        randOb = random.Random(self.entId * self.level.doId)
        while self.endingTime < self.GameDuration:
            if len(eligibleMoles) == 0:
                eligibleMoles = usedMoles
                self.getRng().shuffle(usedMoles)
                usedMoles = []
                self.notify.debug('eligibleMoles=%s' % eligibleMoles)
            moleIndex = eligibleMoles[0]
            eligibleMoles.remove(moleIndex)
            usedMoles.append(moleIndex)
            moleType = randOb.choice([HILL_MOLE,
             HILL_MOLE,
             HILL_MOLE,
             HILL_BOMB])
            self.schedule.append((curTime,
             moleIndex,
             curMoveUpTime,
             curStayUpTime,
             curMoveDownTime,
             moleType))
            curTime += curTimeBetweenPopup
            curMoveUpTime = self.calcNextMoveUpTime(curTime, curMoveUpTime)
            curStayUpTime = self.calcNextStayUpTime(curTime, curStayUpTime)
            curMoveDownTime = self.calcNextMoveDownTime(curTime, curMoveDownTime)
            curTimeBetweenPopup = self.calcNextTimeBetweenPopup(curTime, curTimeBetweenPopup)
            self.endingTime = curTime + curMoveUpTime + curStayUpTime + curMoveDownTime

        self.schedule.pop()
        self.endingTime = self.schedule[-1][0] + self.schedule[-1][2] + self.schedule[-1][3] + self.schedule[-1][4]
        self.notify.debug('schedule length = %d, endingTime=%f' % (len(self.schedule), self.endingTime))

    def calcNextMoveUpTime(self, curTime, curMoveUpTime):
        newMoveUpTime = curMoveUpTime * self.MoveUpTimeMultiplier
        if newMoveUpTime < self.MoveDownTimeMin:
            newMoveUpTime = self.MoveDownTimeMin
        return newMoveUpTime

    def calcNextStayUpTime(self, curTime, curStayUpTime):
        newStayUpTime = curStayUpTime * self.StayUpTimeMultiplier
        if newStayUpTime < self.StayUpTimeMin:
            newStayUpTime = self.StayUpTimeMin
        return newStayUpTime

    def calcNextMoveDownTime(self, curTime, curMoveDownTime):
        newMoveDownTime = curMoveDownTime * self.MoveDownTimeMultiplier
        if newMoveDownTime < self.MoveDownTimeMin:
            newMoveDownTime = self.MoveDownTimeMin
        return newMoveDownTime

    def calcNextTimeBetweenPopup(self, curTime, curTimeBetweenPopup):
        newTimeBetweenPopup = curTimeBetweenPopup * self.TimeBetweenPopupMultiplier
        if newTimeBetweenPopup < self.TimeBetweenPopupMin:
            newTimeBetweenPopup = self.TimeBetweenPopupMin
        return newTimeBetweenPopup
# okay decompyling C:\Users\Maverick\Documents\Visual Studio 2010\Projects\Unfreezer\py2\toontown\coghq\MoleFieldBase.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2013.08.22 22:19:18 Pacific Daylight Time
