class Calculator:
    def __init__(self, *init_value):
        self.value = init_value

    def add(self, val):
        result=0
        for num in self.value:
            result += num
        return result

cal=Calculator(5,3,4,45,3)
cal.add(3)
print(cal.value)