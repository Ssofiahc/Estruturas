from Pilha import Pilha

class Calc():

    def __init__(self, formato):  

        self.__formato = formato
        self.__p = Pilha()

    def operando(self, v: float):

        self.__p.push(v)
        print(f"{self.__p.top():{self.__formato}}")

    def operador(self, op: str):

        b = self.__p.pop()
        a = self.__p.pop()
        result = 0

        if op == '+':
            result = a + b

        elif op == '-':
            result = a - b

        elif op == '*':
            result = a * b

        elif op == '/':
            if b == 0:
                print("Erro, divisor deve ser diferente de zero!")
                self.__p.push(a)

            else:
                result = a / b

        else:
            print("Erro, operador inválido!")

        self.__p.push(result)
        print(f"Resultado da operação foi: {self.__p.top():{self.__formato}}")

    def libera(self):

        self.__p.libera()
        print("Calculadora limpa!")
    
    def interpreta(self, expr: str):

        el = expr.split()
        
        for i in el:
            if i in "+-*/":
                self.operador(i)

            else:
                self.operando(float(i))