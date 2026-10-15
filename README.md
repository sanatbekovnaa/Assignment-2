# Cable Measurement Program (Assignment 2)

A simple Python program that processes cable lengths measured in centimeters, classifies them into different ranges, and calculates the total and average statistics.

## Project Structure
* `measuring_cables.py`: The main source code containing the logic and functions.

## Features
* **Classification Function (`classify`):** Categorizes each cable length based on strict range constraints.
  * Below 48 cm: `Below range`
  * From 48 to 52 cm (inclusive): `In range`
  * Above 52 cm: `Above range`
* **Average Calculation (`calculate_average`):** Calculates the average length from the accumulated total and count.
* **Formatted Summary Output:** Uses Python `f-strings` to display final statistics.

## How to Run
Run the program in your terminal using:
```bash
python measuring_cables.py
```
