#!/usr/bin/python3
# Codigo utilizado para reconocimeinto de señales (Server)
# Equipo 3
# Noemi Carolina Guerra Montiel A00826944
# Maria Fernanda Hernandez Montes A01704918
# Mizael Beltran Romero A01114973
# Izac Saul Salazar Flores A01197392
# Junio 2022

# Librerias
import socket
import cv2, json
import numpy as np
import darknet as dn
from socketing import recv_variable_length, send_variable_length
from socketing import TCP_PORT

# Cargar los pesos y configuraciones de los datos
net = dn.load_net(b"cfg/ois.cfg", b"weights/ois_final.weights", 0)
meta = dn.load_meta(b"cfg/ois.data")

# Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', TCP_PORT))
s.listen(True)

while True:
    conn, addr = s.accept()
    try:
        while True:
            # Mandar imagen y realizar deteccion
            bytedata = recv_variable_length(conn)
            frame = np.frombuffer(bytedata, dtype='uint8')
            frame = cv2.imdecode(frame, 1)
            img = dn.cv_img_to_darknet_img(frame)
            r = dn.detect(net, meta, img)
            send_variable_length(conn, json.dumps(r).encode('utf-8'))
    except:
        print('Client connection closed')
        conn.close()
