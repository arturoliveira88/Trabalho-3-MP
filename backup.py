def leArquivo(path):
    
    """
    Função que lê e interpreta caracteristicas do arquivo
    
    Recebe:
        :path: String referente ao caminho do arquivo.
    
    Retorna:
        :: Mensagem em string especificando o fenômeno ocorrido.
    
    """

    
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
    
    # Ocorre erro pois não há solicitação de backup e não é possível
    # retaurar um arquivo mais atual que o anterior
    if lista[1][-1] == 'F' and lista[2][-1] == 'V' and lista[3][-1] == 'V' and lista[4][-1] == 'V':
        return 'Erro'
    
    # Nada é feito pois os arquivos presentes nos dois dispositivos têm
    # a mesma data e não há solicitação de backup
    if lista[1][-1] == 'F' and lista[2][-1] == 'V' and lista[3][-1] == 'V' and lista[5][-1] == 'V':
        return 'Faz nada'
    
    # É feita a retauração do arquivo do Pen-drive para o HD pois
    # seu arquivo é mais atual não há solicitção de backup  
    if lista[1][-1] == 'F' and lista[2][-1] == 'V' and lista[3][-1] == 'V' and lista[6][-1] == 'V':
        return 'Copia de Pen-drive para HD'
    
    # Ocorre erro pois o arquivo não está presente em nenhum dos
    # dispositivos e é solicitado o backup
    if lista[1][-1] == 'V' and lista[2][-1] == 'F' and lista[3][-1] == 'F':
        return 'Erro'
    
    # Nada é feito pois o arquivo a ser transferido por backup já está
    # armazenado no Pen-drive
    if lista[1][-1] == 'V' and lista[2][-1] == 'F' and lista[3][-1] == 'V':
        return 'Faz nada'
    
    # Ocorre erro pois há Backup.parm mas não solicitação de backup nem
    # arquivos a serem transferidos 
    if lista[1][-1] == 'F' and lista[2][-1] == 'F' and lista[3][-1] == 'F':
        return 'Erro'
    
    # Restaura arquivo presente no Pen-drive e ausente no HD
    if lista[1][-1] == 'F' and lista[2][-1] == 'F' and lista[3][-1] == 'V':
        return 'Copia de Pen-drive para HD'