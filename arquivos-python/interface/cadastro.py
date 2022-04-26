from PySimpleGUI import PySimpleGUI as sg

# Criação do Layout
sg.theme('Reddit')
layout = [
    [sg.Text('USUÁRIO:'), sg.Input(key='usuario', size=(30, 1))],
    [sg.Text('SENHA:   '), sg.Input(key='senha', password_char='*', size=(30, 1))],
    [sg.Checkbox('Salvar login?')],
    [sg.Button('Entrar')]
]

# Criação da janela
janela = sg.Window('Tela de Login', layout)

# Ler o processo
while True: 
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Rick' and valores['senha'] == '123456':
            print('Login efetuado.')      