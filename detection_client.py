#!/usr/bin/python3
# Codigo utilizado para reconocimeinto de señales (Cliente)
# Equipo 3
# Noemi Carolina Guerra Montiel A00826944
# Maria Fernanda Hernandez Montes A01704918
# Mizael Beltran Romero A01114973
# Izac Saul Salazar Flores A01197392
# Junio 2022

# Librerias
import socket, time
import cv2, json
import numpy as np
from socketing import recv_variable_length, send_variable_length
from socketing import TCP_PORT
from threading import Thread

TCP_IP = 'localhost'

# Socket
sock = socket.socket()
sock.connect((TCP_IP, TCP_PORT))

# Acceder a webcam
cap = cv2.VideoCapture(0)

c = 0
avg = 0

# Cambiar el tamaño de la imagen
def resize_img(frame):
  h = frame.shape[0]
  frame = frame[h//3:]
  fr = (frame.shape[0] // 2)
  frame = np.concatenate((frame[:,:fr], frame[:,-fr:]), axis=1)
  frame = cv2.resize(frame, (416, 416))
  return frame


# Mientras la webam esta abierta
while cap.isOpened():
  start = time.time()
  # Leer la imagen
  ret, frame = cap.read()
  if(not ret or frame is None):
    break

  # frame = resize_img(frame)
  encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
  # Obtener el resultado
  result, imgencode = cv2.imencode('.jpg', frame, encode_param)
  data = np.array(imgencode)
  data = data.tobytes()
  send_variable_length(sock, data)
  detection = recv_variable_length(sock).decode()
  # Labels
  detection = json.loads(detection)
  end = time.time()
  avg = (avg*c + (end - start))/(c + 1)
  c += 1
  if(len(detection) > 0):
    print(detection, avg)

sock.close()
