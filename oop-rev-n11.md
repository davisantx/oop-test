---
aliases: [revisão de poo]
tags: [oop, paradigma, ads]
data: 31/08
status: write
---
# Revisão dos conceitos abordados em Programação Orientada a Objetos na N1.1

*ADS, IFCE CAMPUS ITAPIPOCA - 2026.2*


## Porquê desse paradigma?

Existem vários paradigmas de programação, de fato. 

Mas qual o diferencial deste para os outros?

O paradigma utilizado, quase sempre, quando se aprende a programar é o procedural/imperativo.

Que, de modo geral, separa dados e comportamentos (funções), tornando o código menos coeso -- mais como um bloco de instruções do que com uma abstração que represente coisas do mundo real.

## Objetos e Classes: O que são? Qual a relação entre ambos?

O que seria um objeto? 

Poderia definir como algo concreto. Um exemplo real de algo, que possui seus próprios dados e a capacidade de realizar certos comportamentos.

Quais seriam possíveis exemplos?

##### Do tipo **Aluno**:

```python
davi = Aluno("Davi", 20, "ads", 2)
zaino = Aluno("Zaino", 19, "ads", 2)
adna = Aluno("Adna", 22, "ads", 2)
lucas = Aluno("Lucas", 19, "ads", 2)
```

<br>

Note a sequência de atributos inseridos ao criar os Objetos do tipo Aluno:

- nome: str
- idade: int
- curso: str
- semestre: int

Para possibilitar a criação de objetos do tipo Aluno e permitir a inserção desses dados na criação de cada objeto:

1. Crie a classe **Aluno**:
    ```python
    class Aluno:
        pass
    ```

2. Crie o método **construtor** de **Aluno**
    - Métodos são ações comportamentos atribuídos a cada objeto de uma classe.
    - Métodos se assemelham a funções.
    - O método construtor, em específico, é um método padrão da classe que pode receber dados pelos seus parâmetros, permitindo a inserção de dados no objeto já no momento de sua criação, como em:

      - Aluno("Lucas", 19, "ads", 2)

    - Para **criar** o método **construtor** de **Aluno**:
      ```python
      class Aluno:
        def __init__(self, nome: str, idade: int, curso: str, semestre: int):
            self.nome = nome
            self.idade = idade
            self.curso = curso
            self.semestre = semestre
        ```

3. Atente-se ao **self**

    - O **self** se refere ao objeto que está sendo ou foi criado.
    - Ou seja, o **self** é utilizado pra **se referir aos atributos** e **métodos** dos **objetos** que serão **gerados a partir da classe**. 

##### **Lembrete**:
Lembre sempre que o **objeto** pode ser entendido como:

- **Entidade**:
  - "Entidade do mundo real"
  - "Entidade do domínio"
- **Instância**:
  - "Instância da classe X"

Exemplos de ações que podem ser atribuidas aos objetos **Aluno**:

- passar_de_semestre()

  ```python

  class Disciplina:
      def __init__(self, nome: str, carga_horaria_em_horas):
          self.nome = nome
          self.carga_horaria_em_horas = carga_horaria_em_horas
    
  class Aluno:
    def __init__(self, nome: str, idade: int, curso: str, semestre: int, disciplinas: list[Disciplina]):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.semestre = semestre
        self.disciplinas = disciplinas

    def passar_de_semestre(self, novas_disciplinas: list[Disciplina]):
        self.semestre += 1
        self.disciplinas = novas_disciplinas
  ```

    Observe como seria criar objetos **Aluno** nesse contexto (pseudo-hipotético):

    ```python
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
    ```

E se fosse pra imprimir todos os dados atrelados a cada objeto de **Aluno** de modo formatado?

  ```python
  class Aluno:
    QUANTIDADE_ALUNOS = 0
    
    def __init__(self, nome: str, idade: int, curso: str, semestre: int, disciplinas: list[Disciplina]):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.semestre = semestre
        self.disciplinas = disciplinas
        Aluno.QUANTIDADE_ALUNOS += 1
        self.id = Aluno.QUANTIDADE_ALUNOS
    
    def passar_de_semestre(self, novas_disciplinas: list[Disciplina]):
        self.semestre += 1
        self.disciplinas = novas_disciplinas
    
    def exibir_disciplinas(self):
        saida = ""
        for i, disciplina in enumerate(self.disciplinas):
            saida += disciplina.nome
            if i != len(self.disciplinas) - 1:
                saida += " | "
    
        return saida
                
    def __str__(self):
        str = f"Aluno {self.id}: \n"
  
        str += f"  Nome: {self.nome},\n"
        str += f"  Idade: {self.idade},\n"
        str += f"  Curso: {self.curso},\n"
        str += f"  Semestre: {self.semestre},\n"
        str += f"  Disciplinas: {self.exibir_disciplinas()}\n"
        return str

  ```

Note o que foi feito:
  - Para além da adição do método ```__str__``` que possibita a impressão dos dados do objeto sem a necessidade de algum método auxiliar -- apenas fazendo ```print(objeto)```
  - Adicionou-se um **atributo de classe**, que independe de objetos para ser acessado.
  - O que foi criado neste caso, serve para contabilizar a quantidade de instâncias de ```Aluno``` que foram criadas.
  - Essa contabilização ocorre através do incremento de 1 no atributo em questão, todas as vezes em que o método construtor de ```Aluno``` é chamado -- em toda criação de objeto do tipo ```Aluno```.

<br>
    
Note o resultado da adição do método ```__str__``` em ```Aluno```:
```python
print(davi)
print(zaino)
```

```
Aluno 1:
  Nome: Davi,
  Idade: 20,
  Curso: ads,
  Semestre: 2,
  Disciplinas: Programação Orientada a Objetos | Redes de Computadores | Projeto Social

Aluno 2:
  Nome: Zaino,
  Idade: 19,
  Curso: ads,
  Semestre: 2,
  Disciplinas: Programação Orientada a Objetos | Engenharia de Software | Banco de Dados
```

##### **Análise -- Reflexão**

Considerando todo esse contexto, concorda que alguém que esteja tendo acesso a esse código pode simplesmente modificar qualquer um dos dados atribuidos a qualquer um dos objetos criados e que poderão existir posteriormente?

No código atual, isso é válido:

```python
zaino.idade = -86
zaino.semestre = 487

davi.idade = 998
davi.semestre = -332
```

Esses atributos precisam ser **encapsulados** de um modo a impedir esse tipo de ação.

Mas... Como fazer isso?

1. Atributos privados
    - Parcialmente privados (ainda acessiveis com ```objeto._nome_atributo```)
    ```python
    def __init__(self, nome: str, idade: int, curso: str, semestre: int, disciplinas: list[Disciplina]):
        self._nome = nome
        self._idade = idade
        self._curso = curso
        self._semestre = semestre
        self._disciplinas = disciplinas
        Aluno.QUANTIDADE_ALUNOS += 1
        self._id = Aluno.QUANTIDADE_ALUNOS
    ```
    - Mais privados (não são acessíveis com ```objeto.__nome_atributo```)
    ```python
    def __init__(self, nome: str, idade: int, curso: str, semestre: int, disciplinas: list[Disciplina]):
        self.__nome = nome
        self.__idade = idade
        self.__curso = curso
        self.__semestre = semestre
        self.__disciplinas = disciplinas
        Aluno.QUANTIDADE_ALUNOS += 1
        self.__id = Aluno.QUANTIDADE_ALUNOS
    ```

    Se esses atributos, agora, não podem mais ser acessados do modo tradicional, de que modo os mesmos podem ser acessados ou modificados?

    - **Métodos getters** (acesso)
    - **Métodos setters** (modificação)


##### **Detalhando -- Jeito tradicional de usar getters e setters**


```python
def get_idade(self) -> int:
    return self.__idade
```

```python
def set_idade(self, idade: int):
    if idade <= 0:
        raise ValueError("Idade inválida!")

    self.__idade = idade
```

Exemplo de uso:
```python
# Supondo um aniversário
zaino.set_idade(zaino.get_idade() + 1)
davi.set_idade(davi.get_idade() + 1)

print(f"Nova idade de Zaino: {zaino.get_idade()}")
print(f"Nova idade de Davi: {davi.get_idade()}")
```

##### **Detalhando -- Jeito pythonico de fazer**

```python
@property
def idade(self) -> int:
    return self.__idade

@idade.setter
def idade(self, idade: int):
    if idade <= 0:
        raise ValueError("Idade inválida!")

    self.__idade = idade
```

Exemplo de uso:
```python
# Supondo um aniversário
zaino.idade += 1
davi.idade += 1

print(f"Nova idade de Zaino: {zaino.idade}")
print(f"Nova idade de Davi: {davi.idade}")
```