from backup import leArquivo

def test_1():
    entrada = leArquivo('./Testes/T1.txt')
    saida = 'Impossível'
    assert entrada == saida
    