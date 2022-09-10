from PySimpleGUI import PySimpleGUI as program
import requests
#layout and window
#set theme
program.theme('Dark')
#set layout
layout = [
    [program.Text('INFO'),program.Input(key='info')],
    [program.Button('check')]
]

window = program.Window('info check', layout)

#events
while True:
    event, checkValors = window.read()
    content = checkValors['info']
    

    if event == program.WIN_CLOSED:
        break
    if event == 'check':
        try:
            int(content)
            data = requests.get('https://cep.awesomeapi.com.br/json/{}'.format(content))
            data = data.json()
            cep = data['cep']
            street = data['address_name']
            state = data['state']
            district = data['district']
            lat = data['lat']
            lng = data['lng']
            city = data['city']
            ibge = data['city_ibge']
            ddd = data['ddd']
            print(cep, street, state, district, lat, lng, city, ibge, ddd)
            window.hide()
    
        except:
           pass
    
     