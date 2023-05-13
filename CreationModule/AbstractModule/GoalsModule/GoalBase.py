from CreationModule.AbstractModule.ActionsModule.ActionBase import ActionBase


class GoalBase:
    def __init__(self) -> None:
        pass

    def isDesiredStateReached(self) -> bool:
        return False

    def getCorrectiveAction(self) -> ActionBase:
        pass

    def getAmplitude(self) -> float:
        pass

    class GoalBuilder:
        def withDesiredState(self, desiredState) -> GoalBuilder:
            self.desiredState = desiredState
            return self

        def withCorrectiveAction(self, correctiveAction) -> GoalBuilder:
            self.correctiveAction = correctiveAction
            return self

        def withAmplitude(self, amplitude) -> GoalBuilder:
            self.amplitude = amplitude
            return self

        def build(self) -> GoalBase:
            return GoalBase(self.desiredState, self.correctiveAction, self.amplitude)
