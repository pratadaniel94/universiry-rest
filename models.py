import sqlite3

con = sqlite3.connect('apirest.db')
cur = con.cursor()

cur.execute("create table alunos (id char(3) primary key, nome char(50) not null)")
cur.execute("create table coordenadores (id char(3) primary key, nome char(50) not null)")
cur.execute("create table professores (id char(3) primary key, nome char(50) not null, matricula char(7))")
cur.execute("create table cursos (id char(3) primary key, nome char(50) not null)")
cur.execute("create table disciplinas (id char(3) primary key, nome TEXT not null, carga_horaria char(3), data TEXT, id_coordenador char(3), plano_ensino char(1), status char(1), FOREIGN KEY(id_coordenador) REFERENCES coordenadores(id))")
cur.execute("create table disciplinas_ofertadas (id char(3) primary key, ano char(4), id_disciplina char(3), id_professor char(3), semestre char(2), turma char(1),FOREIGN KEY(id_disciplina) REFERENCES disciplinas(id),FOREIGN KEY(id_professor) REFERENCES professores(id))")
cur.execute("create table solicitacoes_matricula (id char(3) primary key, id_aluno char(3), id_disciplina_ofertada char(3), dt_solicitacao TEXT, id_coordenador char(3), status char(1), FOREIGN KEY (id_aluno) REFERENCES alunos(id), FOREIGN KEY (id_disciplina_ofertada) REFERENCES disciplinas_ofertadas(id), FOREIGN KEY (id_coordenador) REFERENCES coordenadores(id))")
con.commit()
cur.close()
con.close()

