# Tarea #4: Simulador de caché
## Parte I: Caché de un solo nivel

### Argumentos de línea de comandos
*  -s: tamaño de la cache en kiloBytes; número entero potencia de 2
*  -a: asociatividad; número entero potencia de 2
* -b: tamaño del bloque en Bytes; número entero potencia de 2
*  -r: política de reemplazo: _-r l_ elige "LRU" y _-r r_ elige "Aleatoria"
* -t: Elección de trace file



### Ejemplos de cómo correr, esto en la carpeta adecuada dónde se encuentran los archivos "cache_sim.py" y "cahe.py"
##### Para correr el trace 400.perlbench-41B.trace.txt con los argumentos de tamaño 128 kB, asociatividad de 16 ways, tamaño de bloque de 64B y política LRU.  Se hace lo siguiente:
* python3 cache_replacement.py -s 128 -a 16 -b 64 -r l -t 400.perlbench-41B.trace.txt
##### Para correr el trace 401.bzip2-226B.trace.txt con los argumentos de tamaño 128 kB, asociatividad de 16 ways, tamaño de bloque de 64B y política LRU.  Se hace lo siguiente:
* python3 cache_replacement.py -s 128 -a 16 -b 64 -r l -t 401.bzip2-226B.trace.txt
##### Para correr todos las pruebas se hace un script de bat, para ejecutarlo se debe de correr el siguiente comando en la misma carpeta dónde se encuentran los archivos "cache_sim.py" y "cache.py"
* .\scripts\todo.bat 
##### Es importante aclarar que se debe de modificar en los archivos .bat, la ruta dónde están los archivos, para cado uno de los usuarios probablemente es diferente 
