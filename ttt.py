def init_matrix():
    Matrix = [[None,None,None]
              [None,None,None]
              [None,None,None]]
    return Matrix

def check_matrix_comp(arg:str,Matrix:list):
    matrix_comp = Matrix
    for i in arg:
        arg_int = int(i)
        matrix_comp = matrix_comp[arg_int]
    return matrix_comp



