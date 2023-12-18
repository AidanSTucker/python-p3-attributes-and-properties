class Person:
    approved_jobs = [
        "Admin", "Customer Service", "Human Resources", "ITC", "Production", "Legal", 
        "Finance", "Sales", "General Management", "Research & Development", "Marketing", "Purchasing"
    ]

    def __init__(self, name="", job=""):
        self.name = name
        self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be string between 1 and 25 characters.")
            self._name = ""
        else:
            self._name = value.title()

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value not in self.approved_jobs and value != "":
            print("Job must be in list of approved jobs.")
            self._job = ""
        else:
            self._job = value
