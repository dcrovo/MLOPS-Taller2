![alt text](https://github.com/c4ttivo/MLOpsTaller1/blob/main/mlopstaller1/imgs/logo.png?raw=true)

# MLOps - Taller 4
## Autores
*    Daniel Crovo (dcrovo@javeriana.edu.co)
*    Carlos Trujillo (ca.trujillo@javeriana.edu.co)

## Profesor
*    Cristian Diaz (diaz.cristian@javeriana.edu.co)

## Docker Hub

Para la realización del taller fue necesario crear una cuenta en Docker Hub, con el objetivo de publicar la imagen del contenedor de inferencia del Proyecto 2. En la URL https://hub.docker.com/
se crea la cuenta y el repositorio, inicialmente privado y una vez se tengan los datos, desde la VM se ejecutan los siguientes comandos para subir la imagen.

### Creación tag
Inicialmente se debe crear un tag para la imagen con el siguiente comando:

```
# sudo docker tag mlops_p2_inference:latest dcrovo/mlops_taller4:inference
```

Donde mlops_p2_inference es el nombre de la imagen en el contenedor y latest es el tag por defecto. Mientras que dcrovo es el nombre del usuario en docker hub y mlops_taller4 el repositotio acompañado del tag inference.

### Publicar la imagen

Antes de publicar la imagen, es necesario loguearse desde la VM al docker hub, usando el siguiente comando:

```
# sudo docker login -u dcrovo
```

Se autentica con el password y una vez se encuentra logueado se procede a realizar al push con el siguiente comando.

```
# sudo docker push dcrovo/mlops_taller4:inference
```

Luego se debe cambiar la configuración para que la imagen quede publica y se debe acceder de tal forma que se vea:

https://hub.docker.com/r/dcrovo/mlops_taller4 </br>
<img src="https://github.com/dcrovo/MLOPS-Taller4/blob/main/img/docker-hub.png?raw=true" width="60%" height="60%" /> </br>


## Instrucciones
Clone el repositorio de git usando el siguiente comando en la consola de su sistema operativo:


```
# git clone https://github.com/dcrovo/MLOPS-Taller4.git
```

Una vez ejecutado el comando anterior aparece el folder MLOPS-Taller4. Luego es necesario ubicarse en el directorio de trabajo en el que se encuentra el archivo docker-compose.yml.


```
# cd MLOPS-Taller4/inference_test
```

Ahora es necesario construir los contenedores


```
# sudo docker-compose up
```
En este paso se descarga la imagen cargada previamente en docker hub de acuerdo con lo especificado en el archivo docker-compose.yml.

## Pruebas de carga
Ubiquese en el directorio

```
# cd MLOPS-Taller4/locust
```

Ahora es necesario construir los contenedores


```
# sudo docker-compose up
```

Con el contenedor arriba se accede a la consola de locust,

http://10.43.101.155:8089/ </br>
<img src="https://github.com/dcrovo/MLOPS-Taller4/blob/main/img/locust.png?raw=true" width="60%" height="60%" /> </br>

## Evidencia de pruebas

A continuación se observan imágenes de las pruebas realizadas.

<img src="https://github.com/dcrovo/MLOPS-Taller4/blob/main/img/locust-1.jpeg?raw=true" width="60%" height="60%" /> </br>
<img src="https://github.com/dcrovo/MLOPS-Taller4/blob/main/img/locust-2.jpeg?raw=true" width="60%" height="60%" /> </br>

