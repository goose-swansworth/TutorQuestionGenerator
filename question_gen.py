import random as rd

RANGES_NAT = {"smallest" : (0, 12),
          "small" : (10, 30),
          "medium": (10, 100),
          "big": (10, 1000),
          "biggest": (10, 10000)}

RANGES_INT = {"smallest" : (-10, 10),
          "small" : (-30, 30),
          "medium": (-100, 100),
          "big": (-1000, 1000),
          "biggest": (-10000, 10000)}

DIGITS = []

OPERATORS = ["+", "-", "*", "/"]


class Question:

    def __init__(self):
        """Create a new question object"""
        self.type = None
        self.latex_string = None
        self.answer = None

    def __str__(self):
        return self.latex_string


class ArithmeticQuestion(Question):

    def __init__(self, op, num_size, intergers=False, decimal=False, digits=None):
        super().__init__()
        self.left = None
        self.right = None
        self.op = op
        self.is_decimal = decimal
        self.is_int = intergers
        self.num_size = num_size
        if not decimal:
            self.regen()
            while op == "/" and self.right == 0:
                self.regen()
        else:
            self.regen_decimal()
            while op == "/" and self.right == 0:
                self.regen_decimal()


    def regen(self):
        self.lower, self.upper = RANGES_INT[self.num_size] if self.is_int else RANGES_NAT[self.num_size]
        if op in {"+", "-"}:
            self.left = rd.randint(self.lower, self.upper)
            self.right = rd.randint(self.lower, self.upper)
        elif op == "*":
            range_right = list(RANGES_INT.keys()).index(self.num_size)
            self.left = rd.randint(self.lower, self.upper)
            sizes = list(RANGES_INT.keys())
            right_lower, right_upper = RANGES_INT[sizes[rd.randint(0, range_right)]] if self.is_int else RANGES_NAT[sizes[rd.randint(0, range_right)]]
            self.right = rd.randint(right_lower, right_upper)
        else:
            self.left = rd.randint(self.lower, self.upper)
            self.right = rd.randint(*RANGES_INT["smallest"]) if self.is_int else rd.randint(*RANGES_NAT["smallest"])

    def regen_decimal(self):
        pass

    def solve(self):
        match self.op:
            case "+":
                self.answer = self.left + self.right
            case "-":
                self.answer = self.left - self.right
            case "*":
                self.answer = self.left * self.right
            case "/":
                if self.right == 0:
                    self.regen()
                else:
                    if self.is_decimal:
                        self.answer = self.left / self.right
                    else:
                        if self.left % self.right == 0:
                            self.answer = self.left // self.right
                        else:
                            quotient = self.left // self.right
                            self.answer = f"{quotient} x {self.right} + {self.left - self.right * quotient}"

    def __str__(self):
        return f"{self.left} {self.op} {self.right} = {self.answer}"


for _ in range(6):
    op = OPERATORS[rd.randint(0, 3)]
    size = list(RANGES_INT.keys())[rd.randint(0, 4)]
    question = ArithmeticQuestion(op, size, intergers=False)
    question.solve()
    print(question)
