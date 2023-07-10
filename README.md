# ESP32 micropython
[ESP32 CAM](./static/ESP32CAM.md)
![board](static/ESP32-38pin.png)
[Micropython Documentation](https://docs.micropython.org/en/latest/index.html)
## **ESPTOOL**
[ESPTOOL Documentation](https://docs.espressif.com/projects/esptool/en/latest/esp32/index.html)
### installation
```bash
pip3 install esptool
```
### Erase flash
```bash
#For windows change the port: COM4 --> /dev/ttyUSB0  
esptool --port COM4 erase_flash
```
### Deploy new firmware
```bash
#For Linux change the port: COM4 --> /dev/ttyUSB0  
esptool --chip esp32 --port COM4 write_flash -z 0x1000 esp32-idf3-20210202-v1.14.bin
```
## **AMPY**
[AMPY Documentation](https://pypi.org/project/adafruit-ampy/)
### install ampy
```bash
pip3 install adafruit-ampy
```
### Options
```bash
-p, --port PORT  Name of serial port for connected board.  [required]  
-b, --baud BAUD  Baud rate for the serial connection. (default 115200)  
-d, --delay DELAY Delay in seconds before entering RAW MODE (default 0)  
--help           Show this message and exit.
--no-output Do not show the output, do not enter to REPL
```
### Configuration
For convenience you can set an **AMPY_PORT** environment variable which will be used if the port parameter is not specified.
```bash
#For windows  
set AMPY_PORT=COM4  
ampy ls  
#For linux  
export AMPY_PORT=/dev/tty.SLAB_USBtoUART  
ampy ls
```
Similarly, you can set **AMPY_BAUD** and **AMPY_DELAY** to control your baud rate and the delay before entering RAW MODE.  
- AMPY_BAUD as default is 115200
- AMPY_DELAY as default is 0

### Commands
```bash
ampy ls #list content
ampy reset #perform a soft reset/reboot
ampy mkdir #create a directory on the board
ampy rmdir #forcefully remove a folder and its children on the board
ampy rm file.py #remove a file from the board
ampy run file.py #run a script
ampy get file.py #retrieve a file
ampy put file.py #put a file or folder and its content
ampy put test.py /main.py #copy the content from test.py to main.py
```
## USE
1. Set the port `set AMPY_PORT=COM4`
2. Reset the board `ampy --port COM4 reset`
3. List the files on the board `ampy ls`
4. Upload your file with a specific name (for testing) or with main name for being executed as default
```bash
#for testing
ampy put file.py
#for being executed constantly
ampy put main.py
```
5. Execute the file `ampy run file.py` or `ampy run main.py`

## Serial Connection
For linux:
```bash
screen /dev/tty.board_name 115200
```
To exit, press `Ctrl-a` then `k` then `y` or `Ctrl-a` then typing `:quit`

## Pymakr
- Install [nodejs](https://nodejs.org).
- Install [PYMAKR](https://marketplace.visualstudio.com/items?itemName=pycom.Pymakr) on VScode.
- Create a project(where three files will be created `main.py`, `boot.py` and `pymakr.conf`).
- Inside `main.py` put the code.
- To run the code in the device:
  * Connect the device and select `connect device`.
  * Press `Sync project to device`.
  * After the upload finish, press the option `Hard reset the device` to execute the script.
- To run the REPL, press `Create terminal`.
- To see the files inside the device, press `Open device in file explorer`.

## PlatformIO
- install [python](https://python.org/download)
- install [PlatformIO](https://marketplace.visualstudio.com/publishers/platformio)
- create a new project
- select the board `DOIT ESP32 DEVKIT V1`
- a folder will be created
- put your code inside `src/main.cpp`
- edit `platformio.ini`, specify the baudrate `monitor_speed = 115200`
