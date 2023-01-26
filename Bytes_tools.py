
def stringToBinary(string, encoding = 'utf-8'):
    """
    Return a object to binary
    """
    return ' '.join(format(x, 'b') for x in bytearray(string, encoding))
    
def bytesToBinary(BytesValue, encoding = 'utf-8'):
    """
    Return a bytes object to binary
    """
    return ' '.join(format(c, 'b') for c in BytesValue)

def bytescutting(BytesValue, indexCutting):
    """
    Return a list of bytes converting to string following a list of index
    
    indexCutting doesn't start with 0
    
    """
    indexCutting = [0] + indexCutting
    valToBeCut = ' '.join(format(c, 'b') for c in BytesValue)
    listToBeReturned = [ valToBeCut[indexCutting[i]: indexCutting[i+1]] for i in range(len(indexCutting)-1)] + [valToBeCut[indexCutting[-1]:]]
    return listToBeReturned

    

