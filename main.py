
from turtle import back
from PySimpleGUI import PySimpleGUI as program
import requests
import json

# two windows
     
#layout
def info_window():
    program.theme('Dark')
    layout = [
        [program.Text('INFO'),program.Input(key='info', size=(20, 1))],
        [program.Button('check'), program.Button('continue')]
    ]

    return program.Window('info check', layout, finalize=True)

window1, window2 = info_window(), None


#event
while True:
    window, event, values = program.read_all_windows()
    checkValors = window1.read()
    content = checkValors
    
    
    
    if window == window1 and event == program.WIN_CLOSED:
        break
    
    if window == window1 and event == 'check':
        
         
                print(window1.read())
       
    def reader_window():
        program.theme('Dark')
        layout = [
            [program.Text('cep, street, state, district, lat, lng, city, ibge, ddd')],
            [program.Button('back'), program.Button('exit')]

        ]

        return program.Window('Reader', layout, finalize=True)


    if window == window1 and event == 'continue':
        window2 = reader_window()
        window1.hide()
    
    if window == window2 and event == 'back':
        window2.hide()
        window1.un_hide()


    #    if event == program.WIN_CLOSED:
#        break
#    elif event == 'check':
#       
#        if content.isdigit():
#            try:
#                int(content)
#                data = requests.get('https://cep.awesomeapi.com.br/json/{}'.format(content))
#                data = data.json()
#                cep = data['cep']
#                street = data['address_name']
#                state = data['state']
#                district = data['district']
#                lat = data['lat']
#                lng = data['lng']
#                city = data['city']
#                ibge = data['city_ibge']
#                ddd = data['ddd']
#                print(cep, street, state, district, lat, lng, city, ibge, ddd)
#                
#
#            except:
#                pass

