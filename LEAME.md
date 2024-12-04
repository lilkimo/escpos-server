# PYTHON ESC/POS SERVER
HTTP API basada en [python-escpos](https://github.com/python-escpos/python-escpos). Sin hardware extra requerido, sin software extra requerido, no `libudev`, Zadig, WinUSB, `libusb`, `pywin32` requeridos.

# CÓMO USAR
```
escpos-server> pip install fastapi[standard]>=0.115.5
escpos-server> pip install python-escpos[all]>=3.1
```
```
escpos-server> fastapi dev --port 9130
```
Luego puede acceder a través de la siguiente URL http://localhost:9130/docs

# CONSIDERACIONES ADICIONALES
Para utilizar la interfaz USB y Bluetooth es necesario que tenga agregada la impresora en Windows, esto suele suceder de forma automática tras enchufar tu dispositivo o tras instalar sus drivers. [Este artículo](https://support.microsoft.com/en-us/windows/add-a-printer-or-scanner-in-windows-14d9a442-0bcb-e11c-7a6c-63f00efae79f) podría ser de ayuda.

El siguiente paso sería [compartir tu impresora](https://support.microsoft.com/en-us/windows/share-your-network-printer-c9a152b5-59f3-b6f3-c99f-f39e5bf664c3#:~:text=Share%20your%20printer%20using%20Control%20Panel&text=Under%20Hardware%20and%20Sound%2C%20select,tab%2C%20select%20Share%20this%20printer.) y darle un **Share name**.

La interfaz Puerto Serial no está soportada (A menos que logres agregar la impresora a Windows).

# CÓMO IMPRIMIR
Los comandos deben hacerse mediante una solicitud POST a la API (Véase [endpoints](#ENDPOINTS)), el *body* debe tener la siguiente estructura:
```
[
    {
        "command": "command",
        "args": [],
        "kwargs": {}
    },
    ...
]
```
\* Comandos soportados: `'image', 'qr', 'barcode', 'text', 'textln', 'ln', 'block_text', 'software_columns', 'cut', 'buzzer'`

Para más información de los comandos/métodos y sus argumentos véase [python-escpos](https://python-escpos.readthedocs.io/en/latest/user/methods.html).

## ENDPOINTS
La API cuenta con 2 endpoints:
### `/print/network?ip=IP&port=PORT`
Funciona para impresoras conectadas a la tu red LAN, por ethernet o wifi.
### `/print/driver?shareName=SHARENAME`
Funciona para impresoras agregadas a Windows, usualmente por USB o Bluetooth (Véase [Consideraciones Adicionales](#CONSIDERACIONES-ADICIONALES)).
