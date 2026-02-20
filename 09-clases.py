class persona:
    def inicializar(self,nom):
        self.nombre=nom
    def imprimir(self):
        print("Nombre",self.nombre)

persona1=persona()
persona1.inicializar("Pedro")
persona1.imprimir()

persona2=persona()
persona2.inicializar("Carla")
persona2.imprimir()

class operasBas:
    n1=0
    n2=0
    res=0
    def sumar(self,a,b):
        return a+b
    def pedirNumeros(self):
        self.n1=int(input("n1: "))
        self.n2=int(input("n2: "))
        print("La suma es: ",self.sumar(self.n1,self.n2))
obj=operasBas()
obj.pedirNumeros()
