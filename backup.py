def leArquivo(path):
    
    A = open(path, 'r')
    lista_A = []
    
    for i in A:
        i = i.rstrip()
        lista_A.append(i)
    '''    
    temBackup = False
    fazBackup = False
    arqEHD = False
    arqEPenDrive = False
    dataPen<HD = False
    dataPen==HD = False
    dataPen>HD = False
    '''    
        
    if lista_A[0][-1] == 'F': # Verifica se há Backup.parm. 
        return 'Impossível'
    
    if lista_A[1][-1] == 'V' and lista_A[2][-1] == 'V' and lista_A[3][-1] == 'F':
        return 'Copia de HD para Pen-drive'
    '''
    if lista_A[2][-1] == 'V':
        arqEHD = True
        
    if lista_A[3][-1] == 'V':
        arqEPenDrive = True
    
    if lista_A[4][-1] == 'V':
        dataPen<HD = True
    
    if lista_A[5][-1] == 'V':
        dataPen==HD = True
    
    if lista_A[6][-1] == 'V':
        dataPen>HD = True
        
    '''
leArquivo('./Testes/T2.txt')