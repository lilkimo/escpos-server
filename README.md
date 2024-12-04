# PYTHON ESC/POS SERVER
HTTP API built on top of [python-escpos](https://github.com/python-escpos/python-escpos) and [FastAPI](https://github.com/fastapi/fastapi) designed to run on Windows. No extra hardware required. No extra software required. No Zadig, WinUSB, `libudev`, `libusb` or `pywin32` required.

# HOW TO USE
```
escpos-server> pip install fastapi[standard]>=0.115.5
escpos-server> pip install python-escpos[all]>=3.1
```
```
escpos-server> fastapi dev --port 9130
```
Then you can access it via the following URL: http://localhost:9130/docs

# ADDITIONAL CONSIDERATIONS
To use the USB and Bluetooth interfaces the printer must be added to Windows. This typically happens automatically after plugging your device or installing its drivers. [This article](https://support.microsoft.com/en-us/windows/add-a-printer-or-scanner-in-windows-14d9a442-0bcb-e11c-7a6c-63f00efae79f) might be helpful.

Next you have to [share your printer](https://support.microsoft.com/en-us/windows/share-your-network-printer-c9a152b5-59f3-b6f3-c99f-f39e5bf664c3#:~:text=Share%20your%20printer%20using%20Control%20Panel&text=Under%20Hardware%20and%20Sound%2C%20select,tab%2C%20select%20Share%20this%20printer.) and give it a **Share name**.

The Serial Port interface is not supported (unless you manage to add the printer to Windows).

# HOW TO PRINT
Commands must be sent via a POST request to the API (see [endpoints](#ENDPOINTS)). The *body* must have the following structure:
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
\* Supported commands: `'image', 'qr', 'barcode', 'text', 'textln', 'ln', 'block_text', 'software_columns', 'cut', 'buzzer'`

For more information about the commands/methods and their arguments, see [python-escpos docs](https://python-escpos.readthedocs.io/en/latest/user/methods.html).

## ENDPOINTS
There are 2 endpoints:
### `/print/network?ip=IP&port=PORT`
Works for printers connected to your LAN network via Ethernet or WiFi.
### `/print/driver?shareName=SHARENAME`
Works for printers added to Windows, typically via USB or Bluetooth (see [Additional Considerations](#ADDITIONAL-CONSIDERATIONS)).
