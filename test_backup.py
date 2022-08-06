from backup import leArquivo

def test_1():
    entrada = leArquivo('./Testes/T1.txt')
    saida = 'Impossível'
    assert entrada == saida
    
def test_2():
    entrada = leArquivo('./Testes/T2.txt')
    saida = 'Copia de HD para Pen-drive'
    assert entrada == saida