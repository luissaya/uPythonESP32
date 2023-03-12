# ESP32 micropython
![board](static/ESP32-38pin.png).
## **ESPTOOL**
## installation
pip install esptool
## Erase flash
```bash
#For windows change the port: COM4 --> /dev/ttyUSB0  
esptool --port COM4 erase_flash
```
## Deploy new firmware
```bash
#For Linux change the port: COM4 --> /dev/ttyUSB0  
esptool --chip esp32 --port COM4 write_flash -z 0x1000 esp32-idf3-20210202-v1.14.bin
```
## **AMPY**
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
```
## Configuration
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
ampy put file.py #put a file or folder and its content
ampy get file.py #retrieve a file
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