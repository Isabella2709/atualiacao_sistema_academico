estudantes_lista = [
    {"codigo": 4572,"nome": "luana", "cpf": "966541531"},
    {"codigo": 4578,"nome": "joão", "cpf": "458925318"},
    {"codigo": 4574,"nome": "lucas", "cpf": "21441531"},

                        ]


disciplinas_lista = [
    {"nome": "comunicacao aplicada", "professor": "maria", "codigo": 8965214},
    {"nome": "pensamente computacional", "professor": "carlos", "codigo": 5698742},
    {"nome": "emprendedorismo e inovacao", "professor": "catia", "codigo": 865231}

                         ]



print("Bem vindo ao sistema academico:")
print("================================")

operacao = str(input("Deseja começar a fazer operações? (S - Fazer operações / N - para sair): "))
operacao = operacao.upper()

if(operacao != "N" and operacao != "S"):
  print("Opção invalida")
  operacao = str(input("Deseja começar a fazer operações? (S - Fazer operações / N - para sair): "))
  operacao = operacao.upper()

operacao = operacao.upper()


while(operacao == "S"):

  escolha_menu = int(input("Bem vindo ao menu principal, por favor escolha a opção desejada: \n 1. Estudantes \n 2. Disciplinas \n 3. Professores \n 4. Turmas \n 5. Matriculas \n 6. Sair \n"))

  if(escolha_menu == 1):
   escolha_pergunta = int(input("====== [ESTUDANTES] MENU DE OPERAÇÕES ====== \n 1. Incluir \n 2. Listar \n 3. Atualizar \n 4. Excluir \n 5. Voltar ao menu inicial"))
   if(escolha_pergunta == 1):

     codigo_estudante = str(input("Digite o codigo de 4 digitos do estudante: "))
     nome_estudante = str(input("Digite o nome do estudante que voce deseja inserir: "))
     cpf_estudante = str(input("Digite o cpf de 9 digitos do estudante "))
     estudantes_lista.append({"codigo": codigo_estudante, "nome": nome_estudante, "cpf": cpf_estudante})

     print("Estudante adicionado com sucesso")
   elif(escolha_pergunta == 2):

    for estudante in estudantes_lista:
                print(estudante)

   elif(escolha_pergunta == 3):
    atualizar_estudante = str(input("Digite qual o nome do estudante que você quer alterar: "))
    for estudante in estudantes_lista:
        if(estudante["nome"] == atualizar_estudante):
            nome_estudante = str(input("Digite o nome do estudante que você deseja inserir: "))
            cpf_estudante = str(input("Digite o CPF de 9 dígitos do estudante: "))
            estudante.update({"nome": nome_estudante, "cpf": cpf_estudante})
            print("Estudante atualizado com sucesso")
            break
    else:
        print("Estudante não encontrado.")

   elif(escolha_pergunta == 4):
    remover_estudante = int(input("Digite o código do estudante que você quer remover: "))
    nova_lista = [estudante for estudante in estudantes_lista if estudante["codigo"] != remover_estudante]
    if len(nova_lista) != len(estudantes_lista):
        estudantes_lista[:] = nova_lista
        print("Estudante removido com sucesso")
    else:
        print("Estudante não encontrado.")


   elif(escolha_pergunta == 5):
    print("Voltando ao menu inicial")



  elif(escolha_menu == 2):
   escolha_menu_disciplina = int(input("====== [DISCIPLINAS] MENU DE OPERAÇÕES ====== \n 1. Incluir \n 2. Listar \n 3. Atualizar \n 4. Excluir \n 5. Voltar ao menu inicial"))

   if escolha_menu_disciplina == 1:
    nome_disciplina = str(input("Digite o nome da disciplina que você quer adicionar: "))
    professor_disciplina = str(input("Digite o nome do professor dessa disciplina: "))
    codigo_disciplina = int(input("Digite o numero da disciplina: "))
    disciplinas_lista.append({"nome": nome_disciplina, "professor": professor_disciplina, "codigo_disciplina": codigo_disciplina})

   elif escolha_menu_disciplina == 2:
      for disc in disciplinas_lista:
        print(disc)

   elif(escolha_menu_disciplina == 3):
      atualizar_disciplina = input("Digite o nome da disciplina que você quer alterar: ")
      for disc in disciplinas_lista:
         if disc["nome"] == atualizar_disciplina:
             nome_disc_atualizacao = input("Digite o novo nome da disciplina: ")
             prof_disci_atualizacao = input("Digite o nome do professor atualizado: ")
             disc.update({"nome": nome_disc_atualizacao, "professor": prof_disci_atualizacao})
             print("Disciplina atualizada com sucesso")
             break

   elif escolha_menu_disciplina == 4:
    remover_disciplina = int(input("Digite o código da disciplina que você quer remover: "))
    disciplina_encontrada = False


    for disciplina in disciplinas_lista:
        if disciplina["codigo"] == remover_disciplina:
            disciplinas_lista.remove(disciplina)
            disciplina_encontrada = True
            print("Disciplina removida com sucesso")
            break

    if not disciplina_encontrada:
        print("Disciplina não encontrada")

  elif escolha_menu_disciplina == 5:
     print("Retornando ao menu inicial")






  elif(escolha_menu == 3):
   print("====== [PROFESSORES] MENU DE OPERAÇÕES ====== \n 1. Incluir \n 2. Listar \n 3. Atualizar \n 4. Excluir \n 5. Voltar ao menu inicial")
  elif(escolha_menu == 4):
   print("====== [TURMAS] MENU DE OPERAÇÕES ====== \n 1. Incluir \n 2. Listar \n 3. Atualizar \n 4. Excluir \n 5. Voltar ao menu inicial")
  elif(escolha_menu == 5):
   print("====== [MATRICULAS] MENU DE OPERAÇÕES ====== \n 1. Incluir \n 2. Listar \n 3. Atualizar \n 4. Excluir \n 5. Voltar ao menu inicial")
  elif(escolha_menu == 6):
   print("Obrigada por ultilizar nosso sistema, esperamos te ver em breve.")
  else:
   print("Opção invalida, por favor informe um numero valido, você sera direcionado para o menu inicial.")
  operacao = str(input("Deseja começar a fazer operações? (S - Fazer operações e N para sair): "))
  operacao = operacao.upper()

  if(operacao == "N"):
   print("Bem vindo de volta ao menu do sistema academico")
   operacao = str(input("Deseja começar a fazer operações novamente? (S - Fazer operações e N para sair): "))
   operacao = operacao.upper()
    
    print("===================================")o.upper()
