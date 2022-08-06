def leArquivo(path):
    
    A = open(path, 'r')
    lista_A = []
    
    for i in A:
        i = i.rstrip()
        lista_A.append(i)
        
    if lista_A[0][-1] == 'F': # Verifica se há Backup.parm. 
        return 'Impossível'
