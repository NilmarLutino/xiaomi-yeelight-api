import socket

def discover_yeelight_bulbs():
    msg = "M-SEARCH * HTTP/1.1\r\n" \
          "HOST: 239.255.255.250:1982\r\n" \
          "MAN: \"ssdp:discover\"\r\n" \
          "ST: wifi_bulb\r\n"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(msg.encode('utf-8'), ('239.255.255.250', 1982))
    sock.settimeout(2)

    bulbs = []
    try:
        while True:
            data, addr = sock.recvfrom(65507)
            bulbs.append(data.decode('utf-8'))
    except socket.timeout:
        pass
    return bulbs

bulbs = discover_yeelight_bulbs()
if bulbs:
    for bulb in bulbs:
        print("Dispositivo encontrado:")
        print(bulb)
else:
    print("No se encontraron focos Yeelight en la red. Asegúrate de que el foco esté encendido y que el Modo LAN esté habilitado.")
