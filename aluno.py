class Disciplina:
    def __init__(self, nome: str, carga_horaria_em_horas):
        self.nome = nome
        self.carga_horaria_em_horas = carga_horaria_em_horas

class Aluno:
    QUANTIDADE_ALUNOS = 0

    @property
    def idade(self) -> int:
        return self.__idade
    
    @idade.setter
    def idade(self, idade: int):
        if idade <= 0:
            raise ValueError("Idade inválida!")
    
        self.__idade = idade
        
    def __init__(self, nome: str, idade: int, curso: str, semestre: int, disciplinas: list[Disciplina]):
        self.__nome = nome
        self.idade = idade
        self.__curso = curso
        self.__semestre = semestre
        self.__disciplinas = disciplinas
        Aluno.QUANTIDADE_ALUNOS += 1
        self.__id = Aluno.QUANTIDADE_ALUNOS
    
    def passar_de_semestre(self, novas_disciplinas: list[Disciplina]):
        self.__semestre += 1
        self.__disciplinas = novas_disciplinas
    
    def exibir_disciplinas(self):
        saida = ""
        for i, disciplina in enumerate(self.__disciplinas):
            saida += disciplina.nome
            if i != len(self.__disciplinas) - 1:
                saida += " | "
    
        return saida
                
    def __str__(self):
        str = f"Aluno {self.__id}: \n"
    
        str += f"  Nome: {self.__nome},\n"
        str += f"  Idade: {self.__idade},\n"
        str += f"  Curso: {self.__curso},\n"
        str += f"  Semestre: {self.__semestre},\n"
        str += f"  Disciplinas: {self.exibir_disciplinas()}\n"
        return str

    

davi = Aluno(
    nome="Davi",
    idade=20,
    curso="ads",
    semestre=2,
    disciplinas=[
        Disciplina("Programação Orientada a Objetos", 80),
        Disciplina("Redes de Computadores", 80),
        Disciplina("Projeto Social", 40),
    ]
)
zaino = Aluno(
    nome="Zaino",
    idade=19,
    curso="ads",
    semestre=2, 
    disciplinas=[
        Disciplina("Programação Orientada a Objetos", 80),
        Disciplina("Engenharia de Software", 80),
        Disciplina("Banco de Dados", 80),
    ]
)

paulo = Aluno(
    nome="Paulo",
    idade=21,
    curso="fisica",
    semestre=4,
    disciplinas=[
        Disciplina("Calculo 3", 80)
    ]
)

print(davi)
print(zaino)
print(paulo)

# Supondo um aniversário
zaino.idade = zaino.idade + 1
davi.idade = davi.idade + 1

print(f"Nova idade de Zaino: {zaino.idade}")
print(f"Nova idade de Davi: {davi.idade}")


