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
    
# Nada é feito, pois os dois dispositivos já possuem o mesmo arquivo
# com a mesma data
def test_4():
    entrada = leArquivo('./Testes/T4.txt')
    saida = 'Faz nada'
    assert entrada == saida

# Ocorre erro pois a data do arquivo armazenada no Pen-drive não pode
# ser mais atual do que a do arquivo presente no HD
def test_5():
    entrada = leArquivo('./Testes/T5.txt')
    saida = 'Erro'
    assert entrada == saida
    
# Ocorre erro pois não há solicitação de backup do arquivo do HD para
# o Pen-drive
def test_6():
    entrada = leArquivo('./Testes/T6.txt')
    saida = 'Erro'
    assert entrada == saida
    
# Ocorre erro pois não há solicitação de backup e não é possível
# retaurar um arquivo mais atual que o anterior
def test_7():
    entrada = leArquivo('./Testes/T7.txt')
    saida = 'Erro'
    assert entrada == saida
        
        