import random

class Pessoa:
    total = 0
    
    def __init__(self, name="nameless", age=-1, sex='?'):
        Pessoa.total += 1
        self.name = name
        self.id = Pessoa.total
        self.age = age 
        self.sex = sex

    def __del__(self):
        Pessoa.total -= 1
    
    def printInfo(self):
        print(f'id: {self.id}, nome: {self.name}, idade: {self.age}, sexo: {self.sex}')

class Trabalhador(Pessoa):
    office_cont = 0
    def __init__(self, name="nameless", age=-1, sex='?', firm="none"):
        # Pessoa.__init__(self, name, age, sex)
        super().__init__(name, age, sex)
        Trabalhador.office_cont += 1
        self.firm = firm
        self.office_id = Trabalhador.office_cont
        
    def printInfo(self):
        print(f'id: {self.id}, nome: {self.name}, idade: {self.age}, sexo: {self.sex} -- trabalha em {self.firm}, id: {self.office_id}')
        # self._displaySecret()
  
class Sociedade:
    # METODOS BASICOS
    nomesM = ['Pedro', 'Paulo', 'Joao', 'Breno']
    nomesF = ['Maria', 'Miranda', 'Carla', 'Lais']
    empresas = ['Amazon', 'Google', 'Netflix']
    
    def __init__(self, populacao=0):
        self.populacao = populacao
        self.pessoas = [Pessoa() for _ in range(populacao)]
        print(f'SOCIEDADE INICIADA. ({populacao})')
        self.executar()
    
    def __del__(self):
        pass
        # print(f'SOCIEDADE ANIQUILADA')
        # print(f'SOBREVIVENTES: {self.populacao}')
        # self.printTodos()
        
    # METODO EXECUTOR
    def executar(self):
        self.popularDados()
        self.aplicarDerivadas()
        self.printTodos()
        self.mortalidade()

    
    # METODOS GERAIS
    def printTodos(self):
        # print("hi")
        # print(pessoa.printInfo() for pessoa in self.pessoas)
        for pessoa in self.pessoas:
            pessoa.printInfo()
    
            
    
    def mortalidade(self):
        for pessoa in self.pessoas:
            if (random.randint(1,10) < 5):
                # self.pessoas.pop(self.pessoas.index(pessoa))
                self.pessoas.remove(pessoa)
                del pessoa
                self.populacao -= 1
                
    def nomear(self):
        for pessoa in self.pessoas:
            if (pessoa.sex == 'M'):
                sorteio = random.randint(0, len(Sociedade.nomesM) - 1)
                pessoa.name = Sociedade.nomesM[sorteio]  
                # pessoa.setNome(Sociedade.nomesM[sorteio])      
            else:
                sorteio = random.randint(0, len(Sociedade.nomesF) - 1)
                pessoa.name = Sociedade.nomesF[sorteio]
                # pessoa.setNome(Sociedade.nomesF[sorteio])      
            
    
    def idades(self):
        for pessoa in self.pessoas:
            pessoa.age = random.randint(1, 101)
    
    def sexos(self):
        for pessoa in self.pessoas:
            pessoa.sex = 'M' if (random.randint(1,2)) == 1 else 'F'
    
    def darTrabalhos(self):
        for i, pessoa in enumerate(self.pessoas):
            if(pessoa.age >= 18 and pessoa.age <= 70):
                sorteio = random.randint(0,len(Sociedade.empresas) - 1)
                # pessoa = Trabalhador(pessoa.name, pessoa.age, self.empresas[sorteio])
                idaux = pessoa.id
                self.pessoas[i] = Trabalhador(pessoa.name, pessoa.age, pessoa.sex, self.empresas[sorteio])
                self.pessoas[i].id = idaux
                

            
    def popularDados(self):
        self.sexos()
        self.nomear()
        self.idades()

    def aplicarDerivadas(self):
        self.darTrabalhos()
                     
s = Sociedade(15)