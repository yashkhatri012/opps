class employee:
    def __init__(self): #constructer
        self.id=123
        self.salary=50000
        self.designation= "SDE"
    def travel(self, destination):
        print(f"empolyee is now travelling to {destination} ")


sam=employee()
print(sam.id)

sam.travel("manali")