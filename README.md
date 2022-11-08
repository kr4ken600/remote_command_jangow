## REMOTE_COMMAND_JANGOW
RC AMBASSADIR, es un script programado en python diseñado especificamente para la maquina JANGOW: 1.0.1 de Vulnhub.
Realizando peticiones por GET al servidor, para poder realizar un Remote Command
***
## Instalacion
```
git clone https://github.com/kr4ken600/remote_command_jangow.git rcJangow
cd rcJangow
pip install -r requirements.txt
```
***
## Uso
Solo basta con agregar dos parametros, [HOST] y [COMMAND]:
### Ejemplo
```
python3 lfi_ambassador.py 10.0.2.8 'whoami'
```
* El [HOST] sera la ip de la maquina victima
* El [COMMAND] sera el comando que se desea ejecutar