### Exercises developed in the Python with in the database connection SQLite3 

#### Step 1. Connection Database SQLite3

- Install DBeaver Community : [DBeaver installation](https://dbeaver.io/download/)
- Create new connection with SQLite3, file named 'banco' save in the same directory of file .py

#### Step 2. Run file .py

- In the terminal the your machine, write the command:
~~~bash
  git clone 'link-ssh-or-https'
~~~
- Access the paste created after execution of the previous command and write the next command to access [VSCode](https://code.visualstudio.com/download)
~~~bash
  code .
~~~

- In the terminal of VSCode write the command:
  
~~~bash
   python3 --name-file-.py
~~~
- Result:

~~~bash
---------------Listagem de Alunos-----------------
(1, 'Maria Antônia Silveira', 23, 'Engenharia')
(2, 'Ana Pereira', 34, 'Medicina Veterinária')
(3, 'Augusto Anselmo Ludwig', 19, 'Ciências Contábeis')
(4, 'Murilo Carlos Júnior Bento', 26, 'Engenharia')
(5, 'Maria Clara Willers', 27, 'Engenharia')


---------------Nome e Idade Alunos-----------------
('Maria Antônia Silveira', 23)
('Ana Pereira', 34)
('Murilo Carlos Júnior Bento', 26)
('Maria Clara Willers', 27)


---------------Alunos que cursam Engenharia-----------------
(1, 'Maria Antônia Silveira', 23, 'Engenharia')
(5, 'Maria Clara Willers', 27, 'Engenharia')
(4, 'Murilo Carlos Júnior Bento', 26, 'Engenharia')


Número Total de alunos: 5


---------------Clientes com idade superior a 30 anos-----------------
(1, 'José Caye', 70, 1000.34)
(2, 'Pietra Calmo', 67, 65000.45)
(3, 'Carla Santoro', 35, 30000)
(5, 'Marcela Ludwig Pretto', 45, 2500.2)


Saldo médio dos clientes:39,200.22


Saldo máximo:97,500.10 do cliente Pablo Luis Vister


Quantidade de clientes com saldo acima de R$1000,00: 5


---------------Nome cliente, produto e valor da compra-----------------
('Carla Santoro', 'Vestido vermelho tamanho único', 230.45)
('José Caye', 'Sapato Masculino social Pegada tamanho 40', 456.99)
('Marcela Ludwig Pretto', 'Bolsa Luis Vitton Preta Couro', 1450.34)
('Pablo Luis Vister', 'Carteira de Couro cor marrom', 378.6)
~~~
