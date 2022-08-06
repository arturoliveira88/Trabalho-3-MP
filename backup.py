def leArquivo(path):
    
    A = open(path, 'r')
    lista = []
    
    for i in A:
        i = i.rstrip()
        lista.append(i)
        
    # Verifica se há Backup.parm -----------------------------------------
    if lista[0][-1] == 'F': 
        return 'Impossível'
    
    # Copia o arquivo do presente no HD para o Pen-drive -----------------
    if lista[1][-1] == 'V' and lista[2][-1] == 'V' and lista[3][-1] == 'F':
        return 'Copia de HD para Pen-drive'
    
    # Copia o arquivo do presente no HD para o Pen-drive, considerando que
    # o arquivo já presente no Pen-drive é mais antigo (data menor)  
    if lista[1][-1] == 'V' and lista[2][-1] == 'V' and lista[3][-1] == 'V' and lista[4][-1] == 'V':
        return 'Copia de HD para Pen-drive'
    
    # Nada é feito, pois os dois dispositivos já possuem o mesmo arquivo
    # com a mesma data
    if lista[1][-1] == 'V' and lista[2][-1] == 'V' and lista[3][-1] == 'V' and lista[5][-1] == 'V':
        return 'Faz nada'
    
    # Ocorre erro pois a data do arquivo armazenada no Pen-drive não pode
    # ser mais atual do que a do arquivo presente no HD
    if lista[1][-1] == 'V' and lista[2][-1] == 'V' and lista[3][-1] == 'V' and lista[6][-1] == 'V':
        return 'Erro'
     
    # Ocorre erro pois não há solicitação de backup do arquivo do HD para
    # o Pen-drive
    if lista[1][-1] == 'F' and lista[2][-1] == 'V' and lista[3][-1] == 'F':
        return 'Erro'
    
    
    