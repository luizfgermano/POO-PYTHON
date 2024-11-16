
# Exercício 1: Classe Retângulo
# Crie uma classe chamada Retangulo que tenha:

# Atributos: largura e altura (definidos na inicialização).
# Métodos:
# area() que retorna a área do retângulo.
# perimetro() que retorna o perímetro do retângulo.
# Teste a classe:

# Crie uma instância de Retangulo com largura 5 e altura 10.
# Mostre no console a área e o perímetro desse retângulo.


class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        
        
    def area(self):
        return self.largura * self.altura
    
    
    def perimetro(self):
        return 2 * (self.largura + self.altura)
    



retangulo1 = Retangulo(5, 10)


retangulo1.area()

retangulo1.perimetro()


retangulo2 = Retangulo(25, 48)


retangulo2.area()

retangulo2.perimetro()



#------------------------------------------------------------------------------




























