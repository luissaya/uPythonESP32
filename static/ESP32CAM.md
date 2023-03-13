# ESP32CAM

![ESP32CAM](./ESP32-CAM-pinout.png)

## Internal Pin Connect
**Camera connection**
|---CAM---|--ESP32--|
|---------|---------|
|---D0----|--GPIO5--|
|---D1----|--GPIO18-|
|---D2----|--GPIO19-|
|---D3----|--GPIO21-|
|---D4----|--GPIO36-|
|---D5----|--GPIO39-|
|---D6----|--GPIO34-|
|---D7----|--GPIO35-|
|--XCLK---|--GPIO0--|
|--VCLK---|--GPIO22-|
|--VSYNC--|--GPIO25-|
|--HREF---|--GPIO23-|
|---SDA---|--GPIO26-|
|---SCL---|--GPIO27-|
|POWER PIN|--GPIO32-|

**SD connection**
|------CAM-------|--ESP32---|
|----------------|----------|
|------CLK-------|--GPIO14--|
|------CMD-------|--GPIO15--|
|-----DATA0------|--GPIO2---|
|DATA1/Flash Lamp|--GPIO4---|
|-----DATA2------|--GPIO12--|
|-----DATA3------|--GPIO13--|

**LEDs**
|------LED-------|--ESP32---|
|----------------|----------|
|---ONBOARD LED--|--GPIO33--|
|----FLASH LED---|--GPIO4---|

Note: The onboard LED has inverse logic