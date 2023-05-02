disciplinas = []


def cadastro_de_disciplina():
  encontrou = 0
  while True:
    codigo = int(input("Insira o código da disciplina: "))
    for disciplina in disciplinas:
      if (codigo == disciplina[0]):
        print("Disciplina já cadastrada!")
        encontrou = 1
        break
      else:
        continue
    if (encontrou == 0):
      break

  if (encontrou == 0):
    nome_da_disciplina = str(input("Insira o nome da disciplina: "))
    ano = int(input("Insira o ano: "))
    periodo = int(input("Insira o período: "))
    semestre = str(ano) + "." + str(periodo)
    alunos = []
    professores = []
    carga_horaria = int(input("Insira a carga horária da disciplina: "))
    while True:
      n = int(
        input(
          "Insira a quantidade de dias da semana em que a disciplina será lecionada, 2 ou 3: "
        ))
      if (n == 2 or n == 3):
        break
      else:
        print("Insira um valor válido!")
    dias = []
    i = 0
    while i < n:
      while True:
        dia_da_semana = int(
          input(
            "Insira o dia da semana desejado: 1-Segunda, 2-Terça, 3-Quarta, 4-Quinta, 5-Sexta, 6-Sábado "
          ))
        if (dia_da_semana != 1 and dia_da_semana != 2 and dia_da_semana != 3
            and dia_da_semana != 4 and dia_da_semana != 5
            and dia_da_semana != 6):
          print("Digite um valor válido!")
          continue
        else:
          dias.append(dia_da_semana)
          i = i + 1
          break
    while True:
      horario = int(
        input(
          "Selecione o horário da disciplina: 1-Das 8 às 10, 2-Das 10 às 12, 3-Das 12 às 14, 4- Das 14 às 16, 5-Das 16 às 18, 6-Das 18 às 20, 7-Das 20 às 22 "
        ))
      if (horario != 1 and horario != 2 and horario != 3 and horario != 4
          and horario != 5 and horario != 6 and horario != 7):
        print("Insira um valor válido!")
      else:
        break

    disciplina = ((codigo, nome_da_disciplina, semestre, professores, alunos,
                   carga_horaria), (dias, horario))
    disciplinas.append(disciplina)


def pesquisar_disciplina():
  codigo = int(input("Insira o código da disciplina desejada: "))
  aux = 0
  for disciplina in disciplinas:
    if (codigo == disciplina[0][0]):
      aux = 1
      break
  if (aux == 1):
    return disciplina
  else:
    return None


def lista_disciplinas():
  aux = 1
  for disciplina in disciplinas:
    if (disciplina[0][1] == None):
      aux = 0
      continue
    else:
      aux = 1
      print(
        f'Nome da disciplina: {disciplina[0][1]}, Código da disciplina: {disciplina[0][0]}'
      )
  if (aux == 0):
    print("Nenhuma disciplina cadastrada!")


professores = []


def cadastra_professor():
  aux = 0
  while True:
    cod_disc = int(
      input(
        "Insira o codigo da disciplina que deseja cadastrar o professor: "))
    for disciplina in disciplinas:
      if (cod_disc == disciplina[0][0]):
        aux = 1
        break
      else:
        continue
    if (aux == 1):
      disc = disciplina
      break
    else:
      print("Disciplina não cadastrada! Tente novamente!")

  encontrou = 0

  while True:
    codigo = int(input("Insira o código do professor: "))
    for professor in professores:
      if (codigo == professor[0]):
        print("Professor já cadastrado. Tente novamente!")
        encontrou = 1
        break
      else:
        continue

    if (encontrou == 0):
      nome_do_professor = str(input("Insira o nome do professor: "))
      professor = (codigo, nome_do_professor)
      disc[0][3].append(professor)
      break


alunos = []


def cadastra_aluno():
  aux = 0
  while True:
    cod_disc = int(
      input("Insira o codigo da disciplina que deseja cadastrar o aluno: "))
    for disciplina in disciplinas:
      if (cod_disc == disciplina[0][0]):
        aux = 1
        break
      else:
        continue
    if (aux == 1):
      disc = disciplina
      break
    else:
      print("Disciplina não cadastrada! Tente novamente!")

  encontrou = 0
  while True:
    matricula = input("Insira a matrícula do aluno: ")
    for aluno in alunos:
      if (matricula == aluno[0]):
        print("Aluno já cadastrado. Tente novamente!")
        encontrou = 1
        break
      else:
        continue
    if (encontrou == 0):
      nome_do_aluno = str(input("Insira o nome do aluno: "))
      curso = str(input("Insira o nome do curso: "))
      notas = []
      aluno = (matricula, nome_do_aluno, curso, notas)
      disc[0][4].append(aluno)
      break


def lista_professores():
  aux = 0
  while True:
    cod_disc = int(
      input(
        "Insira o código da disciplina que deseja listar os professores: "))
    for disciplina in disciplinas:
      if (cod_disc == disciplina[0]):
        aux = 1
        break
      else:
        continue
    if (aux == 1):
      disc = disciplina
      break
    else:
      print("Disciplina não cadastrada! Tente novamente!")

  if (len(disc[0][3]) == 0):
    print("A disciplina não possui professores no momento.")
  else:
    print("Professores da disciplina: ")
    for each in disc[0][3]:
      print((disc[0][3])[1])
      print()


def lista_alunos():
  aux = 0
  while True:
    cod_disc = int(
      input("Insira o código da disciplina que deseja listar os alunos: "))
    for disciplina in disciplinas:
      if (cod_disc == disciplina[0]):
        aux = 1
        break
      else:
        continue
    if (aux == 1):
      disc = disciplina
      break
    else:
      print("Disciplina não cadastrada! Tente novamente!")

  if (len(disc[0][4]) == 0):
    print("A disciplina não possui professores no momento.")
  else:
    print("Alunos da disciplina: ")
    for each in disc[0][4]:
      print((disc[0][4])[1])
      print()


def inserir_notas(notas):
  i = 0
  while i < 3:
    while True:
      nota = float(input(f"Digite a nota {i+1} do aluno: "))
      if (nota < 0 or nota > 10):
        print("Insira uma nota válida!")
      else:
        notas.append(nota)
        i += 1
        break


def pesquisar_aluno(matric, alunos):
  for aluno in alunos:
    if (matric == aluno[0]):
      return aluno
  return None


print('''--- Mini Controle Acadêmico ---
        1. Cadastrar disciplina
        2. Pesquisar disciplina
        3. Listar disciplinas cadastradas
        4. Cadastrar professor em disciplina
        5. Matricular aluno em disciplina
        6. Lançar notas do aluno em uma disciplina
        7. Listar alunos de uma disciplina
        8. Listar notas dos alunos de uma disciplina
        9. Sair''')

while True:
  escolha = int(input("Insira uma opção do menu acima: "))

  if (escolha == 1):
    cadastro_de_disciplina()
    print()

  elif (escolha == 2):
    disciplina = pesquisar_disciplina()
    if (disciplina == None):
      print("Disciplina não cadastrada. Tente novamente!")
    else:
      print("Disciplina: " + disciplina[0][1])

  elif (escolha == 3):
    lista_disciplinas()
    print()

  elif (escolha == 4):
    if (len(disciplinas) == 0):
      print("Não existem disciplinas cadastradas nesse momento!")
    else:
      cadastra_professor()
      print()

  elif (escolha == 5):
    if (len(disciplinas) == 0):
      print("Não existem disciplinas cadastradas nesse momento!")
    else:
      cadastra_aluno()
      print()

  elif (escolha == 6):
    if (len(disciplinas) == 0):
      print("Não existem disciplinas cadastradas nesse momento!")
    else:
      while True:
        print("Escolha uma disciplina em que deseja lançar as notas do aluno:")
        disciplina = pesquisar_disciplina()
        if (disciplina == None):
          print("Disciplina não encontrada. Por favor, tente novamente!")
        else:
          break

      while True:
        matricula = input(
          "Insira a matrícula do aluno que deseja inserir as notas: ")
        if (pesquisar_aluno(matricula, disciplina[0][4]) == None):
          print("Aluno não encontrado. Por favor tente novamente!")
        else:
          inserir_notas((pesquisar_aluno(matricula, disciplina[0][4]))[3])
          print()
          break

  elif (escolha == 7):
    if (len(disciplinas) == 0):
      print("Não existem disciplinas cadastradas no momento!")
    else:
      while True:
        disciplina = pesquisar_disciplina()
        if (disciplina == None):
          print("Disciplina não encontrada. Por favor, tente novamente!")
        else:
          break
      if (len(disciplina[0][4]) == 0):
        print("Não existem alunos matriculados ainda.")
      else:
        print("Alunos cadastrados na disciplina: ")
        for aluno in disciplina[0][4]:
          print(f"Matricula: {aluno[0]}, Aluno(a): {aluno[1]}")
          print()

  elif (escolha == 8):
    if (len(disciplinas) == 0):
      print("Não existem disciplinas cadastradas no momento!")
    else:
      while True:
        disciplina = pesquisar_disciplina()
        if (disciplina == None):
          print("Disciplina não encontrada. Por favor, tente novamente!")
        else:
          break
      if (len(disciplina[0][4]) == 0):
        print("Não há alunos cadastrados na disciplina no momento.")
      else:
        for aluno in disciplina[0][4]:
          if (len(aluno[3]) == 0):
            print(f"O aluno {aluno[1]} ainda não possui notas cadastradas.")
          else:
            print(f"Aluno: {aluno[1]} , Matrícula: {aluno[0]} , Notas: ",
                  end="")
            soma = 0.0
            notas = 0
            for nota in aluno[3]:
              soma += float(nota)
              notas += 1
              print(f"{nota}, ", end="")
            media = soma / notas
            print(f"Média das notas: {media:.2f}")
            print()

  elif (escolha == 9):
    print("Execução encerrada.")
    break
