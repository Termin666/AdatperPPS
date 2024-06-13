class ReportValue:
    def __init__(self, criterionKey: str, criterionValue: float):
        self.criterionKey = criterionKey
        self.criterionValue = criterionValue

    def __repr__(self):
        return f"ReportValue(criterionKey={self.criterionKey}, criterionValue={self.criterionValue})"