import os



class operasBas:
    n1=0
    n2=0
    res=0
    def sumar(self):
        self.res=self.n1+self.n2
        return self.res
    def resta(self):
        self.res=self.n1-self.n2
        return self.res
    def multiplicar(self):
        self.res=self.n1*self.n2
        return self.res
    def dividir(self):
        self.res=self.n1/self.n2
        return self.res
    def pedirNumeros(self):
        self.n1=int(input("n1: "))
        self.n2=int(input("n2: "))


obj=operasBas()

def main():
    while True:
        print("Menu de operciones \n1.- +\n2.- -\n3.- *\n4.- /\n5.- Salir")
        opmenu=int(input("Elige una opcion: "))
        if opmenu>5:
            print("Opcion Invalida")
        if opmenu==5:
            break
        if opmenu==1:
            obj.pedirNumeros()
            obj.sumar()
            obj.imprimir()
            input()
        if opmenu==2:
            obj.pedirNumeros()
            obj.resta()
            obj.imprimir()
            input()
        if opmenu==3:
            obj.pedirNumeros()
            obj.multiplicar()
            obj.imprimir()
            input()
        if opmenu==4:
            obj.pedirNumeros()
            obj.dividir()
            obj.imprimir()
            input()




if __name__=="__main__":
    main()
