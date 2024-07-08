# Simulador de Caché Multinivel

Este programa simula un sistema de caché multinivel. Está diseñado para ser altamente parametrizable, permitiendo al usuario especificar las características de los niveles de caché mediante argumentos de línea de comandos.

## Requisitos

- Python 3.x

## Configuración e Instalación

Para ejecutar este programa, asegúrate de tener Python instalado en tu sistema. Clone este repositorio por medio del comando:

```git clone https://github.com/Mrfahrenheit25/IE0521_Tarea4_Cache```

y diríjase al directorio `parte_II`.

## Uso

El simulador se ejecuta desde la línea de comandos. A continuación se detallan los argumentos que se deben proporcionar para configurar los niveles de caché:

### Argumentos

- `--l1_s <tamaño>`: Capacidad del caché L1 en kB. Debe ser una potencia de 2.
- `--l1_a <asociatividad>`: Asociatividad del caché L1. Debe ser una potencia de 2.
- `--l2`: Incluir este flag si se va a simular el caché L2.
- `--l3`: Incluir este flag si se va a simular el caché L3.
- `--l2_s <tamaño>`, `--l2_a <asociatividad>`, `--l3_s <tamaño>`, `--l3_a <asociatividad>`: Capacidad y asociatividad para los cachés L2 y L3, definidos de la misma manera que para L1.
- `-b <tamaño_bloque>`: Tamaño del bloque en bytes, debe ser una potencia de 2.
- `-t <trace>`: Trace con el cual se va a realizar la simulación.

### Ejemplos de Ejecución

Para simular un caché con un L1 de 8kB, 4-way set associative, bloques de 16 bytes, con el trace 400.perlbench-41B:

```bash
python cache_sim.py --l1_s 8 --l1_a 4 -b 16 -t 400.perlbench-41B.trace.txt