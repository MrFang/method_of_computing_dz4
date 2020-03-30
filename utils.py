def readMatrixFromFile(filename):
    with open(filename, 'r') as f:
        s = f.read();
    a = s.split('\n');
    for idx, val in enumerate(a):
        a[idx] = val.split(" ")      
    
    a=[[float(elem) for elem in row]for row in a]

    return a