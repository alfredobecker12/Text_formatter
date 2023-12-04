def get_file_path():
    file_path = input("Olá, digite o caminho do arquivo que deseja formatar: ")
    file_name = input("Digite o nome do arquivo txt que deseja formatar: ")
    separator = input("Digite qual o separador o qual quebrar linha em seguida: ")

    file_name += '.txt'

    return file_path, file_name, separator
