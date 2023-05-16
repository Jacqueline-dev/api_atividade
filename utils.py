from models import Pessoas, Usuarios


# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Bruno', idade=29)
    print(pessoa)
    pessoa.save()


# Realiza consulta na tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='Bruno').first()
    print(pessoa.idade)
    print(pessoas)


# Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Bruno').first()
    pessoa.idade = 21
    pessoa.save()


# Exclui dados na tabela pessoa
def excluir_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Bruno').first()
    pessoa.delete()


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    insere_usuario('Jacque', '1234')
    insere_usuario('Bruno', '4321')
    consulta_todos_usuarios()
    # insere_pessoas()
    # consulta_pessoas()
    # altera_pessoa()
    # excluir_pessoa()
