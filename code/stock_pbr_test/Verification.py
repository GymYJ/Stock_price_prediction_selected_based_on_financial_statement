from Investment.Verification.VerificationBase import VerificationBase
from datetime import date


class Verification(VerificationBase):
    def __init__(self):
        super().__init__

    def __repr__(self):
        return self.Name

    def setVerification(self):
        super().setVerification()

    def doVerification(self):
        return super().doVerification()

    def saveResult(self):
        return super().saveResult()

    def saveResulToJSON(self):
        return super().saveResulToJSON()

    def saveSummary(self, record, num):
        return super().saveSummary(record, num)
