# Connecting ESP32 to Tencent Cloud by MQTT

## Introduction

+ **What does this project do?**

  This project connects an ESP32 board to Tencent cloud by MQTT protocol, and publishes a topic which shows the value of a on-board Touch Pad (Capacitive Touch module).

  Also, it receives from the cloud and set-high or set-low GPIO0 accordingly.

+ **What do I need to get this project running?**

  See **1. Preparation**

+ **How should I do to get this project running?**

  See **2. Create a Product on Tencent Cloud** and **3. Connect ESP32 to Tencent Cloud**

## 1. Preparation

### 1.1 Hardware

+ **The Board**

  The board I use called ESP-32F, which is a never-heard-of version of ESP32. It has a RGB light module which is soldered incorrectly (never gonna light up), and a speaker module which speaks when I try to light the RGB module up, and so many other shits. By the way, 1-starred on its TaoBao Page of course.

  But it has two touch pads. Although their pin number don't comply with the schematic, they work smoothly thank god.

<img src=".\md_pics\ESP32F.jpg" alt="ESP32F" style="zoom:15%;" />

### 1.2 Software

+ **MicroPython**: http://docs.micropython.org/en/latest/esp32/tutorial/intro.html#esp32-intro
+ **Thonny**: https://thonny.org/

## 2. Create a Product on Tencent Cloud

+ **Enter Tencent Cloud**

  ![TC-Entry](.\md_pics\TC-Entry.png)

+ **Click '立即使用'**, after which you need a scan login

  ![TC-Click](F:\Leisure_Projects\ESP32-TencentCloud\md_pics\TC-Click.png)

+ After logging in, you should see a page like this, **click '创建产品'**

  ![TC-Create](.\md_pics\TC-Create.png)

+ **Set up your product like this**

  <img src=".\md_pics\TC-PSetup.png" alt="TC-PSetup" style="zoom: 80%;" />

+ **Click Manage for the product you just created**

  ![TC-MClick](.\md_pics\TC-MClick.png)

+ **Go to '设备列表' and click '添加新设备'**

  ![TC-GNC](.\md_pics\TC-GNC.png)

  ![TC-CDevice](F:\Leisure_Projects\ESP32-TencentCloud\md_pics\TC-CDevice.png)

  ![TC-MDevice](.\md_pics\TC-MDevice.png)

+ **The information you need for now is just:**

  ![TC-Dinfo](F:\Leisure_Projects\ESP32-TencentCloud\md_pics\TC-Dinfo.png)

  ![TC-PID](.\md_pics\TC-PID.png)

  ![TC-Alist](.\md_pics\TC-Alist.png)

  `Product ID` & `Client ID` & `MQTT Username` & `MQTT Password` & `Topic`

## 3. Connect ESP32 to Tencent Cloud

+ Put `main.py` and `simple.py` to the board through Thonny.

+ Modify `main.py`, fill in the information (`Product ID` & `Client ID` & `MQTT Username` & `MQTT Password` & `Topic`)  you just got from Tencent Cloud.

+ Run `main.py` on board through Thonny.

+ If everything goes well, you could observe your data on Tencent Cloud:

  ![TC-Result](.\md_pics\TC-Result.png)

# 4. Reference

This project is just a modified version of a blog on the 01Studio (https://www.01studio.cc/) forum:

https://bbs.01studio.cc/thread/28

Thanks to Jackey.