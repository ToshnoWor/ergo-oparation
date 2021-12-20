class Operation:
    def __init__(self, type_operation, values):
        match type_operation:
            case 'P':
                self.operation_type = 'P'
                self.next = None
                self.b = values['B']
                self.m = values['M']
                self.d = values['D']
            case 'K':
                self.operation_type = 'K'
                self.next = None
                self.k11 = values['K11']
                self.k00 = values['K00']
                self.m = values['M']
                self.d = values['D']
            case 'RR':
                self.rr(values)
            case 'RK':
                self.rk(values)
            case 'RKR':
                self.rkr(values)
            case _:
                pass

    def rr(self, values):
        self.operation_type = 'P'
        self.next = None
        self.b = 1.0
        self.m = 0.0
        self.d = 0.0
        for p in values:
            self.b *= p.get_b()
            self.m += p.get_m()
            self.d += p.get_d()

    def rk(self, values):
        self.operation_type = 'P'
        self.next = None
        p = values['P']
        k = values['K']
        b1 = p.get_b()
        b0 = 1 - b1
        k00 = k.get_k('00')
        k11 = k.get_k('11')
        k10 = 1 - k11
        ml = 1 / (1 - (b1 * k10 + b0 * k00))
        dl = (b1 * k10 + b0 * k00) / ((1 - (b1 * k10 + b0 * k00)) * (1 - (b1 * k10 + b0 * k00)))
        self.b = b1 * k11 * ml
        self.m = (p.get_m() + k.get_m()) * ml
        self.d = dl * (p.get_m() + k.get_m()) * (p.get_m() + k.get_m()) + (
                p.get_d() + k.get_d()
        ) * ml

    def rkr(self, values):
        self.operation_type = 'P'
        self.next = None
        p1 = values['P1']
        p2 = values['P2']
        k = values['K']
        b11 = p1.get_b()
        b10 = 1 - b11
        b21 = p2.get_b()
        b20 = 1 - b21
        b1 = b11 * b21
        b0 = 1 - b1
        k11 = k.get_k('11')
        k10 = 1 - k11
        k00 = k.get_k('00')
        k01 = 1 - k00

        self.b = b11 * k11 * (1 - k00 * b20) / (k01 + b11 * b21 * (k11 - k01))
        a = b11 * k10 + b10 * k00
        b = 1 - (b1 * k10 + b0 * k00)
        c1 = a / (b ** 2)
        c2 = a / b
        c3 = (b11 * k11 + b10 * k01) / (b ** 2)
        d1 = p1.get_m() + k.get_m()
        d = d1 + p2.get_m()
        c4 = d ** 2
        self.m = d1 + d * c2
        self.d = p1.get_d() + k.get_d() + (p1.get_d() + p2.get_d() + k.get_d()) * c2 + c1 * c2 * c3 * c4

    def add_next_for_p(self, o):
        self.next = o

    def add_next_for_k(self, o1, o2):
        self.next = [o1, o2]

    def get_b(self):
        return self.b

    def get_m(self):
        return self.m

    def get_d(self):
        return self.d

    def get_k(self, code):
        match code:
            case '11':
                return self.k11
            case '00':
                return self.k00

    def get_type(self):
        return self.operation_type

    def to_string(self):
        if self.operation_type == 'P':
            return f'b= {self.b} m= {self.m} d= {self.d}'
        return f'k11= {self.k11} k00= {self.k00} m= {self.m} d= {self.d}'


class Operations:
    def __init__(self):
        self.operations = []

    def add_operation(self, o):
        self.operations.append(o)
