class Student:
	def __init__(self, first_name:str, last_name:str, gpa:float):
		self.first_name = first_name
		self.last_name = last_name
		self.gpa = gpa

	def __repr__(self) -> str:
		return f"FirstName: {self.first_name}\nLastName: {self.last_name}\nGPA: {self.gpa}\n"

	def full_name(self):
		return f"{self.first_name} {self.last_name}"

new_stu = Student("Jose", "Alvarado", 4.0)

print(new_stu)

print(new_stu.full_name())