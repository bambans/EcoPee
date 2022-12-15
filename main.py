print('Main.py...')

from network import WLAN, STA_IF
from connection import socket_connector, response_sender, close_connection, wifi_connector, ap_connector, ap_deactivator
from telegramBot import getUserData, sendToTelegram
from machine import reset, Pin, ADC
from time import sleep

try:
    from json import dumps, loads
except:
    from ujson import dumps, loads

try:
    f = open('config.json', 'r')
    e = True
    f.close()
except:
    e = False

if(e):
    print('Config file found...')
    data_set = ''
    with open('config.json', 'r') as load:
        print('Loading config file...')
        data_set = loads(load.read())
        load.close()

    print('Config file loaded. Displaying data:')
    print(data_set)

    print('Decoding data...')
    for data in data_set:
        data_set[data] = str(data_set[data], 'UTF-8')
    print('Data decoded. Displaying data:')
    data = data_set
    print(data)

    print('Connecting to wifi...')
    wifi = wifi_connector(data['wifi_name'], data['wifi_pass'])

    print('Wifi connected. Displaying data:')
    print(wifi.ifconfig())

    print('Connecting to telegram...')

    print('Telegram connected. Getting user chatID...')
    chatID = getUserData(data['mom_telegram_id'])
    print(f'ChatID: {chatID}')

    print('ChatID received. Sending messages...')
    print('Test: turning on EcoPee message...')
    if sendToTelegram(chatID, f"Olá {data['mom_name']}, seu EcoPee já está ligado!"):
        print('Message sent!')
    else:
        print('Error sending message.')
    
    print('Test: warning EcoPee message...')
    if sendToTelegram(chatID, f"Quando o(a) {data['baby_name']} urinar você será avisado(a)!"):
        print('Message sent!')
    else:
        print('Error sending message.')

    print('Waiting true signal from sensor...')
    pin = ADC(Pin(34))
    pin.atten(ADC.ATTN_11DB)
    while True:
        test = pin.read()
        print(f'Pin value read: {test}')
        if test > 1000:
            print('True signal received. Sending message...')
            if sendToTelegram(chatID, f"Olá {data['mom_name']}. O(a) {data['baby_name']} urinou!"):
                print('Message sent!')
            else:
                print('Error sending message.')
        sleep(300)
else:
    print('Config file not found...')

    print('Creating access point...')
    ap = ap_connector('EcoPee', 'novousuario')

    print('Access point created. Displaying data:')
    print(ap.ifconfig())

    print('Creating socket...')
    s = socket_connector(80, 5)

    print('Socket created. Waiting for connections...')
    while True:
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))

        request = conn.recv(1024)
        request = str(request, 'UTF-8')

        print('Content = %s' % request)

        if request.find('GET / HTTP/1.1') != -1 or request.find('GET /index.html HTTP/1.1') != -1:
            print('Sending index.html...')
            with open('index.html',' r') as index:
                response = index.read()
                response_sender(conn, response, 'text/html')
                index.close()

        if request.find('GET /wifi_scan HTTP/1.1') != -1:
            print('Scanning wifi...')
            station = WLAN(STA_IF)
            station.active(True)
            scanned_networks = station.scan()
            station.active(False)
            networks = []
            for sn in scanned_networks:
                networks.append(sn[0].decode('UTF-8'))
            response = dumps(networks)
            response_sender(conn, response, 'application/json')

        if request.find('POST /config HTTP/1.1') != -1:
            print('Saving config file...')
            with open('config.json', 'w') as config:
                config.write(str(request.split('\r\n')[12]))
                config.close()

        if request.find('GET /exit.html HTTP/1.1') != -1:
            print('Sending exit.html...')
            with open('exit.html',' r') as exit:
                response = exit.read()
                response_sender(conn, response, 'text/html')
                exit.close()

        if request.find('GET /test_config HTTP/1.1') != -1:
            print('Testing config file...')
            try:
                f = open('config.json')
                e = True
                f.close()
            except:
                e = False

            if(e):
                print('Config file found. Sending True...')
            else:
                print('Config file not found. Sending False...')

            response_sender(conn, dumps(e), 'application/json')
        
        if request.find('GET /reset HTTP/1.1') != -1:
            print('Resetting...')
            ap_deactivator(ap)
            reset()
        
        print('Closing connection...')
        close_connection(conn)
