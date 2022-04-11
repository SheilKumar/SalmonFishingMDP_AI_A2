class Action:
    def __init__(self) -> None:
        pass

    def getTransitionAndRewardProbabilities(self):
        pass

class ReBreed(Action):
    def __init__(self) -> None:
        super().__init__()

    def getTransitionAndRewardProbabilities(self,state):
        actionMap = {
            "empty" : {"empty"     : (0.05,-4),
                        "low"      : (0.85,-4),
                        "medium"   : (0.10,-4)},
            "low"   : {"medium"    : (0.8,-2.50),
                        "high"     : (0.2,-2.50)},
            "medium": {"high"      : (1, -1)},
            "high"  : {"high"      : (1, -0.5)}
        }

        return actionMap[state]

class NotFish(Action):
    def __init__(self) -> None:
        super().__init__()

    def getTransitionAndRewardProbabilities(self,state):
        actionMap = {
            "empty" : {"empty"  : (1,0)},
            "low"   : {"empty"  : (0.05,0),
                        "low"   : (0.70,0),
                        "medium": (0.25,0)},
            "medium": {"low"    : (0.05,0),
                        "medium": (0.90,0),
                        "high"  : (0.05,0)},
            "high"  : {"medium" : (0.20,0),
                        "high"  : (0.80,0)}
        }

        return actionMap[state]

class Fish(Action):
    def __init__(self) -> None:
        super().__init__()

    def getTransitionAndRewardProbabilities(self,state):
        actionMap = {
            "empty" : {"empty"  : (1,0)},
            "low"   : {"empty"  : (0.65,0.60),
                        "low"   : (0.35,0.60)},
            "medium": {"low"    : (0.35,1.70),
                        "medium": (0.60,1.70),
                        "high"  : (0.05,1.70)},
            "high"  : {"medium" : (0.65,2.5),
                        "high"  : (0.35,2.5)}
        }

        return actionMap[state]


