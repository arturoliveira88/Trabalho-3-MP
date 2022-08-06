from backup import leArquivo

# Verifica se há Backup.parm -----------------------------------------
def test_1():
    entrada = leArquivo('./Testes/T1.txt')
    saida = 'Impossível'
    assert entrada == saida

# Copia o arquivo do presente no HD para o Pen-drive -----------------
def test_2():
    entrada = leArquivo('./Testes/T2.txt')
    saida = 'Copia de HD para Pen-drive'
    assert entrada == saida

# Copia o arquivo do presente no HD para o Pen-drive, considerando que
# o arquivo já presente no Pen-drive é mais antigo (data menor) 
def test_3():
    entrada = leArquivo('./Testes/T3.txt')
    saida = 'Copia de HD para Pen-drive'
    assert entrada == saida