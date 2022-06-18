# Reto Final Puzzlebot
<i>Implementación de Robótica inteligente</i>
#### Equipo 3:
#### Noemi Carolina Guerra Montiel A00826944 
#### Maria Fernanda Hernandez Montes A01704918 
#### Mizael Beltran Romero A01114973 
#### Izac Saul Salazar Flores A01197392

## Descripción del proyecto
Recorrido de una pista para un robot diferencial llamado "Puzzlebot".

## Tabla de Contenidos
* Seguimiento de linea 
* Visión de semaforos 
* Planeación de ruta 
* Detección de señales 

## Tecnología
* Sistema operativo Ubuntu 18.04
* Ros
* Python
* OpenCV
* Yolo

## Setup
Para su uso, se tiene el nodo precargado dentro de la Jetson Nano para mejorar el rendimiento y el tiempo de ejecución. La instrucción para empezar el nodo del archivo reto_final.py es:
```
rosrun puzzlebot reto_final.py
```

Para acceder al puzzlebot, se realiza una conexión ssh mediante la instrucción:
```
ssh puzzlebot@10.42.0.1
Contraseña: Puzzlebot72
```

De manera alterna, se pueden correr los programas directamente en la computadora con estos dos comandos:
```
export ROS_MASTER_URI=http://10.42.0.1:11311
export ROS_IP=10.42.0.24
```
Notese que la ip varía dependiendo de cada computadora.

Para inicializar el nodo de la cámara, se utiliza la siguiente instrucción dentro de la terminal del puzzlebot
```
roslaunch ros_deep_learning video_viewer.ros1.launch
```

Para obtener la imagen que está recibiendo la cámara se utiliza la instrucción:
```
rosrun rqt_image_view rqt_image_view /video_source/raw
```
