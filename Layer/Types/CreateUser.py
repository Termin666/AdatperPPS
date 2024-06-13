class CreateUser:
    def __init__(self, email: str, employeeId: int):
        self.email = email
        self.employeeId = employeeId

    def __repr__(self):
        return f"CreateUser(email={self.email}, employeeId={self.employeeId})"