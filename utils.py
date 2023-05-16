from models import Pessoas


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


if __name__ == '__main__':
    # insere_pessoas()
    # consulta_pessoas()
    # altera_pessoa()
    excluir_pessoa()
