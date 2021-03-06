from Person import Person

#TODO make name private
class Student(Person):
	__doc__ = "Student"

	points = 0
	marks = 0
	semester = 0
	totalSemesters = 8
	totalMarks = 0
	modules = []
	moduleEnrollments = {}
	facult = ""

	resultFromSimluation = True # Result from simualtuion: True -> advance to next year; False -> expelled
	passedByCompFromSimulation = 0 # Counter of a number of passed by compensation modules

	def __init__(self, studentID, name = "Student X", gender = "m", leavingCertificate = 700):
		self.studentID = studentID
		Person.__init__(self, name, gender)
		self.modules = []
		self.moduleEnrollments = {}
		self.semester = 1
		self.leavingCertificate = leavingCertificate #TODO: check Irish system
		self.faculty = ""

	def getModules(self):
		return self.modules

	def getCourse(self):
		return self.course

	#TODO
	def canTake(self, module):
		return True

	#TODO
	def hasTaken(self, module):
		return True

	def getSemester(self):
		return self.semester

	def getTotalSemesters():
		return self.totalSemesters

	def getTotalMarks():
		return self.totalMarks