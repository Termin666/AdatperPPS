from typing import List
from Layer.Types.ReportValue import ReportValue


class Report:
    def __init__(self, year: int, employeeId: str, values: List[ReportValue]):
        self.year = year
        self.employeeId = employeeId
        self.values = values

    def __repr__(self):
        return f"Report(year={self.year}, employeeId={self.employeeId}, values={self.values})"