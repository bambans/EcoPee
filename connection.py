from network import WLAN, STA_IF, AP_IF, AUTH_WPA_WPA2_PSK
try:
    from usocket import socket, AF_INET, SOCK_STREAM
except:
    from socket import socket, AF_INET, SOCK_STREAM

def wifi_connector(SSID, PASSWORD):
    station = WLAN(STA_IF)
    station.active(True)
    station.connect(SSID, PASSWORD)
    while station.isconnected() == False:
        pass
    return station

def wifi_deactivator(STATION):
    STATION.active(False)

def ap_connector(SSID, PASSWORD):
    ap = WLAN(AP_IF)
    ap.active(True)
    ap.config(essid = SSID, authmode = AUTH_WPA_WPA2_PSK, password = PASSWORD)
    return ap

def ap_deactivator(AP):
    AP.active(False)

def socket_connector(port, listen):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', port))
    s.listen(listen)
    return s

def response_sender(conn, response, mime_type):
    conn.send('HTTP/1.1 200 OK\n')
    conn.send(f'Content-Type: {mime_type}\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)

def close_connection(conn):
    conn.close()

