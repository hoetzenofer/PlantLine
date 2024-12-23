# PlantLine

---

## Table of Contents

1. [About this Project](#about-this-project)

2. [Automation](#automation)

3. [Data Monitoring](#data-monitoring)

4. [Hardware](#hardware)

5. [All Features](#all-features)

6. [ToDo List](#todo-list)

---

## About this Project

A **smart indoor growing station**, controlled by a **Raspberry PI**, for different plants of all kinds, also featuring **automation and data monitoring**. Since the growing station itself is (in my case) 1m long and only 20cm wide, I just decided to call it **PlantLine**. Right now, you can't build the exact same thing, but I'm already working on a tutorial if anyone would want to build this at home, in which I tell you exactly how to connect the sensors, install all needed modules, run the programm, and much more. *Also, please note that this README is about the **finished project**, and may describe things the current code is **not able to do** yet!*

---

## Automation

The plan was to create an **easy-to-use growing station** that **does most of the necessary things on its own**, like watering the plants. Of course, the user still has to **manually plant, harvest, and overall care** for the plants - as I said though, almost everything in between is done by the PlantLine itself. **Data from different sensors** (like for temperature, soil moisture, ...) is used to give the plants whatever they need right now - for example water. 

---

## Data Monitoring

With all the data from the sensors, the PlantLine is not only able to automate almost the whole growing process, but also **show some stats to the user** that might be interesting or important. For example, if the plants have grown to a desired size, the user may be notified to **harvest the plants**. All the monitoring will work via **Discord** for now - although you need to set up a bot first, I just like the implemented features (like **mention @everyone for important notifications**). Another neat things is that **multiple people can observe the same plant stats** if they are in the same server. I could do this with **MQTT** or similar things, but Discord is enough for this project right now, and I am **planning on integrating MQTT** in the future.

---

## Hardware

- **Raspberry PI 3B+**
  
  - Main component
  
  - Connects all the other components
  
  - Operates Discord bot
  
  - Runs all the scripts

- **DHT22**
  
  - Used for temperature and humidity detection
  
  - DHT22 is easy to use and returns precise measures

- **A-Z Delivery soil moisture sensor**
  
  - Used for soil moisture detection

- **IR sensor**
  
  - Any sensor will work
  
  - Used for plant height detection

- **Any water pump**
  
  - Again, anything works here
  
  - I used a 5V relay since my pump needs 12V

- **LED strips**
  
  - To make the plants grow faster and give them a better aroma
  
  - Most LED strips for plants (red and blue) work here as long as they have enough power

- **230V 12V power supply**
  
  - For water pump and LED strips

---

## All Features

Here are all the features, **summarized**:

- Get temperature

- Get humidity

- Get soil moisture

- Get plant height

- Controll water pump
  
  - Soil is not humid enough?
  
  - Wait a few hours first (to avoid the soil constantly being wet)
  
  - Then water the plant

- Use blue and red light (if needed, for example in winter)

- Send messages on Discord via bot

---

## ToDo List

- [ ] **Use sensors**
  
  - [ ] Temperature
  
  - [ ] Humidity
  
  - [ ] Soil moisture
  
  - [ ] Plant height

- [ ] **Make the plants grow**
  
  - [ ] Water the plants
  
  - [ ] Turn LED lights on/off

- [ ] **Share stats on Discord**
  
  - [x] Make a Discord bot which can post and delete messages
  
  - [ ] Post stats if requested
