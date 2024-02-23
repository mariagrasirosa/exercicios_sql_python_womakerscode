import sqlite3

conexao = sqlite3.connect('banco')

cursor = conexao.cursor()


#1. Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto)

cursor.execute('create table alunos(id int, nome varchar(255), idade int, curso varchar(255))')

#2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

cursor.execute('insert into alunos(id, nome,idade,curso) values(1,"Maria Antônia Silveira", 23, "Engenharia")')

cursor.execute('insert into alunos(id, nome,idade,curso) values(2,"Ana Pereira", 34, "Medicina Veterinária")')

cursor.execute('insert into alunos(id, nome,idade,curso) values(3,"Augusto Anselmo Ludwig", 19, "Ciências Contábeis")')

cursor.execute('insert into alunos(id, nome,idade,curso) values(4,"Murilo Carlos Júnior Bento", 26, "Engenharia")')

cursor.execute('insert into alunos(id, nome,idade,curso) values(5,"Maria Clara Willers", 27, "Engenharia")')

#3.a) Selecionar todos os registros da tabela "alunos"

alunos = cursor.execute('select * from alunos')
print("\n")
print("---------------Listagem de Alunos-----------------")
for aluno in alunos:
  print(aluno)
print("\n")

#3.b) Selecionar o nome e a idade dos alunos com mais de 20 anos.

alunos = cursor.execute('select nome, idade from alunos where idade > 20')
print("---------------Nome e Idade Alunos-----------------")
for aluno in alunos:
   print(aluno)
print("\n")
#3.c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética

alunos = cursor.execute('select * from alunos where curso = "Engenharia" order by nome asc')
print("---------------Alunos que cursam Engenharia-----------------")
for aluno in alunos:
   print(aluno)
print("\n")
#3.d)Contar o número total de alunos na tabela

qtde_alunos = cursor.execute('select count(id) qtde from alunos')
for qtde in qtde_alunos:
  print("Número Total de alunos:", qtde[0])
print("\n")
#4.a) Atualize a idade de um aluno específico na tabela
  
cursor.execute('update alunos set idade = 20 where id = 4')

#4. b) Remova um aluno pelo seu ID.

cursor.execute('delete from alunos where id = 5')


"""5. Criar uma Tabela e Inserir Dados:
- Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). 
- Insira alguns registros de clientes na tabela."""

#criação da tabela clientes
cursor.execute('create table clientes(id int primary key, nome varchar(255), idade int, saldo decimal(10))')

#inserção de dados na tabela clientes

cursor.execute('insert into clientes(id, nome,idade,saldo) values(1,"José Caye", 70, 1000.34)')

cursor.execute('insert into clientes(id, nome,idade,saldo) values(2,"Pietra Calmo", 67, 65000.45)')

cursor.execute('insert into clientes(id, nome,idade,saldo) values(3,"Carla Santoro", 35, 30000.00)')

cursor.execute('insert into clientes(id, nome,idade,saldo) values(4,"Pablo Luis Vister", 20, 97500.10)')

cursor.execute('insert into clientes(id, nome,idade,saldo) values(5,"Marcela Ludwig Pretto", 45, 2500.20)')

#6.a) Selecione o nome e a idade dos clientes com idade superior a 30 anos

clientes = cursor.execute('select * from clientes where idade > 30')
print("---------------Clientes com idade superior a 30 anos-----------------")
for cliente in clientes:
   print(cliente)
print("\n")
#6.b) Calcule o saldo médio dos clientes.

saldo_medio = cursor.execute('select avg(saldo) media from clientes')
for media in saldo_medio:
   print(f'Saldo médio dos clientes:{media[0]:,.2f}')
print("\n")
#6.c) Encontre o cliente com o saldo máximo.

saldo_max = cursor.execute('select nome, max(saldo) saldo_max from clientes')
for max_saldo in saldo_max:
   print(f'Saldo máximo:{max_saldo[1]:,.2f} ' + 'do cliente', max_saldo[0])
print("\n")
#6.d) Conte quantos clientes têm saldo acima de 1000.
   
qtde_cli = cursor.execute('select count(id) qtde from clientes where saldo > 1000.00')
for qtde in qtde_cli:
   print("Quantidade de clientes com saldo acima de R$1000,00:",qtde[0])
print("\n")
#7.a) Atualize o saldo de um cliente específico

cursor.execute('update clientes set saldo = 1000.03 where id = 4')

#7.b) Remova um cliente pelo seu ID

cursor.execute('delete from clientes where id = 2')

"""
8.
- Crie uma segunda tabela chamada "compras" com os campos: 
id(chave primária), cliente_id (chave estrangeira referenciando o id
da tabela "clientes"), produto (texto) e valor (real). 
- Insira algumas compras associadas a clientes existentes na tabela "clientes".
- Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra
"""

#criação da tabela compras
cursor.execute('create table compras(id int primary key, cliente_id int, produto varchar(255), valor decimal(10), foreign key (cliente_id) references clientes(id))')

#inserções na tabela compras
cursor.execute('insert into compras(id, cliente_id,produto,valor) values(1,3, "Vestido vermelho tamanho único", 230.45)')

cursor.execute('insert into compras(id, cliente_id,produto,valor) values(2,1, "Sapato Masculino social Pegada tamanho 40", 456.99)')

cursor.execute('insert into compras(id, cliente_id,produto,valor) values(3,4, "Carteira de Couro cor marrom", 378.60)')

cursor.execute('insert into compras(id, cliente_id,produto,valor) values(4,5, "Bolsa Luis Vitton Preta Couro", 1450.34)')

#consulta nome do cliente, o produto e o valor de cada compra

clientes = cursor.execute('select cli.nome, com.produto, com.valor from clientes cli, compras com where cli.id = com.cliente_id order by cli.nome asc')
print("---------------Nome cliente, produto e valor da compra-----------------")
for cliente in clientes:
   print(cliente)
print("\n")
conexao.commit()

conexao.close()

